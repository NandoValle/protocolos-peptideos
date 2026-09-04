# -*- coding: utf-8 -*-
"""Meldonium — pagina montada de fonte primaria."""

from datas import DATA_APURACAO as _DT

MELDONIUM = {
"proprio_meldonium": dict(
    secoes=[
        dict(h="O que é", tipo="p", corpo=[
            "Meldonium — também mildronato, MET-88 ou quaterine — é o 3-(2,2,2-trimetil-hidrazínio)propionato. "
            "Foi desenvolvido no <strong>Instituto Letão de Síntese Orgânica</strong>, em Riga, e é vendido como "
            "fármaco cardioprotetor na Letônia, na Rússia e em países próximos.",
            "É o composto mais bem documentado de todo o bloco de medicamentos do leste europeu desta referência: "
            "357 artigos no PubMed, 35 marcados como ensaio clínico e <strong>7 ensaios registrados no "
            "ClinicalTrials.gov</strong> — contra zero da família de bioreguladores de Khavinson.",
        ]),
        dict(h="O mecanismo é o contrário do que parece", tipo="p", corpo=[
            "Muita gente supõe que um composto ligado à carnitina serve para <em>aumentar</em> carnitina. É o oposto. "
            "Segundo a revisão de Dambrova e colegas, o meldonium inibe a <strong>γ-butirobetaína hidroxilase</strong>, "
            "enzima da biossíntese da L-carnitina, e também o transportador OCTN2. O resultado é <strong>queda</strong> "
            "da L-carnitina.",
            "A lógica declarada do desenho é essa mesma: com menos carnitina, o tecido isquêmico deixa de acumular "
            "intermediários citotóxicos da beta-oxidação de ácidos graxos — um processo que consome muito oxigênio — "
            "e o metabolismo desloca-se para a glicose, que rende mais ATP por oxigênio gasto. Caem junto as "
            "acilcarnitinas de cadeia longa e o TMAO.",
            "No sistema nervoso central a explicação não fecha, porque o cérebro não usa ácido graxo como combustível. "
            "A revisão de Sjakste, Gutcaits e Kalvinsh — este último o inventor do composto — propõe um segundo "
            "mecanismo, independente de carnitina, via produção de óxido nítrico no endotélio vascular.",
        ]),
        dict(h="Quanta evidência existe", tipo="p", corpo=[
            f"Levantamento feito no PubMed e no ClinicalTrials.gov em {_DT}.",
        ], tabela=dict(
            cap="Levantamento de evidência",
            linhas=[
                ["Base", "Consulta", "Resultado"],
                ["PubMed", "<code>meldonium OR mildronate</code>", "357 artigos"],
                ["PubMed", "<code>(meldonium OR mildronate) AND (Clinical Trial[Publication Type] OR Randomized Controlled Trial[Publication Type])</code>", "35 artigos"],
                ["ClinicalTrials.gov", "intervenção contendo meldonium ou mildronate", "<strong>7 registros</strong>"],
            ])),
        dict(h="Os ensaios registrados", tipo="p", corpo=[
            "Estes são os sete. Repare que dois deles testam o meldonium <strong>combinado com o Mexidol</strong> "
            "(etilmetilhidroxipiridina succinato), sob a marca BRAINMAX — os dois compostos aparecem separados no "
            "mesmo catálogo de importação que originou esta lista.",
        ], tabela=dict(
            cap="Ensaios registrados no ClinicalTrials.gov",
            linhas=[
                ["Registro", "Fase", "Condição", "N", "Situação"],
                ["NCT01831011", "2", "AVC isquêmico agudo — mildronato vs. cinepazida", "227", "Concluído"],
                ["NCT01800357", "2", "AVC isquêmico agudo — contra placebo", "240", "Situação desconhecida"],
                ["NCT06648902", "1/2", "Carcinoma renal metastático com fadiga associada ao tratamento", "60", "Concluído em 2024"],
                ["NCT07304921", "1", "Metabolismo de ômega-3 — Riga Stradins, Letônia", "48", "Concluído"],
                ["NCT05689827", "4", "Astenia pós-covid — BRAINMAX, com Mexidol", "160", "Concluído"],
                ["NCT05939622", "4", "Astenia pós-covid com fMRI — BRAINMAX, com Mexidol", "30", "Concluído"],
                ["NCT07568574", "n/d", "Substâncias de performance sob supervisão médica em atletas de elite", "60", "Recrutando por convite"],
            ])),
        dict(h="O ponto que decide o uso: a janela de detecção", tipo="p", corpo=[
            "O meldonium entrou na lista de substâncias proibidas da <strong>WADA em 1º de janeiro de 2016</strong>, "
            "depois de um ano no Programa de Monitoramento de 2015. Nos primeiros meses de 2016, laboratórios "
            "antidoping relataram um número anormal de amostras com concentração alta.",
            "O que importa para quem faz exame antidoping não é a proibição em si, e sim <strong>quanto tempo a "
            "molécula continua detectável</strong>. Dois estudos independentes mediram isso, e o resultado é "
            "fora do comum:",
        ], tabela=dict(
            cap="Janela de detecção urinária medida",
            linhas=[
                ["Estudo", "Dose testada", "Janela de detecção", "Observação"],
                ["Görgens et al., 2017<br><small>German Sport University, Colônia</small>",
                 "500 mg, dose única (5 voluntários)", "<strong>até 65 dias</strong>",
                 "Acima do limite de quantificação de 10 ng/mL"],
                ["Görgens et al., 2017", "2 × 500 mg/dia por 6 dias (5 voluntários)",
                 "<strong>até 117 dias</strong>", "Excreção bifásica, não linear e dependente da dose"],
                ["Rabin et al., 2018<br><small>WADA + FMBA (Rússia)</small>",
                 "1,0 g ou 2,0 g/dia por 3 semanas (32 voluntários)",
                 "<strong>vários meses</strong>", "O estado de equilíbrio no sangue leva dias para ser atingido"],
            ])),
        dict(h="Leitura prática desses números", tipo="li", corpo=[
            "<strong>Seis dias de uso podem render quase quatro meses de detecção.</strong> Não existe janela de "
            "limpeza curta para esse composto — é a característica farmacocinética que definiu o caso todo.",
            "<strong>A excreção é bifásica e não linear.</strong> A concentração cai rápido no começo e depois se "
            "arrasta num platô longo. Concentração baixa no exame não prova uso antigo, e foi justamente essa "
            "ambiguidade que a WADA teve de administrar.",
            "<strong>Quem faz exame antidoping em qualquer esporte federado deve tratar o meldonium como "
            "indisponível</strong>, e não como algo a suspender com algumas semanas de antecedência.",
            "<strong>O estudo de 2018 foi coassinado pela própria WADA</strong> — Olivier Rabin é o diretor "
            "científico da agência — em parceria com a agência federal russa. É evidência de qualidade incomum "
            "para um composto desta origem.",
        ]),
        dict(h="Doses usadas em estudos humanos publicados", tipo="p", corpo=[
            "Isto <strong>não é recomendação de dose</strong>: é o registro do que foi administrado em estudos "
            "publicados, com a finalidade de cada um. Fora do contexto do estudo, esses números não se transferem.",
        ], tabela=dict(
            cap="O que foi administrado, e para quê",
            linhas=[
                ["Estudo", "Dose", "Duração", "Finalidade do estudo"],
                ["Görgens et al., 2017", "500 mg, oral, dose única", "1 dia", "Medir a janela de detecção"],
                ["Görgens et al., 2017", "2 × 500 mg/dia, oral", "6 dias", "Medir a janela de detecção com dose repetida"],
                ["Rabin et al., 2018", "1,0 g/dia ou 2,0 g/dia, oral", "3 semanas", "Farmacocinética de longo prazo em atletas saudáveis"],
                ["Nechaeva e Zheltikova, 2015", "não especificada no resumo", "12 semanas", "Período pós-infarto precoce, somado à terapia padrão"],
            ])),
        dict(h="O que o ensaio pós-infarto encontrou", tipo="p", corpo=[
            "Segundo o PubMed, o ensaio randomizado de Nechaeva e Zheltikova acompanhou 67 pacientes de 40 a 70 anos "
            "após infarto do miocárdio: 32 com terapia padrão para doença isquêmica e 35 com a mesma terapia mais "
            "mildronato por 12 semanas.",
            "O grupo com mildronato apresentou menos crises de angina (p = 0,001), menos extrassístoles (p = 0,002), "
            "menos distúrbios paroxísticos de ritmo (p = 0,001) e pressão arterial média mais baixa (p = 0,001). "
            "Os autores não registraram efeitos adversos no período.",
            "A ressalva: artigo russo, 67 participantes, 12 semanas de seguimento. É um sinal, não um desfecho duro "
            "de mortalidade ou reinfarto.",
        ]),
        dict(h="Status regulatório", tipo="li", corpo=[
            "<strong>Letônia, Rússia e países próximos:</strong> registrado como medicamento cardioprotetor, com décadas de uso.",
            "<strong>Brasil:</strong> sem registro na ANVISA.",
            "<strong>Estados Unidos e União Europeia:</strong> sem aprovação.",
            "<strong>WADA: proibido desde 1º de janeiro de 2016</strong>, em competição e fora dela.",
        ]),
        dict(h="O que esta página não responde", tipo="p", corpo=[
            "Não localizei, em fonte primária acessível, uma posologia consolidada em bula que eu pudesse reproduzir "
            "com segurança. A bula letã ou russa do Mildronate é a referência válida — e é dela, não daqui, que uma "
            "dose deve sair.",
            "Também não avaliei interações. Um composto que altera o metabolismo da carnitina e desloca o substrato "
            "energético do coração não é neutro em quem já usa fármaco cardiovascular. Isso é conversa com "
            "cardiologista, não com site.",
        ]),
    ],
    referencias=[
        ("Dambrova M et al. Pharmacological effects of meldonium: Biochemical mechanisms and biomarkers of cardiometabolic activity. Pharmacol Res. 2016;113(Pt B):771-780. doi:10.1016/j.phrs.2016.01.019",
         "https://doi.org/10.1016/j.phrs.2016.01.019"),
        ("Sjakste N, Gutcaits A, Kalvinsh I. Mildronate: an antiischemic drug for neurological indications. CNS Drug Rev. 2005;11(2):151-68. doi:10.1111/j.1527-3458.2005.tb00267.x",
         "https://doi.org/10.1111/j.1527-3458.2005.tb00267.x"),
        ("Gorgens C et al. The atypical excretion profile of meldonium: comparison of urinary detection windows after single- and multiple-dose application in healthy volunteers. J Pharm Biomed Anal. 2017;138:175-179. doi:10.1016/j.jpba.2017.02.011",
         "https://doi.org/10.1016/j.jpba.2017.02.011"),
        ("Rabin O et al. Meldonium long-term excretion period and pharmacokinetics in blood and urine of healthy athlete volunteers. Drug Test Anal. 2018;11(4):554-566. doi:10.1002/dta.2521",
         "https://doi.org/10.1002/dta.2521"),
        ("Nechaeva GI, Zheltikova EN. [Effects of Meldonium in Early Postmyocardial Infarction Period]. Kardiologiia. 2015;55(8):35-42. PMID 26761970",
         "https://pubmed.ncbi.nlm.nih.gov/26761970/"),
        ("Registros consultados no ClinicalTrials.gov: NCT01831011, NCT01800357, NCT06648902, NCT07304921, NCT05689827, NCT05939622, NCT07568574",
         "https://clinicaltrials.gov/search?intr=meldonium"),
    ],
),
}
