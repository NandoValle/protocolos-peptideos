# -*- coding: utf-8 -*-
"""Metadado da auditoria dos GLP-1 contra a bula."""

from datas import DATA_APURACAO as _DT

EXTRA6 = {
"proprio_glp1_bula": dict(
    nome="Os GLP-1 contra a bula", categoria="primaria", aprovado="parcial",
    tagline="As doses estavam certas. A tarja preta estava faltando",
    resumo="Primeira auditoria deste site contra um gabarito oficial. Comparei as cinco escadas de titulação de "
           f"semaglutida e tirzepatida, degrau por degrau, com as bulas aprovadas pela FDA, lidas em {_DT}"
           ". Nenhum valor de dose está errado — e o site até acerta um detalhe difícil, que 7,5 e 12,5 mg "
           "de tirzepatida são degraus de passagem e não de manutenção. Mas faltavam seis instruções da bula, e "
           "faltava a coisa mais importante: nas nove páginas de GLP-1 não havia uma única menção a tireoide, "
           "carcinoma medular ou NEM 2. Numa segunda rodada li as quatro bulas da ANVISA, e elas divergem da FDA em "
           "seis pontos — inclusive uma dose de 7,2 mg do Wegovy que não existe nos Estados Unidos.",
    alerta="Semaglutida e tirzepatida têm tarja preta da FDA por tumor de células C da tireoide em roedores. No "
           "Brasil o tratamento é diferente para cada uma: a bula do MOUNJARO contraindica carcinoma medular de "
           "tireoide e NEM 2, e as de Ozempic, Wegovy e Rybelsus apenas pedem cautela. Este site publicava a "
           "titulação completa sem nada disso. A falha era minha, não da fonte, e está corrigida nas nove páginas.",
),
}
