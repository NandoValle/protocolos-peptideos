# -*- coding: utf-8 -*-
"""Metadado da pagina de ajuste de dose por funcao renal."""

EXTRA12 = {
"proprio_dose_renal": dict(
    nome="Ajuste de dose por função renal", categoria="primaria", aprovado="parcial",
    tagline="Onde o dado existe, a bula manda não ajustar nada — e o risco de verdade está três seções "
            "acima, num item que quase ninguém lê",
    resumo="Página que nasceu de uma lacuna declarada: a de doença renal diz que não traz ajuste de dose, e "
           "esta explica por quê. Extraí a seção 8.6 direto do endpoint de rótulos da openFDA, composto por "
           "composto. Semaglutida e tirzepatida: nenhum ajuste, nem em doença renal em estágio terminal, "
           "porque a farmacocinética não muda. Bremelanotida: cautela abaixo de 30 mL/min/1,73 m². "
           "Tesamorelina: a bula declara que a farmacocinética em insuficiência renal não foi estabelecida — "
           "num peptídeo aprovado pela FDA. Para os outros onze compostos consultados, de BPC-157 a "
           "Cerebrolisina, a base da FDA devolveu zero rótulos: não há o que ajustar porque não há o que "
           "consultar. E o achado que reorganiza a leitura: os dois GLP-1 trazem, nas advertências, um item "
           "chamado Lesão Renal Aguda por Depleção de Volume — o risco renal não vem da molécula, vem do "
           "vômito e da diarreia desidratarem quem continua tomando.",
    alerta="\"Nenhum ajuste de dose\" responde a uma pergunta só — se o remédio se acumula no rim doente — e "
           "não à outra, se o remédio pode piorar o rim. A página traz também a armadilha que atinge quem "
           "treina: creatina, massa muscular e dieta rica em proteína elevam a creatinina do sangue sem "
           "lesão renal, e a TFGe calculada a partir dela vem pior do que a realidade. Nesses casos o exame "
           "certo é a cistatina C.",
),
}
