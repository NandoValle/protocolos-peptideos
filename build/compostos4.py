# -*- coding: utf-8 -*-
"""Metadados das paginas de evidencia do KLOW e do Semax."""

EXTRA3 = {
"proprio_klow_evidencia": dict(
    nome="KLOW — a evidência", categoria="primaria", aprovado="nao",
    tagline="A blend segue sem ensaio, mas três componentes entraram em fase clínica em 2026",
    resumo="Companheira da página de protocolo do KLOW. Nenhum estudo jamais testou os quatro peptídeos juntos, e "
           "isso não mudou. O que mudou é que BPC-157, TB-500 e GHK-Cu entraram em ensaio clínico formal pela "
           "primeira vez: três estudos da Hudson Biotech, de fase 1/2 e 2, começaram em fevereiro de 2026 e estão "
           "recrutando. Deixou de ser verdade dizer que a evidência desses compostos é só pré-clínica — mas nenhum "
           "dos ensaios testa a combinação, e o KPV continua sem nada.",
    alerta="Os ensaios testam os componentes isoladamente e em indicações diferentes — isquiotibiais, doença "
           "cardiovascular e gel tópico para ferida. O ensaio de GHK-Cu é tópico, não injetável: não valida o "
           "protocolo subcutâneo do KLOW.",
),
"proprio_semax_evidencia": dict(
    nome="Semax — a evidência", categoria="primaria", aprovado="parcial",
    tagline="A dose dos ensaios russos é de 12 a 72 vezes a da comunidade",
    resumo="Companheira da página de protocolo do Semax, e a maior discrepância que este site encontrou. Os quatro "
           "ensaios clínicos publicados usaram 6.000, 12.000 e 18.000 mcg por dia; a faixa que circula na comunidade "
           "é de 250 a 1.000 mcg. São contextos diferentes — AVC agudo em hospital contra cognição no dia a dia — "
           "mas a consequência é que a faixa praticada nunca foi testada em ensaio nenhum. Zero registros no "
           "ClinicalTrials.gov, e um dos quatro estudos é francamente negativo.",
    alerta="Nenhum dos quatro ensaios foi feito em pessoa saudável. A base clínica do Semax é toda em doença — AVC, "
           "neurônio motor, nervo óptico — e não diz nada sobre cognição em quem está bem, que é o uso mais comum "
           "fora da Rússia.",
),
}
