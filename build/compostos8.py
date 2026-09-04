# -*- coding: utf-8 -*-
"""Metadado da varredura de registro na ANVISA."""

from datas import DATA_APURACAO as _DT

EXTRA7 = {
"proprio_anvisa": dict(
    nome="O que existe no Brasil", categoria="primaria", aprovado="nao",
    tagline="40 dos 44 compostos deste site não têm nenhum medicamento registrado na ANVISA",
    resumo=f"Varredura do dado aberto oficial da ANVISA — 43.489 registros de medicamento, baixado em {_DT}"
           " — atrás de cada composto do site, por princípio ativo e por nome de produto. "
           "Quatro existem: semaglutida, tirzepatida, ocitocina e azul de metileno. Os outros quarenta não têm "
           "bula brasileira, dose aprovada nem lote fiscalizado. O resultado agora aparece em cada página de "
           "composto, numa linha própria. O achado lateral mais inesperado: já existem genéricos e similares de "
           "semaglutida registrados no Brasil, de EMS, Germed, Sun e outras — são quinze produtos ao todo.",
    alerta="A primeira tentativa desta varredura usou o bulário e devolveu zero para quarenta compostos. O "
           "controle salvou o resultado: 'insulina' também deu zero no bulário, porque ele busca por nome de "
           "produto e insulina se vende como Lantus e Humalog. Quarenta zeros certos pelo motivo errado ainda "
           "são resultado inválido. A contagem publicada aqui vem do dado aberto, que traz o princípio ativo em "
           "coluna própria, e foi validada com três controles positivos e um grupo de controle inteiro.",
),
}
