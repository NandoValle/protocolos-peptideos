# -*- coding: utf-8 -*-
"""Trava que confere a aritmetica das tabelas de reconstituicao.

POR QUE EXISTE

As tabelas de reconstituicao trazem frasco, agua, concentracao e o volume de
cada dose. Isso e aritmetica fechada:

    volume = dose / concentracao

Nao precisa de fonte externa: a propria tabela se verifica. E um erro aqui e
um erro de dose por fator de 2 ou de 10, que e o modo de falhar que machuca.

Foi assim que a trava nasceu. Em 05/09/2026 uma auditoria manual encontrou,
em 416 celulas, um erro: a tirzepatida trazia "1.125 mL / dividida" onde a
conta da propria tabela dava 1,125 mL -- em portugues, mil cento e vinte e
cinco mililitros. A causa era o encadeamento do dicionario com a regra de
milhar: o dicionario convertia o decimal ingles para virgula, e a regra de
milhar via "1,125" e devolvia "1.125". Auditoria manual nao se repete sozinha;
trava, sim.

OS CINCO FORMATOS

A mesma conta aparece no site em cinco arranjos de tabela. A primeira versao
desta trava so lia o primeiro e cobria 43 tabelas; os outros quatro entraram
em 05/09/2026 e levaram a cobertura a 56 tabelas e 485 celulas.

  F1  concentracao numa coluna, a dose no CABECALHO das colunas seguintes,
      o volume na celula.  ->  volume = dose / concentracao
  F2  dose, concentracao e volume, cada um em sua coluna, na mesma linha.
      ->  volume = dose / concentracao
  F3  o cabecalho declara quantas unidades de insulina se aspira ("10 unidades
      (0,10 mL) entregam") e a celula declara a massa entregue.
      ->  massa = volume x concentracao
  F4  a tabela NAO publica concentracao: publica frasco e agua. A concentracao
      sai da divisao.  ->  volume = dose / (frasco / agua)
  F5  so ha Dose e Volume. A concentracao nao esta escrita em lugar nenhum da
      tabela: e a mediana das razoes dose/volume das proprias linhas. Confere
      so a coerencia interna -- pega uma linha fora da curva, nao pega a tabela
      inteira errada -- e por isso roda com tolerancia mais larga.

TRES ARMADILHAS JA PAGAS, que estao no codigo abaixo:

  1. A celula costuma trazer a unidade de insulina ANTES do volume, como em
     "5 unidades (0,05 mL)". Ler o primeiro numero devolve 5 em vez de 0,05,
     e todo divergente sai com fator 100 -- que e exatamente a razao entre
     unidade e mL. Por isso o volume e lido pelo numero que precede "mL".

  2. Em frasco combinado, a concentracao total nao e a de cada peptideo. A
     tabela do CJC-1295 + ipamorelina diz "10,0 mg/mL no total (5,0 mg/mL de
     cada)" e tem coluna propria "Por peptideo". A dose e de cada um, entao a
     conta usa a concentracao por peptideo. Tabela com "de cada" ou "por
     peptideo" no cabecalho da concentracao usa o menor valor da celula.

  3. No F3 a mesma confusao aparece pelo avesso: no KLOW a concentracao
     publicada e a do blend inteiro ("Concentracao total", 40 mg/mL) e a
     coluna nomeia UM componente ("GHK-Cu por unidade", ~250 mcg). A conta
     0,01 mL x 40 mg/mL = 400 mcg esta certa para o blend e errada para o
     GHK-Cu: 250 + 50 x 3 = 400. Sao os quatro componentes. Coluna de
     componente contra concentracao total nao se confere -- se pula.

Roda sozinha (`python build/trava_reconstituicao.py`) e no hook de pre-commit.
Codigo de saida 1 em caso de divergencia.
"""
import glob
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOLERANCIA = 0.05          # 5%: absorve arredondamento de tabela
TOLERANCIA_F5 = 0.10       # concentracao inferida da propria tabela: mais folga
VOL = re.compile(r"(\d[\d.]*(?:,\d+)?)\s*mL")
NUM = re.compile(r"(\d[\d.]*(?:,\d+)?)")
UNI = re.compile(r"(\d[\d.]*(?:,\d+)?)\s*unidade")
CONC = re.compile("oncentra")
CAB_DOSE = re.compile(r"dose|quantidade de pesquisa|quantidade-alvo", re.I)
CAB_VOL = re.compile(r"volume|aspirar", re.I)
CAB_AGUA = re.compile(r"gua bacteriost", re.I)
CAB_FRASCO = re.compile(r"frasco|vial", re.I)
COMBINADO = re.compile(r"de cada|por pept", re.I)


