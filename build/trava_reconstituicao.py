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

DUAS ARMADILHAS JA PAGAS, que estao no codigo abaixo:

  1. A celula costuma trazer a unidade de insulina ANTES do volume, como em
     "5 unidades (0,05 mL)". Ler o primeiro numero devolve 5 em vez de 0,05,
     e todo divergente sai com fator 100 -- que e exatamente a razao entre
     unidade e mL. Por isso o volume e lido pelo numero que precede "mL".

  2. Em frasco combinado, a concentracao total nao e a de cada peptideo. A
     tabela do CJC-1295 + ipamorelina diz "10,0 mg/mL no total (5,0 mg/mL de
     cada)" e tem coluna propria "Por peptideo". A dose e de cada um, entao a
     conta usa a concentracao por peptideo. Tabela com "de cada" ou "por
     peptideo" no cabecalho da concentracao usa o menor valor da celula.

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
VOL = re.compile(r"(\d[\d.]*(?:,\d+)?)\s*mL")
NUM = re.compile(r"(\d[\d.]*(?:,\d+)?)")


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


def checar(raiz=RAIZ):
    faltas = []
    tabelas = celulas = 0
    for f in sorted(glob.glob(os.path.join(raiz, "p", "*.html"))):
        h = io.open(f, encoding="utf-8", errors="replace").read()
        for cap, bloco in re.findall(r'<div class="tabela-titulo">(.*?)</div>(.*?)</table>', h, re.S):
            if "reconstitui" not in cap.lower():
                continue
            linhas = re.findall(r"<tr>(.*?)</tr>", bloco, re.S)
            if len(linhas) < 2:
                continue
            cab = [limpo(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", linhas[0], re.S)]
            i_conc = next((i for i, c in enumerate(cab) if "oncentra" in c), None)
            if i_conc is None:
                continue
            # frasco combinado: a dose e por peptideo, nao do total
            combinado = bool(re.search(r"de cada|por pept", cab[i_conc], re.I))
            doses = {}
            for i, c in enumerate(cab):
                if i <= i_conc:
                    continue
                d = massa_mcg(c)
                if d:
                    doses[i] = d
            if not doses:
                continue
            tabelas += 1
            for lin in linhas[1:]:
                cels = [limpo(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", lin, re.S)]
                if len(cels) <= i_conc:
                    continue
                texto_conc = cels[i_conc]
                conc = massa_mcg(texto_conc,
                                 menor=combinado or bool(re.search(r"de cada|por pept", texto_conc, re.I)))
                if not conc:
                    continue
                for i, dose in doses.items():
                    if i >= len(cels):
                        continue
                    mv = VOL.search(cels[i])
                    if not mv:
                        continue
                    vol = pt(mv.group(1))
                    esperado = dose / conc
                    celulas += 1
                    if esperado <= 0:
                        continue
                    if abs(vol - esperado) / esperado > TOLERANCIA:
                        faltas.append(
                            "%s | %s | concentracao %g mcg/mL, dose %g mcg: "
                            "a tabela diz %g mL e a conta da %.4g mL (fator %.2f)"
                            % (os.path.basename(f), limpo(cap)[:40], conc, dose,
                               vol, esperado, vol / esperado))
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
