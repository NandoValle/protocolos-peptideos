# -*- coding: utf-8 -*-
"""Prova que a trava de reconstituicao PEGA erro, em cada um dos cinco formatos.

Cobertura sem poder de deteccao nao vale nada: uma trava que le 485 celulas e
nunca acusaria nada passaria neste site exatamente como a de verdade. Este
teste separa as duas coisas.

Copia p/ para uma pasta temporaria, injeta UM erro de dose por vez -- sempre um
fator de 10, que e o modo de falhar que machuca -- e verifica que a trava acusa
no formato certo. O primeiro caso e o bug real de 05/09/2026, na tirzepatida,
que deu origem a trava; os outros quatro cobrem os formatos que entraram depois.

O site original nunca e tocado: a copia e apagada no fim.

    python build/testa_reconstituicao.py

Codigo de saida 1 se algum erro injetado passar batido.
"""
import io, os, re, shutil, sys, tempfile
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import trava_reconstituicao as T

CASOS = [
    # o bug original de 05/09/2026, que deu origem a trava: regressao do F1
    ("F1 Tirzepatida", "protocol_tirzepatide.html", '<td class="num">1,125 mL / dividida</td>',
                                                    '<td class="num">1.125 mL / dividida</td>'),
    ("F2 GHRP-6",      "protocol_ghrp-6.html",      '<td class="num">0,06 mL</td>',        '<td class="num">0,60 mL</td>'),
    ("F3 Pinealon",    "protocol_pinealon.html",    '0,10 mg (100 mcg)',                   '1,00 mg (1000 mcg)'),
    ("F4 Semaglutide", "protocol_semaglutide.html", '<td class="num">0,20 mL (20 u)</td>', '<td class="num">2,00 mL (20 u)</td>'),
    ("F5 LL-37",       "protocol_ll-37.html",       '<td class="num">0,08 mL</td>',        '<td class="num">0,80 mL</td>'),
]

base = tempfile.mkdtemp(prefix="trava-inj-")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
shutil.copytree(os.path.join(RAIZ, "p"), os.path.join(base, "p"))

f, t, c = T.checar(base)
print("copia limpa: %d tabelas, %d celulas, %d divergencias" % (t, c, len(f)))
assert not f, "a copia limpa ja acusa: %s" % f
print()

falhou = False
for nome, arq, de, para in CASOS:
    p = os.path.join(base, "p", arq)
    orig = io.open(p, encoding="utf-8").read()
    if de not in orig:
        print("%-16s NAO CONSEGUI INJETAR (nao achei %r)" % (nome, de))
        falhou = True
        continue
    io.open(p, "w", encoding="utf-8").write(orig.replace(de, para, 1))
    faltas, _, _ = T.checar(base)
    io.open(p, "w", encoding="utf-8").write(orig)
    marca = nome.split()[0]
    pegou = [x for x in faltas if "[%s]" % marca in x]
    print("%-16s %s  (%d divergencia(s))" % (nome, "PEGOU" if pegou else "PASSOU BATIDO", len(faltas)))
    for x in faltas:
        print("      " + x)
    if not pegou:
        falhou = True

f, t, c = T.checar(base)
print()
print("copia restaurada: %d tabelas, %d celulas, %d divergencias" % (t, c, len(f)))
shutil.rmtree(base)
sys.exit(1 if falhou or f else 0)
