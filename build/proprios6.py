# -*- coding: utf-8 -*-
"""KLOW e Semax conferidos em fonte primaria.

Complementam as paginas de protocolo, que vem da fonte secundaria.
Consultas feitas no PubMed e no ClinicalTrials.gov em 04/09/2026.
"""

KLOW_SEMAX = {

# =============================================================== KLOW
"proprio_klow_evidencia": dict(
    secoes=[
        dict(h="Por que esta página existe", tipo="p", corpo=[
            "A <a href='stacks_klow-stack.html'>página de protocolo do KLOW</a> traz seis tabelas de dose, "
            "titulação e reconstituição, todas vindas da fonte secundária comercial. Esta aqui responde outra "
            "pergunta: <strong>o que sustenta aqueles números.</strong>",
            "E a resposta mudou em 2026. <strong>Os três principais componentes do KLOW entraram em ensaio clínico "
            "formal pela primeira vez</strong> — o que torna desatualizado dizer, como se dizia até agora, que a "
            "evidência é só pré-clínica.",
        ]),
        dict(h="A blend continua sem nenhum ensaio", tipo="p", corpo=[
            "Antes do resto, o ponto que não mudou: <strong>nenhum estudo jamais testou os quatro peptídeos "
            "juntos.</strong> A busca no ClinicalTrials.gov por KLOW não devolve nada, e não há publicação da "
            "combinação. Tudo que existe é sobre cada componente isolado.",
            "Isso importa porque a interação entre eles não é conhecida. O GHK-Cu carrega cobre; o KPV é "
            "anti-inflamatório; o BPC-157 e o TB-500 agem em reparo por vias diferentes. Somar quatro mecanismos "
            "num frasco é uma aposta de quem monta a blend, não um achado de pesquisa.",
        ]),
        dict(h="O que mudou: os componentes entraram em ensaio", tipo="p", corpo=[
            "Levantamento no ClinicalTrials.gov em 4 de setembro de 2026. Três destes ensaios têm o mesmo "
            "patrocinador, a Hudson Biotech, e todos começaram em fevereiro de 2026 — é um programa de "
            "desenvolvimento clínico coordenado, não estudos avulsos.",
        ], tabela=dict(
            cap="Ensaios registrados dos componentes",
            linhas=[
                ["Componente", "Registro", "Fase", "Condição", "N", "Patrocinador", "Situação"],
                ["<strong>BPC-157</strong>", "NCT07437547", "<strong>2</strong>",
                 "Estiramento de isquiotibiais grau II, confirmado por ressonância", "<strong>120</strong>",
                 "Hudson Biotech", "<strong>Recrutando</strong>"],
                ["<strong>BPC-157</strong>", "NCT07803250", "1", "Recuperação de reparo do manguito rotador", "30",
                 "Universidade do Arkansas", "Ainda não recrutando (jan/2027)"],
                ["<strong>BPC-157</strong>", "NCT02637284", "1", "Voluntários saudáveis, segurança e farmacocinética", "42",
                 "PharmaCotherapia", "Situação desconhecida (2015)"],
                ["<strong>TB-500</strong>", "NCT07487363", "<strong>1/2</strong>",
                 "Doença cardiovascular aterosclerótica estável, escalonamento de dose", "<strong>80</strong>",
                 "Hudson Biotech", "<strong>Recrutando</strong>"],
                ["<strong>GHK-Cu</strong>", "NCT07437586", "<strong>2</strong>",
                 "Gel tópico para reepitelização de ferida padronizada", "<strong>60</strong>",
                 "Hudson Biotech", "<strong>Recrutando</strong>"],
                ["<strong>GHK-Cu</strong>", "NCT07706361", "n/d", "Níveis sanguíneos de GHK com adesivo X39", "100",
                 "LifeWave", "Ainda não recrutando (2027)"],
                ["<strong>KPV</strong>", "—", "—", "<strong>Nenhum ensaio registrado</strong>", "—", "—", "—"],
                ["<strong>KLOW (a blend)</strong>", "—", "—", "<strong>Nenhum ensaio registrado</strong>", "—", "—", "—"],
            ])),
        dict(h="A literatura de cada componente", tipo="p", corpo=[
            "Contagens no PubMed na mesma data. Repare no contraste entre volume de artigo e ensaio clínico "
            "publicado — é o padrão de um composto muito estudado em bancada e pouco em gente.",
        ], tabela=dict(
            cap="PubMed, por componente",
            linhas=[
                ["Componente", "Artigos", "Ensaios clínicos publicados", "Leitura"],
                ["BPC-157", "<strong>271</strong>", "<strong>2</strong> (de 2002 e 2003)",
                 "Muito estudado em modelo animal, quase nada em humano até agora. Os dois ensaios publicados têm mais de vinte anos"],
                ["GHK-Cu", "<strong>180</strong>", "<strong>3</strong> (1992, 2006 e 2006)",
                 "É o mais antigo dos quatro e o de literatura mais madura. Mas os três ensaios são <strong>tópicos</strong> — pele, ferida e úlcera venosa. Nenhum injetável"],
                ["TB-500", "<strong>26</strong>", "<strong>9</strong> (8 reais)",
                 "Um dos nove é falso positivo: um estudo de <strong>tuberculose</strong>, que casou com a sigla TB. Os oito reais são todos da <strong>timosina beta-4 inteira</strong> — úlcera venosa, olho seco, cardiopatia isquêmica —, não do fragmento de sete aminoácidos que se vende como TB-500"],
                ["KPV", "<strong>9</strong> (em colite)", "2",
                 "Base mínima, concentrada em modelo de colite. É o componente que diferencia o KLOW da GLOW — e o de menor lastro"],
            ])),
        dict(h="O que isso muda na prática", tipo="li", corpo=[
            "<strong>Deixou de ser verdade que a evidência é só pré-clínica.</strong> Três ensaios de fase 1/2 e 2 "
            "estão recrutando agora. Em 2027 haverá dado humano controlado onde hoje há relato de comunidade.",
            "<strong>Mas nenhum deles testa a blend.</strong> Testam BPC-157 em lesão de isquiotibiais, TB-500 em "
            "doença cardiovascular e GHK-Cu em gel tópico — três indicações diferentes, por vias diferentes, "
            "isoladamente.",
            "<strong>O GHK-Cu do ensaio é tópico, não injetável.</strong> O protocolo de comunidade do KLOW é "
            "subcutâneo. Um ensaio de gel em ferida não valida uma injeção.",
            "<strong>O KPV segue sem nada.</strong> Justamente o componente que justifica escolher KLOW em vez de "
            "GLOW é o que tem menos base.",
            "<strong>Vale acompanhar.</strong> Os três ensaios da Hudson Biotech têm conclusão primária prevista "
            "para fevereiro de 2027. É a primeira vez que esses compostos terão desfecho controlado.",
        ]),
        dict(h="O que esta página não responde", tipo="p", corpo=[
            "Os quatro componentes estão com a contagem fechada, e fechá-la piorou a leitura do KLOW, não melhorou: os "
            "três ensaios de GHK-Cu são <strong>tópicos</strong> e os oito de TB-500 são da <strong>timosina "
            "beta-4 inteira</strong>. Nenhum dos onze testou o que o protocolo do KLOW manda injetar. "
            "Não li os protocolos completos dos ensaios em recrutamento: as doses que eles usam não estavam no "
            "registro resumido que consultei.",
            "As tabelas de dose do KLOW continuam na página de protocolo, e continuam vindo da fonte secundária. "
            "Nenhum número de lá foi validado por este levantamento.",
        ]),
    ],
    referencias=[
        ("NCT07437547 — Ensaio de fase 2, duplo-cego e controlado por placebo, do pentadecapeptídeo BPC 157 para reparo de estiramento agudo de isquiotibiais grau II confirmado por ressonância. Hudson Biotech, 120 participantes, recrutando.",
         "https://clinicaltrials.gov/study/NCT07437547"),
        ("NCT07487363 — Fase 1/2, randomizado, duplo-cego, placebo, escalonamento sequencial de dose de TB-500 em adultos com doença cardiovascular aterosclerótica estável. Hudson Biotech, 80 participantes, recrutando.",
         "https://clinicaltrials.gov/study/NCT07487363"),
        ("NCT07437586 — Fase 2, randomizado, duplo-cego, controlado por veículo, de gel tópico de GHK-Cu para reepitelização de feridas cutâneas padronizadas. Hudson Biotech, 60 participantes, recrutando.",
         "https://clinicaltrials.gov/study/NCT07437586"),
        ("NCT07803250 — Fase 1 do BPC-157 na recuperação de cirurgia de manguito rotador. Universidade do Arkansas, 30 participantes.",
         "https://clinicaltrials.gov/study/NCT07803250"),
        ("NCT02637284 — Fase 1 em voluntários saudáveis, segurança e farmacocinética do PCO-02 (BPC-157). PharmaCotherapia, 42 participantes.",
         "https://clinicaltrials.gov/study/NCT02637284"),
        ("Contagens do PubMed obtidas em 4 de setembro de 2026, uma consulta por componente.",
         "https://pubmed.ncbi.nlm.nih.gov/"),
    ],
),

# ============================================================== SEMAX
"proprio_semax_evidencia": dict(
    secoes=[
        dict(h="O achado que muda a leitura da dose", tipo="p", corpo=[
            "Este levantamento produziu a maior discrepância que encontrei em todo o site, e ela é sobre o Semax.",
            "A <a href='protocol_semax.html'>página de protocolo</a> traz as doses que circulam na comunidade: "
            "<strong>250 a 1.000 mcg por dia</strong>. Os ensaios clínicos russos publicados usaram "
            "<strong>6.000, 12.000 e 18.000 mcg por dia</strong> — de doze a setenta e duas vezes mais.",
            "As duas coisas não estão erradas: são <strong>contextos diferentes</strong>. A dose russa é "
            "hospitalar, para AVC isquêmico agudo, em curso curto. A dose de comunidade é para cognição, por "
            "tempo indeterminado. Mas quem lê só a página de protocolo não faz ideia de que a evidência clínica "
            "do Semax foi construída num regime completamente diferente daquele que se pratica.",
        ]),
        dict(h="Quanta evidência existe", tipo="p", corpo=[
            "PubMed e ClinicalTrials.gov, consultados em 4 de setembro de 2026.",
        ], tabela=dict(
            cap="Levantamento de evidência — Semax",
            linhas=[
                ["Base", "Consulta", "Resultado"],
                ["PubMed", "<code>Semax</code>", "232 artigos"],
                ["PubMed", "<code>Semax AND (Clinical Trial[Publication Type] OR Randomized Controlled Trial[Publication Type])</code>", "<strong>4 artigos</strong>"],
                ["ClinicalTrials.gov", "intervenção contendo Semax", "<strong>0 registros</strong>"],
            ])),
        dict(h="Os quatro ensaios, com as doses que usaram", tipo="p", corpo=[
            "Segundo o PubMed, é isto que existe de clínico sobre o Semax. Todos em russo, todos no mesmo par de "
            "periódicos, e três deles com Miasoedov ou Skvortsova entre os autores — o grupo que desenvolveu o "
            "composto.",
        ], tabela=dict(
            cap="Os quatro ensaios clínicos publicados",
            linhas=[
                ["Estudo", "N", "Contexto", "<strong>Dose usada</strong>", "O que encontrou"],
                ["Gusev et al., 2018<br><small>Zh Nevrol Psikhiatr 118(3 Pt 2):61-68</small>", "110",
                 "Reabilitação pós-AVC isquêmico, precoce vs. tardia",
                 "<strong>6.000 mcg/dia</strong>, 2 cursos de 10 dias com 20 dias de intervalo",
                 "Elevou o BDNF plasmático e acelerou a melhora no índice de Barthel, com o efeito somando-se ao da reabilitação precoce"],
                ["Serdiuk et al., 2007<br><small>Zh Nevrol Psikhiatr 107(4):29-39</small>", "27",
                 "Doença do neurônio motor",
                 "<strong>12.000 mcg/dia</strong> intranasal, 2 cursos de 10 dias",
                 "<strong>Não alterou o curso da denervação nem os desfechos clínicos.</strong> Melhorou apenas a qualidade de vida, por estado emocional e motivação, com pico no dia 10"],
                ["Gusev et al., 1997<br><small>Zh Nevrol Psikhiatr 97(6):26-34</small>", "30 (contra 80 controles)",
                 "AVC isquêmico hemisférico agudo",
                 "<strong>12.000 mcg/dia</strong> no AVC moderado e <strong>18.000 mcg/dia</strong> no grave, cursos de 5 e 10 dias",
                 "Acelerou a regressão do déficit neurológico, sobretudo motor, com acompanhamento por EEG e potenciais evocados"],
                ["Polunin et al., 2000<br><small>Vestn Oftalmol 116(1):15-8</small>", "n/d",
                 "Doenças do nervo óptico",
                 "não especificada no resumo",
                 "Melhora de acuidade visual, campo visual e visão de cores, em três grupos por via de administração"],
            ])),
        dict(h="Leitura honesta desses quatro", tipo="li", corpo=[
            "<strong>Zero ensaios registrados.</strong> Nenhum estudo de Semax foi registrado no ClinicalTrials.gov. "
            "Os quatro artigos são publicações, não protocolos pré-registrados.",
            "<strong>Nenhum é em pessoa saudável.</strong> Todos os quatro são em doença — AVC, neurônio motor, "
            "nervo óptico. <strong>A base clínica do Semax não diz nada sobre cognição em quem está bem</strong>, "
            "que é o uso mais comum fora da Rússia.",
            "<strong>Um deles é francamente negativo.</strong> Em doença do neurônio motor, o Semax não mudou a "
            "denervação nem os desfechos clínicos — melhorou só a percepção de qualidade de vida. Esse resultado "
            "raramente aparece em texto de vendedor.",
            "<strong>Os autores são o grupo que criou o composto.</strong> Miasoedov e Skvortsova aparecem em três "
            "dos quatro. Vale a mesma ressalva do Thymalin.",
            "<strong>O mais recente é de 2018</strong>, e o mais antigo de 1997. Não há programa clínico ativo.",
        ]),
        dict(h="O que fazer com a diferença de dose", tipo="p", corpo=[
            "Não estou recomendando subir a dose para o patamar russo. A dose alta foi usada em ambiente hospitalar, "
            "por poucos dias, em quem tinha acabado de ter um AVC — situação em que a relação entre risco e "
            "benefício é outra.",
            "O que registro é mais simples e mais incômodo: <strong>a faixa de comunidade não foi testada em "
            "nenhum ensaio.</strong> Ela não é uma versão reduzida e prudente da dose clínica; é um número que "
            "surgiu na prática e nunca passou por estudo. Quem usa 300 mcg para foco está fora de qualquer "
            "protocolo publicado — para mais ou para menos, ninguém sabe.",
        ]),
    ],
    referencias=[
        ("Gusev EI et al. [The efficacy of semax in the treatment of patients at different stages of ischemic stroke]. Zh Nevrol Psikhiatr Im S S Korsakova. 2018;118(3. Vyp. 2):61-68. doi:10.17116/jnevro20181183261-68",
         "https://doi.org/10.17116/jnevro20181183261-68"),
        ("Serdiuk AV, Levitskii GN, Miasoedov NF, Skvortsova VI. [The study of chronic partial denervation and quality of life in patients with motor neuron disease treated with semax]. Zh Nevrol Psikhiatr Im S S Korsakova. 2007;107(4):29-39. PMID 18379501",
         "https://pubmed.ncbi.nlm.nih.gov/18379501/"),
        ("Gusev EI, Skvortsova VI, Miasoedov NF et al. [Effectiveness of semax in acute period of hemispheric ischemic stroke]. Zh Nevrol Psikhiatr Im S S Korsakova. 1997;97(6):26-34. PMID 11517472",
         "https://pubmed.ncbi.nlm.nih.gov/11517472/"),
        ("Polunin GS et al. [Evaluation of therapeutic effect of new Russian drug semax in optic nerve disease]. Vestn Oftalmol. 2000;116(1):15-8. PMID 10741256",
         "https://pubmed.ncbi.nlm.nih.gov/10741256/"),
        ("Busca por intervenção contendo Semax no ClinicalTrials.gov em 4 de setembro de 2026: nenhum registro.",
         "https://clinicaltrials.gov/search?intr=Semax"),
    ],
),
}
