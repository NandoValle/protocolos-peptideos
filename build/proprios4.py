# -*- coding: utf-8 -*-
"""Secao de suplementos de venda livre, com dose."""

SUPS = {
"proprio_suplementos": dict(
    secoes=[
        dict(h="O que esta página é", tipo="p", corpo=[
            "Quarenta e cinco itens de venda livre, com a faixa de dose usada em estudos e no rótulo padronizado. "
            "Diferente do resto do site, aqui <strong>a maioria tem risco baixo e evidência decente</strong> — e é "
            "por isso que a dose aparece.",
            "A coluna <strong>Evidência</strong> continua sendo a mais importante. <em>Boa</em> significa ensaios "
            "randomizados replicados com desfecho relevante. <em>Razoável</em>, evidência real mas limitada. "
            "<em>Fraca</em>, estudo pequeno, inconsistente ou de desfecho substituto.",
        ]),
        dict(h="Aviso específico de dois itens", tipo="li", corpo=[
            "<strong>Melatonina:</strong> a ANVISA autoriza como suplemento alimentar apenas até <strong>0,21 mg "
            "por dia</strong> para adultos. As apresentações de 0,5 mg e 3 mg estão acima desse limite e, no "
            "Brasil, não se enquadram como suplemento de venda livre.",
            "<strong>Ferro:</strong> só faz sentido com deficiência comprovada em exame. Suplementar ferro sem "
            "deficiência é acumular um metal pró-oxidante sem ganho nenhum, e pode mascarar a investigação de uma "
            "causa de anemia.",
        ]),
        dict(h="Vitaminas e minerais", tipo="p", corpo=[], tabela=dict(
            cap="Vitaminas e minerais",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "Evidência", "Ressalva"],
                ["Vitamina D3", "1.000–4.000 UI/dia", "Deficiência, saúde óssea, imunidade", "Boa para deficiência",
                 "4.000 UI/dia é o limite superior tolerável do IOM. A apresentação de 5.000 UI passa dele — dosar 25-OH-vitamina D antes"],
                ["Vitamina D3 + K2", "D3 conforme acima + K2 (MK-7) 90–200 mcg", "Direcionamento do cálcio para o osso", "Razoável",
                 "<strong>K2 interage com varfarina.</strong> Quem anticoagula com cumarínico não usa sem orientação"],
                ["Vitamina C", "500–1.000 mg/dia", "Antioxidante, colágeno, absorção de ferro", "Boa como nutriente",
                 "Acima de 2 g/dia: diarreia osmótica e risco de cálculo de oxalato"],
                ["Vitamina B12 (metilcobalamina)", "500–1.000 mcg/dia", "Deficiência, sobretudo em vegetariano e em quem usa metformina", "Boa",
                 "Praticamente sem toxicidade. Dosar antes evita suplementar o que não falta"],
                ["Complexo B", "conforme rótulo", "Cobertura ampla do grupo B", "Razoável só em deficiência",
                 "B6 acima de 100 mg/dia por tempo longo causa neuropatia periférica — é o risco esquecido do complexo B"],
                ["Magnésio glicinato", "200–400 mg de magnésio elementar/dia", "Sono, cãibra, ansiedade, pressão", "Razoável a boa",
                 "A forma glicinato é a mais bem tolerada. Reduzir dose em doença renal"],
                ["Magnésio L-treonato", "1,5–2 g/dia do composto (~144 mg de Mg elementar)", "Alegação de foco cognitivo", "Fraca em humanos",
                 "A alegação de atravessar melhor a barreira hematoencefálica vem de estudo animal. Custa várias vezes mais que o glicinato"],
                ["Zinco + cobre", "15–30 mg de zinco + 1–2 mg de cobre", "Imunidade, testosterona, pele", "Boa em deficiência",
                 "Zinco isolado e prolongado <strong>causa deficiência de cobre</strong> — por isso vêm juntos. Limite superior do zinco: 40 mg/dia"],
                ["Selênio", "100–200 mcg/dia", "Tireoide, antioxidante", "Razoável",
                 "Janela estreita. Limite superior 400 mcg/dia; acima disso há selenose"],
                ["Iodo", "150 mcg/dia (RDA do adulto)", "Função tireoidiana", "Boa como nutriente",
                 "Excesso pode <strong>desencadear</strong> disfunção tireoidiana em quem tem tireoidite. Não é item para dose alta por conta própria"],
                ["Ferro bisglicinato", "25–50 mg/dia", "Anemia ferropriva", "Boa quando há deficiência",
                 "<strong>Só com ferritina baixa comprovada.</strong> A forma bisglicinato causa menos constipação que o sulfato"],
                ["Boro", "3–10 mg/dia", "Testosterona livre, metabolismo ósseo", "Fraca",
                 "Estudos pequenos. Limite superior 20 mg/dia"],
            ])),
        dict(h="Desempenho e músculo", tipo="p", corpo=[], tabela=dict(
            cap="Treino, força e recuperação",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "Evidência", "Ressalva"],
                ["Creatina monoidratada", "3–5 g/dia. Saturação opcional: 20 g/dia divididos, por 5–7 dias", "Força, potência, massa magra, cognição",
                 "<strong>Boa — é o suplemento esportivo mais bem estudado que existe</strong>",
                 "Eleva a creatinina sérica sem lesão renal: avise quem for ler seu exame. Não precisa de ciclo nem de pausa"],
                ["L-glutamina", "5–10 g/dia", "Recuperação, barreira intestinal", "Fraca em pessoa saudável",
                 "A evidência boa é em paciente crítico e queimado, não em quem treina"],
                ["Acetil-L-carnitina (ALCAR)", "500–2.000 mg/dia", "Cognição, neuropatia, fadiga", "Razoável para neuropatia diabética",
                 "Aumenta TMAO, marcador ligado a risco cardiovascular. Peso incerto, mas vale saber"],
                ["Colágeno hidrolisado + vitamina C", "10 g/dia, com vitamina C, 30–60 min antes do treino", "Tendão, ligamento, pele",
                 "Razoável", "O momento da tomada importa aqui, diferente da maioria"],
                ["Colágeno tipo II (UC-II)", "40 mg/dia", "Osteoartrite de joelho", "Razoável",
                 "É outro mecanismo: tolerância oral, não matéria-prima. Não confundir com o hidrolisado, nem somar as doses"],
                ["Glucosamina + condroitina", "1.500 mg + 1.200 mg/dia", "Osteoartrite", "Fraca a razoável, resultado inconsistente",
                 "Glucosamina costuma vir de crustáceo — atenção a alergia"],
                ["MSM (metilsulfonilmetano)", "1,5–3 g/dia", "Dor articular, inflamação", "Fraca",
                 "Bem tolerado. Efeito modesto quando aparece"],
            ])),
        dict(h="Sono, humor e cognição", tipo="p", corpo=[], tabela=dict(
            cap="Sistema nervoso",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "Evidência", "Ressalva"],
                ["Melatonina", "0,5–3 mg, 30–60 min antes de dormir", "Latência do sono, ajuste de fuso", "Boa para fuso e atraso de fase",
                 "<strong>ANVISA limita a 0,21 mg/dia como suplemento.</strong> Dose menor costuma funcionar melhor que dose alta"],
                ["Glicina", "3 g antes de dormir", "Qualidade do sono, temperatura corporal", "Razoável",
                 "Estudos pequenos, mas consistentes e de risco baixo"],
                ["L-teanina", "100–400 mg/dia", "Calma sem sedação; combina com cafeína", "Razoável",
                 "Bem tolerada. Combinação com cafeína é a que tem mais dado"],
                ["Citicolina (CDP-colina)", "250–500 mg/dia", "Atenção, memória", "Razoável",
                 "Melhor evidência que a maioria dos nootrópicos de venda livre"],
                ["Alpha-GPC", "300–600 mg/dia", "Colina para acetilcolina, força", "Fraca a razoável",
                 "Um estudo observacional levantou associação com AVC, ainda não confirmada. Vale acompanhar"],
                ["GABA", "100–750 mg/dia", "Ansiedade, sono", "<strong>Fraca — o GABA oral atravessa mal a barreira hematoencefálica</strong>",
                 "Se há efeito, o mecanismo provavelmente não é o que o rótulo diz"],
                ["Inositol (mio-inositol)", "2–4 g/dia; 4 g nos estudos de SOP", "SOP, ansiedade, sensibilidade à insulina", "Boa para SOP",
                 "Uma das melhores relações entre evidência e risco desta página"],
                ["Lecitina de soja", "1–2 g/dia", "Fonte de colina e fosfolipídio", "Fraca",
                 "Fonte barata de colina; efeito próprio pouco demonstrado"],
            ])),
        dict(h="Longevidade e metabolismo", tipo="p", corpo=[], tabela=dict(
            cap="Mitocôndria, senescência e metabólico",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "Evidência", "Ressalva"],
                ["Coenzima Q10", "100–300 mg/dia, com refeição gordurosa", "Mitocôndria, miopatia por estatina", "Razoável",
                 "Absorção depende de gordura junto. Pode reduzir efeito da varfarina"],
                ["Ubiquinol (CoQ10 reduzido)", "100–200 mg/dia", "Mesma finalidade, forma reduzida", "Razoável",
                 "Melhor absorção alegada, sobretudo acima dos 40 anos. Custa mais"],
                ["Ácido alfa-lipóico (ALA)", "300–600 mg/dia", "Neuropatia diabética, sensibilidade à insulina", "Boa para neuropatia diabética",
                 "A forma R é a biologicamente ativa. Pode baixar glicemia — atenção em quem usa antidiabético"],
                ["NAC (N-acetilcisteína)", "600–1.800 mg/dia", "Glutationa, muco, comportamento compulsivo", "Boa em intoxicação por paracetamol; razoável no resto",
                 "<strong>É o precursor que funciona</strong>, enquanto a glutationa oral é mal absorvida. Em alguns países é medicamento"],
                ["Quercetina", "500–1.000 mg/dia", "Antioxidante, senolítico em pesquisa", "Fraca em humanos",
                 "Biodisponibilidade oral baixa. Inibe CYP3A4 — atenção a interações"],
                ["Resveratrol", "150–500 mg/dia", "Sirtuínas, metabolismo", "Fraca — resultados humanos decepcionaram",
                 "Biodisponibilidade oral muito baixa. A promessa não se confirmou em ensaio"],
                ["Fisetina", "dose senolítica não estabelecida em humanos", "Senolítico", "<strong>Muito fraca — ensaios humanos em andamento</strong>",
                 "Os protocolos de pulso alto que circulam vêm de estudo animal, não de dose humana validada"],
                ["Espermidina", "1–6 mg/dia", "Autofagia, longevidade", "Fraca em humanos",
                 "Base sobretudo epidemiológica e pré-clínica"],
                ["NMN", "250–500 mg/dia", "Precursor de NAD+", "Fraca a razoável — eleva NAD+, desfecho clínico não demonstrado",
                 "<strong>A FDA retirou o NMN da categoria de suplemento nos EUA em 2022.</strong> Situação regulatória instável"],
                ["Astaxantina", "4–12 mg/dia", "Antioxidante, pele, olho", "Fraca a razoável",
                 "Carotenoide lipossolúvel: tomar com gordura"],
            ])),
        dict(h="Intestino e fígado", tipo="p", corpo=[], tabela=dict(
            cap="Trato digestivo e hepático",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "Evidência", "Ressalva"],
                ["Ômega-3 (EPA + DHA)", "1–3 g/dia de EPA + DHA somados", "Triglicerídeos, inflamação, cardiovascular", "Boa para triglicerídeos",
                 "Ler o rótulo pelo teor de EPA+DHA, não pelo peso da cápsula. Doses altas aumentam tempo de sangramento"],
                ["Probiótico multicepas", "1–50 bilhões de UFC/dia", "Microbiota, digestão", "Razoável, mas cepa-específica",
                 "Efeito não se transfere entre cepas. <strong>Cautela em imunossuprimido</strong>"],
                ["Psyllium", "5–10 g/dia, com bastante água", "Fibra, constipação, colesterol", "Boa",
                 "Sem água suficiente, causa obstrução. Afasta de outros medicamentos em 2 h"],
                ["Butirato de sódio", "300–600 mg/dia", "Barreira intestinal, colonócito", "Fraca em humanos",
                 "O butirato produzido pela fibra fermentada provavelmente rende mais que a cápsula"],
                ["TUDCA", "250–1.500 mg/dia", "Fígado, colestase, estresse de retículo", "Razoável em colestase",
                 "A evidência boa é hepatológica, não a de proteção hepática em ciclo de anabolizante"],
                ["Colesevelam natural", "conforme rótulo", "Alegação de sequestro de ácido biliar", "<strong>Muito fraca</strong>",
                 "<strong>Nome confuso:</strong> colesevelam de verdade é fármaco de prescrição. O produto de venda livre com esse nome é outra coisa — conferir a composição real antes"],
            ])),
        dict(h="Como usar esta tabela", tipo="li", corpo=[
            "<strong>Dose de suplemento também tem teto.</strong> Selênio, zinco, iodo, B6 e vitamina D têm limite "
            "superior tolerável definido, e ultrapassar não traz benefício extra — traz risco.",
            "<strong>Dosar antes vale mais que suplementar.</strong> Vitamina D, B12, ferro e iodo são os quatro em "
            "que um exame simples troca palpite por decisão.",
            "<strong>Interação existe em suplemento.</strong> Ginkgo e ômega-3 com anticoagulante, K2 com varfarina, "
            "berberina e quercetina com quem depende de CYP3A4, ALA com antidiabético.",
            "<strong>Nada aqui substitui dieta, sono e treino.</strong> É a frase mais batida do assunto e continua "
            "sendo a mais verdadeira.",
        ]),
    ],
    referencias=[
        ("As faixas de dose desta página vêm de ensaios publicados e de rótulos padronizados, e não foram conferidas artigo por artigo nesta compilação — diferente das páginas de Thymalin, bioreguladores e Meldonium, onde cada número tem a consulta declarada.", "https://pubmed.ncbi.nlm.nih.gov/"),
        ("Limites superiores toleráveis de vitaminas e minerais: Dietary Reference Intakes, National Academies.", "https://www.nationalacademies.org/our-work/summary-report-of-the-dietary-reference-intakes"),
        ("Situação regulatória de suplementos no Brasil, incluindo o limite da melatonina: ANVISA.", "https://www.gov.br/anvisa/pt-br/assuntos/alimentos/suplementos-alimentares"),
    ],
),
}
