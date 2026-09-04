# -*- coding: utf-8 -*-
"""Secao de suplementos de venda livre, com dose e contagem de evidencia.

A coluna "ECR/meta" foi conferida no PubMed em 04/09/2026, item a item,
com o filtro Randomized Controlled Trial OR Meta-Analysis.
"""

SUPS = {
"proprio_suplementos": dict(
    secoes=[
        dict(h="Como ler esta página", tipo="p", corpo=[
            "Quarenta e cinco itens de venda livre, com a faixa de dose usada em estudos e no rótulo padronizado. "
            "Diferente do resto do site, aqui <strong>a maioria tem risco baixo e evidência real</strong> — e é por "
            "isso que a dose aparece.",
            "A coluna <strong>ECR/meta</strong> traz o número de ensaios randomizados e metanálises indexados no "
            "PubMed, <strong>conferido item a item em 4 de setembro de 2026</strong>. Onde está escrito "
            "<em>não conferido</em>, é porque não fiz a consulta daquele item — e prefiro dizer isso a inventar "
            "um número.",
            "Ler o número com cuidado: contagem alta significa que muita gente estudou, não que o resultado foi "
            "favorável. O ginkgo, na página de fitoterápicos, é o exemplo caricato disso.",
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
                ["Item", "Faixa usual", "Para quê", "ECR/meta", "Ressalva"],
                ["Vitamina D3", "1.000–4.000 UI/dia", "Deficiência, saúde óssea, imunidade", "<strong>3.625</strong>",
                 "4.000 UI/dia é o limite superior tolerável do IOM. A apresentação de 5.000 UI passa dele — dosar 25-OH-vitamina D antes"],
                ["Vitamina D3 + K2", "D3 conforme acima + K2 (MK-7) 90–200 mcg", "Direcionamento do cálcio para o osso", "não conferido",
                 "<strong>K2 interage com varfarina.</strong> Quem anticoagula com cumarínico não usa sem orientação"],
                ["Vitamina C", "500–1.000 mg/dia", "Antioxidante, colágeno, absorção de ferro", "não conferido",
                 "Acima de 2 g/dia: diarreia osmótica e risco de cálculo de oxalato"],
                ["Vitamina B12 (metilcobalamina)", "500–1.000 mcg/dia", "Deficiência, sobretudo em vegetariano e em quem usa metformina", "não conferido",
                 "Praticamente sem toxicidade. Dosar antes evita suplementar o que não falta"],
                ["Complexo B", "conforme rótulo", "Cobertura ampla do grupo B", "não conferido",
                 "B6 acima de 100 mg/dia por tempo longo causa neuropatia periférica — é o risco esquecido do complexo B"],
                ["Magnésio glicinato", "200–400 mg de magnésio elementar/dia", "Sono, cãibra, ansiedade, pressão", "<strong>563</strong>",
                 "Base sólida. A forma glicinato é a mais bem tolerada. Reduzir dose em doença renal"],
                ["Magnésio L-treonato", "1,5–2 g/dia do composto (~144 mg de Mg elementar)", "Alegação de foco cognitivo", "não conferido",
                 "A alegação de atravessar melhor a barreira hematoencefálica vem de estudo animal. Custa várias vezes mais que o glicinato"],
                ["Zinco + cobre", "15–30 mg de zinco + 1–2 mg de cobre", "Imunidade, testosterona, pele", "<strong>1.363</strong>",
                 "Base ampla. Zinco isolado e prolongado <strong>causa deficiência de cobre</strong> — por isso vêm juntos. Limite superior do zinco: 40 mg/dia"],
                ["Selênio", "100–200 mcg/dia", "Tireoide, antioxidante", "não conferido",
                 "Janela estreita. Limite superior 400 mcg/dia; acima disso há selenose"],
                ["Iodo", "150 mcg/dia (RDA do adulto)", "Função tireoidiana", "não conferido",
                 "Excesso pode <strong>desencadear</strong> disfunção tireoidiana em quem tem tireoidite. Não é item para dose alta por conta própria"],
                ["Ferro bisglicinato", "25–50 mg/dia", "Anemia ferropriva", "não conferido",
                 "<strong>Só com ferritina baixa comprovada.</strong> A forma bisglicinato causa menos constipação que o sulfato"],
                ["Boro", "3–10 mg/dia", "Testosterona livre, metabolismo ósseo", "não conferido",
                 "Estudos pequenos. Limite superior 20 mg/dia"],
            ])),
        dict(h="Desempenho e músculo", tipo="p", corpo=[], tabela=dict(
            cap="Treino, força e recuperação",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "ECR/meta", "Ressalva"],
                ["Creatina monoidratada", "3–5 g/dia. Saturação opcional: 20 g/dia divididos, por 5–7 dias", "Força, potência, massa magra, cognição", "<strong>878</strong>",
                 "<strong>É o suplemento esportivo mais bem estudado que existe.</strong> Eleva a creatinina sérica sem lesão renal: avise quem for ler seu exame. Não precisa de ciclo nem de pausa"],
                ["L-glutamina", "5–10 g/dia", "Recuperação, barreira intestinal", "não conferido",
                 "A evidência boa é em paciente crítico e queimado, não em quem treina"],
                ["Acetil-L-carnitina (ALCAR)", "500–2.000 mg/dia", "Cognição, neuropatia, fadiga", "<strong>173</strong>",
                 "Base real, sobretudo em neuropatia diabética. Aumenta TMAO, marcador ligado a risco cardiovascular"],
                ["Colágeno hidrolisado + vitamina C", "10 g/dia, com vitamina C, 30–60 min antes do treino", "Tendão, ligamento, pele", "<strong>234</strong>",
                 "Volume alto. O momento da tomada importa aqui, diferente da maioria"],
                ["Colágeno tipo II (UC-II)", "40 mg/dia", "Osteoartrite de joelho", "não conferido",
                 "É outro mecanismo: tolerância oral, não matéria-prima. Não confundir com o hidrolisado, nem somar as doses"],
                ["Glucosamina + condroitina", "1.500 mg + 1.200 mg/dia", "Osteoartrite", "<strong>98</strong>",
                 "Muito estudado e ainda assim inconsistente — é o caso em que o volume não resolveu a dúvida. Glucosamina costuma vir de crustáceo: atenção a alergia"],
                ["MSM (metilsulfonilmetano)", "1,5–3 g/dia", "Dor articular, inflamação", "<strong>23</strong>",
                 "Base modesta. Bem tolerado, efeito pequeno quando aparece"],
            ])),
        dict(h="Sono, humor e cognição", tipo="p", corpo=[], tabela=dict(
            cap="Sistema nervoso",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "ECR/meta", "Ressalva"],
                ["Melatonina", "0,5–3 mg, 30–60 min antes de dormir", "Latência do sono, ajuste de fuso", "<strong>773</strong>",
                 "Base ampla, melhor para fuso e atraso de fase. <strong>ANVISA limita a 0,21 mg/dia como suplemento.</strong> Dose menor costuma funcionar melhor que dose alta"],
                ["Glicina", "3 g antes de dormir", "Qualidade do sono, temperatura corporal", "<strong>5</strong>",
                 "Só cinco. Os estudos são consistentes e de risco baixo, mas a base é fina — menor do que a fama sugere"],
                ["L-teanina", "100–400 mg/dia", "Calma sem sedação; combina com cafeína", "<strong>84</strong>",
                 "Base decente. A combinação com cafeína é a que tem mais dado"],
                ["Citicolina (CDP-colina)", "250–500 mg/dia", "Atenção, memória", "<strong>44</strong>",
                 "Melhor lastro que a maioria dos nootrópicos de venda livre"],
                ["Alpha-GPC", "300–600 mg/dia", "Colina para acetilcolina, força", "<strong>4</strong>",
                 "Quatro ensaios. Um estudo observacional levantou associação com AVC, ainda não confirmada"],
                ["GABA", "100–750 mg/dia", "Ansiedade, sono", "<strong>11</strong>",
                 "<strong>O GABA oral atravessa mal a barreira hematoencefálica.</strong> Se há efeito, o mecanismo provavelmente não é o que o rótulo diz"],
                ["Inositol (mio-inositol)", "2–4 g/dia; 4 g nos estudos de SOP", "SOP, ansiedade, sensibilidade à insulina", "<strong>87</strong> (só em SOP)",
                 "Uma das melhores relações entre evidência e risco desta página"],
                ["Lecitina de soja", "1–2 g/dia", "Fonte de colina e fosfolipídio", "não conferido",
                 "Fonte barata de colina; efeito próprio pouco demonstrado"],
            ])),
        dict(h="Longevidade e metabolismo", tipo="p", corpo=[], tabela=dict(
            cap="Mitocôndria, senescência e metabólico",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "ECR/meta", "Ressalva"],
                ["Coenzima Q10", "100–300 mg/dia, com refeição gordurosa", "Mitocôndria, miopatia por estatina", "<strong>657</strong>",
                 "Base ampla. Absorção depende de gordura junto. Pode reduzir efeito da varfarina"],
                ["Ubiquinol (CoQ10 reduzido)", "100–200 mg/dia", "Mesma finalidade, forma reduzida", "incluído na contagem da CoQ10",
                 "Melhor absorção alegada, sobretudo acima dos 40 anos. Custa mais"],
                ["Ácido alfa-lipóico (ALA)", "300–600 mg/dia", "Neuropatia diabética, sensibilidade à insulina", "<strong>65</strong> (só em neuropatia diabética)",
                 "Base boa na indicação. A forma R é a ativa. Pode baixar glicemia — atenção em quem usa antidiabético"],
                ["NAC (N-acetilcisteína)", "600–1.800 mg/dia", "Glutationa, muco, comportamento compulsivo", "<strong>1.183</strong>",
                 "<strong>É o precursor que funciona</strong>, enquanto a glutationa oral é mal absorvida. Em alguns países é medicamento"],
                ["Quercetina", "500–1.000 mg/dia", "Antioxidante, senolítico em pesquisa", "<strong>355</strong>",
                 "Volume alto, resultados clínicos modestos. Biodisponibilidade oral baixa. Inibe CYP3A4"],
                ["Resveratrol", "150–500 mg/dia", "Sirtuínas, metabolismo", "<strong>391</strong>",
                 "Quase 400 ensaios e a promessa não se confirmou — é o caso mais claro de volume sem resultado. Biodisponibilidade oral muito baixa"],
                ["Fisetina", "dose senolítica não estabelecida em humanos", "Senolítico", "<strong>2</strong>",
                 "Dois ensaios humanos publicados. Os protocolos de pulso alto que circulam vêm de estudo animal"],
                ["Espermidina", "1–6 mg/dia", "Autofagia, longevidade", "<strong>9</strong>",
                 "Base sobretudo epidemiológica e pré-clínica"],
                ["NMN", "250–500 mg/dia", "Precursor de NAD+", "<strong>21</strong>",
                 "Eleva NAD+; desfecho clínico não demonstrado. <strong>A FDA retirou o NMN da categoria de suplemento nos EUA em 2022</strong>"],
                ["Astaxantina", "4–12 mg/dia", "Antioxidante, pele, olho", "<strong>106</strong>",
                 "Base melhor do que a fama de nicho sugere. Carotenoide lipossolúvel: tomar com gordura"],
            ])),
        dict(h="Intestino e fígado", tipo="p", corpo=[], tabela=dict(
            cap="Trato digestivo e hepático",
            linhas=[
                ["Item", "Faixa usual", "Para quê", "ECR/meta", "Ressalva"],
                ["Ômega-3 (EPA + DHA)", "1–3 g/dia de EPA + DHA somados", "Triglicerídeos, inflamação, cardiovascular", "<strong>2.597</strong>",
                 "Base enorme, mais forte para triglicerídeos. Ler o rótulo pelo teor de EPA+DHA, não pelo peso da cápsula. Dose alta aumenta tempo de sangramento"],
                ["Probiótico multicepas", "1–50 bilhões de UFC/dia", "Microbiota, digestão", "<strong>5.248</strong>",
                 "O maior número desta página — e o mais enganoso: <strong>o efeito é cepa-específica e não se transfere</strong>. <strong>Cautela em imunossuprimido</strong>"],
                ["Psyllium", "5–10 g/dia, com bastante água", "Fibra, constipação, colesterol", "<strong>216</strong>",
                 "Base sólida. Sem água suficiente, causa obstrução. Afastar de outros medicamentos em 2 h"],
                ["Butirato de sódio", "300–600 mg/dia", "Barreira intestinal, colonócito", "<strong>5</strong>",
                 "Base fina. O butirato produzido pela fibra fermentada provavelmente rende mais que a cápsula"],
                ["TUDCA", "250–1.500 mg/dia", "Fígado, colestase, estresse de retículo", "<strong>24</strong>",
                 "A evidência é hepatológica, não a de proteção hepática em ciclo de anabolizante"],
                ["Colesevelam natural", "conforme rótulo", "Alegação de sequestro de ácido biliar", "não conferido",
                 "<strong>Nome confuso:</strong> colesevelam de verdade é fármaco de prescrição. O produto de venda livre com esse nome é outra coisa — conferir a composição real antes"],
            ])),
        dict(h="O que a contagem revelou", tipo="li", corpo=[
            "<strong>Resveratrol tem 391 ensaios e ainda assim decepcionou.</strong> É a prova de que volume de "
            "pesquisa não é sinônimo de resultado — e por isso a coluna traz o número, não um selo de aprovação.",
            "<strong>Probiótico tem 5.248, o maior da página, e é o mais enganoso</strong>, porque o efeito é de "
            "cepa específica: os milhares de ensaios não somam a favor do frasco que você comprou.",
            "<strong>Glicina, alpha-GPC, butirato e fisetina têm entre 2 e 5 ensaios cada.</strong> São os quatro de "
            "base mais fina desta página.",
            "<strong>Nove itens estão marcados como não conferidos.</strong> Preferi deixar o buraco visível a "
            "preenchê-lo com estimativa.",
            "<strong>Dose de suplemento também tem teto.</strong> Selênio, zinco, iodo, B6 e vitamina D têm limite "
            "superior tolerável definido; passar dele não traz benefício extra.",
        ]),
    ],
    referencias=[
        ("Contagens obtidas no PubMed em 4 de setembro de 2026, com o filtro Randomized Controlled Trial[Publication Type] OR Meta-Analysis[Publication Type], uma consulta por item. Itens marcados como não conferidos não tiveram consulta feita.",
         "https://pubmed.ncbi.nlm.nih.gov/"),
        ("Limites superiores toleráveis de vitaminas e minerais: Dietary Reference Intakes, National Academies.",
         "https://www.nationalacademies.org/our-work/summary-report-of-the-dietary-reference-intakes"),
        ("Situação regulatória de suplementos no Brasil, incluindo o limite da melatonina: ANVISA.",
         "https://www.gov.br/anvisa/pt-br/assuntos/alimentos/suplementos-alimentares"),
    ],
),
}
