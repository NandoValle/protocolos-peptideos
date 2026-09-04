# -*- coding: utf-8 -*-
"""Fitoterapicos e itens de tarja.

A coluna "ECR/meta" traz a contagem de ensaios randomizados e metanalises
no PubMed, conferida em 04/09/2026, item a item.
"""

SUPLEMENTOS = {

# =========================================================== 1. TARJA (13)
"proprio_tarja": dict(
    secoes=[
        dict(h="Por que estes estão separados", tipo="p", corpo=[
            "Os treze itens desta página apareciam misturados numa lista de suplementos. <strong>Não são "
            "suplementos.</strong> São medicamentos que exigem prescrição médica — vários com indicação "
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
                ["Clomifeno (Clomid)", "SERM, agonista e antagonista de estrogênio conforme o tecido", "Indução de ovulação em infertilidade feminina",
                 "Uso masculino para elevar testosterona é off-label. Alterações visuais constam em bula"],
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
                ["Metformina", "Biguanida; reduz produção hepática de glicose e melhora sensibilidade à insulina",
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
        ("Nenhuma dose foi publicada nesta página, por decisão editorial. As indicações registradas devem ser conferidas na bula do produto e na base da ANVISA.",
         "https://consultas.anvisa.gov.br/#/medicamentos/"),
    ],
),

# ==================================================== 2. FITOTERÁPICOS (17)
"proprio_fitoterapicos": dict(
    secoes=[
        dict(h="Como ler esta página", tipo="p", corpo=[
            "Fitoterápico e nootrópico de venda livre ocupam um lugar incômodo: risco geralmente baixo, evidência "
            "muito desigual e marketing sempre forte. As tabelas separam as três coisas.",
            "A coluna <strong>ECR/meta</strong> traz o número de ensaios randomizados e metanálises indexados no "
            "PubMed, <strong>conferido item a item em 4 de setembro de 2026</strong>. É número, não opinião — e em "
            "alguns casos ele contradiz a fama do produto nas duas direções.",
        ]),
        dict(h="Adaptógenos e cognição", tipo="p", corpo=[], tabela=dict(
            cap="Adaptógenos, nootrópicos e cognitivos",
            linhas=[
                ["Item", "Faixa usual em estudos", "Para quê", "ECR/meta", "O que o número diz"],
                ["Ashwagandha (KSM-66)", "300–600 mg/dia do extrato padronizado", "Estresse, cortisol, sono, testosterona", "<strong>67</strong>",
                 "Base real para estresse e sono. Alertas nórdicos de hepatotoxicidade: evitar em doença hepática e tireoidopatia"],
                ["Rhodiola rosea", "200–600 mg/dia (3% rosavinas / 1% salidrosídeo)", "Fadiga mental, estresse", "<strong>70</strong>",
                 "Volume decente, estudos pequenos e padronização de extrato muito variável entre marcas"],
                ["Bacopa monnieri", "300 mg/dia (50% bacosídeos), por 8–12 semanas", "Memória e aprendizado", "<strong>14</strong>",
                 "Efeito modesto e só após semanas. Desconforto gastrointestinal é comum"],
                ["Panax ginseng", "200–400 mg/dia do extrato padronizado", "Fadiga, cognição", "<strong>400</strong>",
                 "Muito mais estudado do que se supõe. O problema é heterogeneidade, não escassez. Interage com anticoagulante e antidiabético"],
                ["Lion's Mane (Hericium erinaceus)", "500–3.000 mg/dia", "Cognição, fator de crescimento neural", "<strong>2</strong>",
                 "Dois. A base é quase toda pré-clínica — a fama não tem lastro humano"],
                ["Ginkgo biloba", "120–240 mg/dia (EGb 761)", "Circulação cerebral, memória", "<strong>88</strong>",
                 "Aqui o volume não salva: os grandes ensaios de prevenção de demência foram <strong>negativos</strong>. <strong>Aumenta risco de sangramento</strong>"],
                ["Piracetam", "1,2–4,8 g/dia", "Nootrópico racetam clássico", "<strong>371</strong>",
                 "Volume alto, mas concentrado em demência, AVC e declínio cognitivo — não em pessoa saudável. <strong>No Brasil é medicamento com prescrição</strong>"],
                ["Fosfatidilserina", "100–300 mg/dia", "Memória, cortisol pós-exercício", "<strong>19</strong>",
                 "A evidência antiga usava fonte bovina; os produtos atuais são de soja, com dados menos robustos"],
            ])),
        dict(h="Metabólicos e hepáticos", tipo="p", corpo=[], tabela=dict(
            cap="Glicemia, lipídios e fígado",
            linhas=[
                ["Item", "Faixa usual em estudos", "Para quê", "ECR/meta", "O que o número diz"],
                ["Berberina", "500 mg, 2–3×/dia, antes das refeições", "Glicemia, perfil lipídico", "<strong>177</strong>",
                 "Base sólida, com efeito comparável ao de fármacos em alguns ensaios. <strong>Inibe CYP3A4 e é interator sério</strong> — não combinar com estatina ou imunossupressor sem orientação"],
                ["Curcumina com piperina", "500–1.000 mg/dia de curcuminoides", "Inflamação, dor articular", "<strong>44</strong> (só em osteoartrite)",
                 "Boa base para osteoartrite. A piperina que aumenta a absorção também aumenta a de outros fármacos"],
                ["Silimarina (cardo mariano)", "200–400 mg/dia", "Proteção hepática", "<strong>33</strong>",
                 "Volume razoável, resultado inconsistente em hepatite. Vendida como detox, que não é desfecho clínico"],
                ["Bergamota (Citrus bergamia)", "500–1.000 mg/dia do extrato", "Colesterol", "não conferido",
                 "Estudos majoritariamente italianos e pequenos"],
                ["Canela (extrato)", "1–6 g/dia", "Glicemia", "<strong>23</strong>",
                 "O problema não é falta de ensaio, é resultado inconsistente entre eles. A canela cássia contém cumarina, hepatotóxica em dose alta; a Ceylon tem muito menos"],
                ["Ácido corosólico (banaba)", "10–50 mg/dia", "Glicemia", "não conferido",
                 "Poucos ensaios humanos, todos pequenos"],
            ])),
        dict(h="Testosterona, libido e o resto", tipo="p", corpo=[], tabela=dict(
            cap="Os de alegação hormonal",
            linhas=[
                ["Item", "Faixa usual em estudos", "Para quê", "ECR/meta", "O que o número diz"],
                ["Tongkat Ali (Eurycoma longifolia)", "200–400 mg/dia do extrato padronizado", "Testosterona, libido, estresse", "<strong>8</strong>",
                 "Pouco, mas existe. O efeito sobre testosterona aparece sobretudo em quem partia de nível baixo"],
                ["Fadogia agrestis", "não estabelecida em humanos", "Testosterona", "<strong>0</strong>",
                 "<strong>Zero ensaios randomizados e nenhum estudo humano.</strong> Conferi os três artigos que o PubMed marca como humanos: um é estudo em ratos, um é levantamento de mercado em Gana e o terceiro é triagem antimalárica in vitro. <strong>Sinal de toxicidade testicular e renal em roedores</strong>"],
                ["Shilajit", "250–500 mg/dia", "Testosterona, energia, ácido fúlvico", "<strong>7</strong>",
                 "Base mínima. Risco de contaminação por metal pesado no produto não purificado — exigir laudo"],
                ["Ioimbina HCl", "5–10 mg antes do treino ou em jejum", "Perda de gordura, disfunção erétil", "<strong>278</strong>",
                 "O volume engana: a maior parte usa ioimbina como sonda farmacológica em pesquisa psiquiátrica, não como emagrecedor. <strong>Ansiedade, taquicardia e picos de pressão.</strong> Não usar com IMAO nem com hipertensão"],
            ])),
        dict(h="O que muda quando se olha o número", tipo="li", corpo=[
            "<strong>Lion's Mane tem 2 ensaios.</strong> É o item com maior distância entre fama e lastro desta página.",
            "<strong>Ginkgo tem 88 e mesmo assim não se recomenda para prevenir demência</strong> — porque os grandes "
            "ensaios deram negativo. Volume de estudo não é sinônimo de evidência favorável.",
            "<strong>Ioimbina e piracetam têm centenas de ensaios</strong>, mas em contextos que não são os do rótulo. "
            "Contagem alta exige checar <em>de que</em> os estudos tratam.",
            "<strong>Fadogia agrestis tem zero.</strong> Foi popularizada por podcast, não por evidência.",
        ]),
    ],
    referencias=[
        ("Contagens de ensaios randomizados e metanálises obtidas no PubMed em 4 de setembro de 2026, com o filtro Randomized Controlled Trial[Publication Type] OR Meta-Analysis[Publication Type], item a item.",
         "https://pubmed.ncbi.nlm.nih.gov/"),
        ("Fadogia agrestis — os três artigos indexados como humanos: Ogunro & Yakubu 2022 (ratos Wistar), van Andel et al. 2012 (mercado herbal de Gana), Sanon et al. 2003 (triagem antimalárica in vitro).",
         "https://pubmed.ncbi.nlm.nih.gov/?term=Fadogia+agrestis"),
        ("Situação regulatória no Brasil: base da ANVISA.", "https://consultas.anvisa.gov.br/"),
    ],
),
}
