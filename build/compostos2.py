# -*- coding: utf-8 -*-
"""Metadados das tres secoes de suplementos."""

EXTRA_CATEGORIAS = {
    "suplemento": ("Suplementos e correlatos",
                   "Itens de venda livre, com a faixa de dose usada em estudos. Separados dos que exigem receita."),
}

EXTRA_COMPOSTOS = {
"proprio_suplementos": dict(
    nome="Suplementos de venda livre", categoria="suplemento", aprovado="parcial",
    tagline="45 itens com dose, do que tem evidência boa ao que só tem marketing",
    resumo="Quarenta e cinco suplementos de venda livre com a faixa de dose usada em estudos e em rótulo padronizado, "
           "organizados por finalidade: vitaminas e minerais, desempenho, sono e cognição, longevidade, intestino e fígado. "
           "Cada um traz a força da evidência e a ressalva que importa — limite superior, interação medicamentosa ou "
           "alegação que o dado não sustenta. É a única seção do site em que a maioria dos itens tem risco baixo e "
           "evidência decente, e é por isso que a dose aparece.",
    alerta="Dose de suplemento também tem teto. Selênio, zinco, iodo, vitamina B6 e vitamina D têm limite superior "
           "tolerável definido — passar dele não traz benefício extra, traz risco. E a melatonina, no Brasil, só é "
           "suplemento até 0,21 mg por dia.",
),
"proprio_fitoterapicos": dict(
    nome="Fitoterápicos e nootrópicos", categoria="suplemento", aprovado="nao",
    tagline="17 itens onde o marketing costuma correr à frente do dado",
    resumo="Ashwagandha, rhodiola, bacopa, ginkgo, berberina, curcumina, tongkat ali e mais dez. Risco geralmente "
           "baixo, evidência geralmente fraca e marketing geralmente forte — a tabela separa as três coisas, item a item. "
           "Traz a faixa de dose usada em estudo, a força da evidência e a ressalva de cada um, incluindo os que têm "
           "sinal de toxicidade ou interação séria.",
    alerta="Fadogia agrestis não tem ensaio humano publicado e tem sinal de toxicidade testicular e renal em roedor. "
           "Ginkgo aumenta risco de sangramento. Berberina é interator sério de CYP3A4. Ioimbina sobe pressão e "
           "frequência cardíaca.",
),
"proprio_tarja": dict(
    nome="Itens de tarja da lista", categoria="primaria", aprovado="parcial",
    tagline="13 medicamentos que apareciam misturados com suplemento",
    resumo="Anastrozol, letrozol, tamoxifeno, clomifeno, mesterolona, DHEA, pregnenolona, metformina, finasterida, "
           "dutasterida, tadalafil e clembuterol apareciam numa lista de suplementos. Não são suplementos: são "
           "medicamentos de prescrição, vários com indicação oncológica, um de uso veterinário e um esteroide "
           "anabolizante. Esta página diz o que cada um é e por que exige receita — e não traz posologia, por decisão.",
    alerta="Nenhuma dose foi publicada nesta página, deliberadamente. Tadalafil com nitrato é interação potencialmente "
           "fatal. Clembuterol e mesterolona são proibidos pela WADA.",
),
}
