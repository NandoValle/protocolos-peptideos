# -*- coding: utf-8 -*-
"""Tres secoes de suplementos, fitoterapicos e itens de tarja.

Criterio de separacao: o que exige receita nao ganha posologia aqui.
"""

SUPLEMENTOS = {

# =========================================================== 1. TARJA (13)
"proprio_tarja": dict(
    secoes=[
        dict(h="Por que estes estão separados", tipo="p", corpo=[
            "Os treze itens desta página apareciam misturados numa lista de suplementos. <strong>Não são "
            "suplementos.</strong> São medicamentos que exigem prescrição médica — vários deles com indicação "
            "oncológica, um é broncodilatador de uso veterinário e outro é esteroide anabolizante.",
            "Esta página diz o que cada um é e por que exige receita. <strong>Não traz posologia, e isso é "
            "deliberado.</strong> Dose de inibidor de aromatase ou de modulador de receptor de estrogênio sai de "
            "consulta com exame na mão, não de tabela em site.",
        ]),
        dict(h="Moduladores hormonais", tipo="p", corpo=[
            "Este é o grupo mais usado fora de indicação em contexto de fisiculturismo e de reposição hormonal "
            "caseira. Todos alteram o eixo hormonal de forma sustentada.",
        ], tabela=dict(
            cap="Inibidores de aromatase, SERMs e afins",
            linhas=[
                ["Fármaco", "O que é", "Indicação registrada", "Por que exige receita"],
                ["Anastrozol", "Inibidor de aromatase não esteroidal", "Câncer de mama hormônio-dependente em mulheres pós-menopausa",
                 "Suprime estradiol de forma acentuada. Estradiol baixo demais custa densidade óssea, perfil lipídico, libido e articulação"],
                ["Letrozol", "Inibidor de aromatase não esteroidal, mais potente que o anastrozol", "Câncer de mama; indução de ovulação em alguns protocolos",
                 "Mesma classe, supressão ainda mais profunda. Não é intercambiável com anastrozol na prática"],
                ["Tamoxifeno", "Modulador seletivo de receptor de estrogênio (SERM)", "Câncer de mama, tratamento e prevenção",
                 "Risco de tromboembolismo e de hiperplasia endometrial. Exige rastreio e acompanhamento"],
                ["Clomifeno (Clomid)", "SERM, agonista/antagonista de estrogênio no hipotálamo", "Indução de ovulação em infertilidade feminina",
                 "Uso masculino para elevar testosterona é off-label. Alterações visuais são efeito descrito em bula"],
                ["Mesterolona (Proviron)", "<strong>Esteroide androgênico anabolizante</strong> oral", "Hipogonadismo masculino, em alguns países",
                 "É anabolizante. Supressão do eixo, perfil lipídico e efeito hepático entram na conta"],
                ["DHEA", "Pró-hormônio precursor de testosterona e estradiol", "Uso restrito; no Brasil é substância controlada",
                 "Converte-se em hormônio sexual de forma variável entre pessoas. Não é vitamina"],
                ["Pregnenolona", "Precursor esteroide a montante de todo o eixo", "Sem indicação consolidada",
                 "Está no topo da cascata esteroide: mexer aqui move tudo abaixo, de forma pouco previsível"],
            ])),
        dict(h="Cardiometabólicos e urológicos", tipo="p", corpo=[], tabela=dict(
            cap="Demais fármacos da lista",
            linhas=[
                ["Fármaco", "O que é", "Indicação registrada", "Por que exige receita"],
                ["Metformina", "Biguanida, reduz produção hepática de glicose e melhora sensibilidade à insulina",
                 "Diabetes tipo 2; síndrome dos ovários policísticos",
                 "Exige função renal avaliada. Acidose láctica é rara e grave. Reduz absorção de vitamina B12 no uso prolongado"],
                ["Finasterida", "Inibidor da 5-alfa-redutase tipo 2", "Hiperplasia prostática benigna; alopecia androgenética",
                 "Efeitos sexuais persistentes são descritos e discutidos na literatura. Altera o valor do PSA, o que interfere no rastreio de câncer de próstata"],
                ["Dutasterida", "Inibidor da 5-alfa-redutase tipos 1 e 2", "Hiperplasia prostática benigna",
                 "Mesma classe, supressão mais ampla e meia-vida muito mais longa — semanas, não horas"],
                ["Tadalafil", "Inibidor da fosfodiesterase tipo 5", "Disfunção erétil; hiperplasia prostática; hipertensão pulmonar",
                 "<strong>Interação potencialmente fatal com nitratos.</strong> Exige avaliação cardiovascular antes"],
                ["Clembuterol", "Agonista beta-2 adrenérgico", "Broncodilatador — em vários países, <strong>apenas uso veterinário</strong>",
                 "Usado fora de indicação para perda de gordura. Taquicardia, arritmia, tremor e hipocalemia. Proibido pela WADA"],
            ])),
        dict(h="O que fazer com esta página", tipo="li", corpo=[
            "<strong>Se um deles te interessa, leve o nome ao seu médico.</strong> É literalmente para isso que "
            "esta página existe: para você chegar informado, não para se automedicar.",
            "<strong>Nenhum deles é suplemento</strong>, mesmo aparecendo em catálogo ao lado de vitamina D e "
            "creatina. O contexto de venda não muda a natureza da molécula.",
            "<strong>Clembuterol e mesterolona são proibidos pela WADA.</strong> Quem compete em esporte federado "
            "não tem margem aqui.",
            "<strong>Tadalafil com nitrato é a interação mais perigosa desta página inteira.</strong> Quem usa "
            "nitrato para angina precisa saber disso antes de qualquer outra coisa.",
        ]),
    ],
    referencias=[
        ("Nenhuma dose foi publicada nesta página, por decisão editorial. As indicações registradas devem ser conferidas na bula do produto e na base da ANVISA.", "https://consultas.anvisa.gov.br/#/medicamentos/"),
    ],
),

# ==================================================== 2. FITOTERÁPICOS (17)
"proprio_fitoterapicos": dict(
    secoes=[
        dict(h="O critério desta página", tipo="p", corpo=[
            "Fitoterápico e nootrópico de venda livre ocupam um lugar incômodo: risco geralmente baixo, evidência "
            "geralmente fraca, e marketing geralmente forte. A tabela abaixo separa as três coisas.",
            "A coluna <strong>Evidência</strong> é a que importa. <em>Razoável</em> significa que existem ensaios "
            "randomizados replicados. <em>Fraca</em> significa estudo pequeno, resultado inconsistente ou desfecho "
            "substituto. <em>Muito fraca</em> significa que a alegação corre à frente do dado.",
        ]),
        dict(h="Adaptógenos e cognição", tipo="p", corpo=[], tabela=dict(
            cap="Adaptógenos, nootrópicos e cognitivos",
            linhas=[
                ["Item", "Faixa usual em estudos", "Para quê", "Evidência", "Ressalva"],
                ["Ashwagandha (KSM-66)", "300–600 mg/dia do extrato padronizado", "Estresse, cortisol, sono, testosterona",
                 "Razoável para estresse e sono", "Relatos de hepatotoxicidade levaram agências nórdicas a emitir alertas. Evitar em doença hepática e em tireoidopatia"],
                ["Rhodiola rosea", "200–600 mg/dia (3% rosavinas / 1% salidrosídeo)", "Fadiga mental, estresse",
                 "Fraca a razoável", "Estudos pequenos, padronização de extrato muito variável entre marcas"],
                ["Bacopa monnieri", "300 mg/dia (50% bacosídeos), por 8–12 semanas", "Memória e aprendizado",
                 "Razoável, com efeito modesto", "O efeito só aparece após semanas. Desconforto gastrointestinal é comum"],
                ["Panax ginseng", "200–400 mg/dia do extrato padronizado", "Fadiga, cognição",
                 "Fraca", "Interage com anticoagulantes e antidiabéticos"],
                ["Lion's Mane (Hericium erinaceus)", "500–3.000 mg/dia", "Cognição, fator de crescimento neural",
                 "Muito fraca em humanos", "A base é quase toda pré-clínica. Estudos humanos são poucos e pequenos"],
                ["Ginkgo biloba", "120–240 mg/dia (EGb 761)", "Circulação cerebral, memória",
                 "Fraca — grandes ensaios em prevenção de demência foram negativos",
                 "<strong>Aumenta risco de sangramento.</strong> Suspender antes de cirurgia; cuidado com anticoagulante"],
                ["Piracetam", "1,2–4,8 g/dia", "Nootrópico racetam clássico",
                 "Fraca em população saudável", "<strong>No Brasil é medicamento com prescrição</strong>, não suplemento. Está aqui porque aparecia na lista"],
                ["Fosfatidilserina", "100–300 mg/dia", "Memória, cortisol pós-exercício",
                 "Fraca a razoável", "A evidência antiga usava fonte bovina; os produtos atuais são de soja, com dados menos robustos"],
            ])),
        dict(h="Metabólicos e hepáticos", tipo="p", corpo=[], tabela=dict(
            cap="Glicemia, lipídios e fígado",
            linhas=[
                ["Item", "Faixa usual em estudos", "Para quê", "Evidência", "Ressalva"],
                ["Berberina", "500 mg, 2–3×/dia, antes das refeições", "Glicemia, perfil lipídico",
                 "Razoável — efeito comparável ao de fármacos em alguns ensaios",
                 "<strong>Inibe CYP3A4 e é um interator sério.</strong> Não combinar com estatina, ciclosporina ou imunossupressor sem orientação"],
                ["Curcumina com piperina", "500–1.000 mg/dia de curcuminoides", "Inflamação, dor articular",
                 "Razoável para osteoartrite", "A piperina que aumenta a absorção também aumenta a de outros fármacos. Pode aumentar risco de sangramento"],
                ["Silimarina (cardo mariano)", "200–400 mg/dia", "Proteção hepática",
                 "Fraca — ensaios em hepatite tiveram resultado inconsistente", "Vendida como detox, o que não é um desfecho clínico"],
                ["Bergamota (Citrus bergamia)", "500–1.000 mg/dia do extrato", "Colesterol",
                 "Fraca", "Estudos majoritariamente italianos e pequenos"],
                ["Canela (extrato)", "1–6 g/dia", "Glicemia",
                 "Fraca e inconsistente", "A canela cássia contém cumarina, hepatotóxica em dose alta. A variedade Ceylon tem muito menos"],
                ["Ácido corosólico (banaba)", "10–50 mg/dia", "Glicemia",
                 "Muito fraca", "Poucos ensaios humanos, todos pequenos"],
            ])),
        dict(h="Testosterona, libido e o resto", tipo="p", corpo=[], tabela=dict(
            cap="Os de alegação hormonal",
            linhas=[
                ["Item", "Faixa usual em estudos", "Para quê", "Evidência", "Ressalva"],
                ["Tongkat Ali (Eurycoma longifolia)", "200–400 mg/dia do extrato padronizado", "Testosterona, libido, estresse",
                 "Fraca a razoável", "O efeito sobre testosterona aparece sobretudo em quem partia de nível baixo"],
                ["Fadogia agrestis", "não estabelecida em humanos", "Testosterona",
                 "<strong>Muito fraca — não há ensaio humano publicado</strong>",
                 "<strong>Sinal de toxicidade testicular e renal em roedores.</strong> Popularizado por podcast, não por evidência"],
                ["Shilajit", "250–500 mg/dia", "Testosterona, energia, ácido fúlvico",
                 "Muito fraca", "Risco de contaminação por metal pesado no produto não purificado. Exigir laudo"],
                ["Yohimbina HCl", "5–10 mg antes do treino ou em jejum", "Perda de gordura, disfunção erétil",
                 "Fraca para gordura; alguma para disfunção erétil",
                 "<strong>Ansiedade, taquicardia e picos de pressão.</strong> Não usar com IMAO, com hipertensão ou com transtorno de ansiedade"],
            ])),
    ],
    referencias=[
        ("As faixas de dose desta página são as usadas em ensaios publicados e em rótulos padronizados. Não foram conferidas artigo por artigo nesta compilação, diferente das páginas de Thymalin, bioreguladores e Meldonium.", "https://pubmed.ncbi.nlm.nih.gov/"),
        ("Para conferir a situação regulatória no Brasil de qualquer item desta lista, a base da ANVISA é a referência.", "https://consultas.anvisa.gov.br/"),
    ],
),
}