def limpo(c):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", "", c)).strip()


def pt(txt):
    """'5.000' -> 5000.0 ; '0,075' -> 0.075. Ponto e milhar em PT-BR."""
    return float(txt.replace(".", "").replace(",", "."))


def massa_mcg(txt, menor=False):
    """Converte a primeira massa do texto para mcg. Com menor=True, usa a
    menor de todas -- e o caso do frasco combinado, em que o cabecalho traz
    o total e o valor por peptideo na mesma celula."""
    vals = []
    for m in NUM.finditer(txt):
        v = pt(m.group(1))
        resto = txt[m.end():m.end() + 8]
        if re.match(r"\s*mg", resto):
            vals.append(v * 1000)
        elif re.match(r"\s*(mcg|µg)", resto):
            vals.append(v)
    if not vals:
        return None
    return min(vals) if menor else vals[0]


def volume(txt):
    """O volume e o numero que PRECEDE 'mL' -- ver armadilha 1."""
    m = VOL.search(txt)
    return pt(m.group(1)) if m else None


def coluna(cab, rx):
    return next((i for i, c in enumerate(cab) if rx.search(c)), None)


def _tabelas(raiz):
    """Devolve (arquivo, legenda, cabecalho, linhas) de cada tabela de
    reconstituicao publicada."""
    for f in sorted(glob.glob(os.path.join(raiz, "p", "*.html"))):
        h = io.open(f, encoding="utf-8", errors="replace").read()
        for cap, bloco in re.findall(
                r'<div class="tabela-titulo">(.*?)</div>(.*?)</table>', h, re.S):
            if "reconstitui" not in cap.lower():
                continue
            linhas = re.findall(r"<tr>(.*?)</tr>", bloco, re.S)
            if len(linhas) < 2:
                continue
            celulas = [[limpo(c) for c in
                        re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", l, re.S)]
                       for l in linhas]
            yield os.path.basename(f), limpo(cap)[:40], celulas[0], celulas[1:]


def checar(raiz=RAIZ):
    faltas = []
    tabelas = celulas = 0

    def erra(fmt, rot, msg):
        faltas.append("%s [%s] %s" % (rot, fmt, msg))

    for arq, cap, cab, corpo in _tabelas(raiz):
        rot = "%s | %s" % (arq, cap)
        i_conc = coluna(cab, CONC)
        i_dose = coluna(cab, CAB_DOSE)
        i_vol = coluna(cab, CAB_VOL)
        n = 0

        # -------------------------------------------------- F1
        if i_conc is not None:
            doses = {i: massa_mcg(c) for i, c in enumerate(cab)
                     if i > i_conc and massa_mcg(c)}
            if doses:
                combinado = bool(COMBINADO.search(cab[i_conc]))
                for cels in corpo:
                    if len(cels) <= i_conc:
                        continue
                    tc = cels[i_conc]
                    conc = massa_mcg(tc, menor=combinado or bool(COMBINADO.search(tc)))
                    if not conc:
                        continue
                    for i, dose in doses.items():
                        if i >= len(cels):
                            continue
                        vol = volume(cels[i])
                        if vol is None:
                            continue
                        n += 1
                        esperado = dose / conc
                        if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA:
                            erra("F1", rot,
                                 "concentracao %g mcg/mL, dose %g mcg: a tabela diz "
                                 "%g mL e a conta da %.4g mL (fator %.2f)"
                                 % (conc, dose, vol, esperado, vol / esperado))
                if n:
                    tabelas += 1
                    celulas += n
                    continue

        # -------------------------------------------------- F2
        if (i_conc is not None and i_dose is not None and i_vol is not None
                and i_dose != i_conc and i_vol != i_conc):
            for cels in corpo:
                if max(i_dose, i_vol, i_conc) >= len(cels):
                    continue
                dose = massa_mcg(cels[i_dose])
                conc = massa_mcg(cels[i_conc])
                vol = volume(cels[i_vol])
                if not (dose and conc and vol is not None):
                    continue
                n += 1
                esperado = dose / conc
                if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA:
                    erra("F2", rot,
                         "concentracao %g mcg/mL, dose %g mcg: a tabela diz %g mL "
                         "e a conta da %.4g mL (fator %.2f)"
                         % (conc, dose, vol, esperado, vol / esperado))
            if n:
                tabelas += 1
                celulas += n
                continue

        # -------------------------------------------------- F3
        if i_conc is not None:
            for j, ch in enumerate(cab):
                if j == i_conc:
                    continue
                mu, mvh = UNI.search(ch), VOL.search(ch)
                if not (mu or mvh):
                    continue
                vol_cab = pt(mvh.group(1)) if mvh else pt(mu.group(1)) / 100.0
                for cels in corpo:
                    if max(j, i_conc) >= len(cels):
                        continue
                    tc, tx = cels[i_conc], cels[j]
                    # celula que soma componentes, ou que fala de cada um
                    if "+" in tx or COMBINADO.search(tx):
                        continue
                    # armadilha 3: coluna de componente contra concentracao total
                    if ("total" in (tc + " " + cab[i_conc]).lower()
                            and "total" not in (tx + " " + ch).lower()):
                        continue
                    conc, massa = massa_mcg(tc), massa_mcg(tx)
                    if not (conc and massa):
                        continue
                    vc = volume(tx)
                    vol = vc if vc is not None else vol_cab
                    n += 1
                    esperado = vol * conc
                    if esperado > 0 and abs(massa - esperado) / esperado > TOLERANCIA:
                        erra("F3", rot,
                             "'%s': %g mL x %g mcg/mL da %.4g mcg e a tabela diz "
                             "%g mcg (fator %.2f)"
                             % (ch[:30], vol, conc, esperado, massa, massa / esperado))
            if n:
                tabelas += 1
                celulas += n
                continue

        # -------------------------------------------------- F4
        i_agua, i_frasco = coluna(cab, CAB_AGUA), coluna(cab, CAB_FRASCO)
        if i_agua is not None and i_frasco is not None and i_agua != i_frasco:
            doses = {i: massa_mcg(c) for i, c in enumerate(cab)
                     if i not in (i_agua, i_frasco) and massa_mcg(c)}
            if doses:
                for cels in corpo:
                    if max(i_agua, i_frasco) >= len(cels):
                        continue
                    frasco = massa_mcg(cels[i_frasco])
                    agua = volume(cels[i_agua])
                    if not frasco or not agua:
                        continue
                    conc = frasco / agua
                    for i, dose in doses.items():
                        if i >= len(cels):
                            continue
                        vol = volume(cels[i])
                        if vol is None:
                            continue
                        n += 1
                        esperado = dose / conc
                        if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA:
                            erra("F4", rot,
                                 "frasco %g mcg em %g mL da %g mcg/mL; dose %g mcg "
                                 "pede %.4g mL e a tabela diz %g mL (fator %.2f)"
                                 % (frasco, agua, conc, dose, esperado, vol,
                                    vol / esperado))
                if n:
                    tabelas += 1
                    celulas += n
                    continue

        # -------------------------------------------------- F5
        if (i_conc is None and i_dose is not None and i_vol is not None
                and i_dose != i_vol):
            pares = []
            for cels in corpo:
                if max(i_dose, i_vol) >= len(cels):
                    continue
                dose, vol = massa_mcg(cels[i_dose]), volume(cels[i_vol])
                if dose and vol:
                    pares.append((dose, vol))
            # com menos de tres linhas a mediana nao tem de onde sair
            if len(pares) >= 3:
                razoes = sorted(d / v for d, v in pares)
                conc = razoes[len(razoes) // 2]
                tabelas += 1
                celulas += len(pares)
                for dose, vol in pares:
                    esperado = dose / conc
                    if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA_F5:
                        erra("F5", rot,
                             "as linhas da tabela dao %g mcg/mL; nessa concentracao "
                             "a dose de %g mcg pede %.4g mL e a tabela diz %g mL "
                             "(fator %.2f)"
                             % (conc, dose, esperado, vol, vol / esperado))

    return faltas, tabelas, celulas


def main():
    faltas, tabelas, celulas = checar()
    if faltas:
        print("TRAVA DE RECONSTITUICAO: %d divergencia(s)\n" % len(faltas), file=sys.stderr)
        for f in faltas:
            print("  " + f, file=sys.stderr)
        print("\nvolume = dose / concentracao. Leia o cabecalho de "
              "build/trava_reconstituicao.py.", file=sys.stderr)
        return 1
    print("trava de reconstituicao: ok (%d tabelas, %d celulas)" % (tabelas, celulas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
