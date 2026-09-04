# -*- coding: utf-8 -*-
"""Pagina de nootropicos montada de fonte primaria.

Contagens do PubMed conferidas em 04/09/2026, uma consulta por item, com o
filtro Randomized Controlled Trial OR Meta-Analysis. As faixas de dose foram
extraidas dos resumos dos proprios ensaios, nao de rotulo nem de forum.
"""

NOOT = {
"proprio_nootropicos": dict(
    secoes=[
        dict(h="Como ler esta página", tipo="p", corpo=[
            "Trinta e dois nootrópicos com evidência humana, mais doze que a comunidade usa e que "
            "<strong>não têm ensaio nenhum</strong>. Nenhum deles repete o que já está nas outras páginas: "
            "piracetam, fenilpiracetam, picamilon, Cortexin, Cerebrolisina, Semax, Selank, alpha-GPC, citicolina, "
            "L-teanina, bacopa, rhodiola, ginkgo e lion's mane já têm lugar próprio neste site.",
            "A coluna <strong>ECR/meta</strong> é o número de ensaios randomizados e metanálises indexados no "
            "PubMed, <strong>conferido item a item em 4 de setembro de 2026</strong>. A coluna "
            "<strong>faixa dos estudos</strong> não é dose de rótulo nem de fórum: é a dose que apareceu nos "
            "resumos dos ensaios citados, transportada de lá.",
            "A ordem é por quantidade de evidência, não por quanto funciona. São coisas diferentes, e a página "
            "inteira existe para deixar isso à vista.",
        ]),
        dict(h="Quatro contagens estavam infladas", tipo="li", corpo=[
            "<strong>L-tirosina aparecia com 199 ensaios.</strong> Restringindo a consulta a "
            "<em>tyrosine supplementation</em> e <em>tyrosine administration</em>, sobram <strong>14</strong>. "
            "Os outros 185 são bioquímica da tirosina como aminoácido, não suplementação.",
            "<strong>Uridina aparecia com 62.</strong> Restrita, cai para <strong>6</strong> — e ao abrir os "
            "resumos, o que existe é lipoatrofia por antirretroviral e quimioterapia com tegafur-uracila. "
            "<strong>Nada de cognição.</strong>",
            "<strong>Forskolina aparecia com 30.</strong> Restrita ao extrato de <em>Coleus forskohlii</em>, "
            "sobram <strong>5</strong>. O resto é forskolina como reagente de laboratório para ativar adenilato "
            "ciclase — não tem nada a ver com tomar cápsula.",
            "<strong>Agmatina aparecia com 9.</strong> Restrita a uso psiquiátrico ou cognitivo: "
            "<strong>zero</strong>.",
        ]),
        dict(h="Faixa A — evidência humana substancial", tipo="p", corpo=[
            "Trinta ou mais ensaios randomizados e metanálises. Volume alto significa que muita gente estudou — "
            "não que o resultado foi favorável.",
        ], tabela=dict(
            cap="Nootrópicos com 30 ou mais ensaios randomizados ou metanálises",
            linhas=[
                ["Item", "Faixa dos estudos", "Para quê", "ECR/meta", "Ressalva"],
                ["Modafinil", "<strong>não publicada aqui</strong>", "Vigília, atenção, fadiga", "<strong>425</strong>",
                 "<strong>Medicamento de prescrição.</strong> Em voluntário saudável a base é bem menor: 53 artigos e 27 ensaios. Proibido pela WADA em competição"],
                ["Açafrão (<em>Crocus sativus</em>)", "20–100 mg/dia; 30 mg/dia é o mais repetido", "Depressão, humor, TDAH", "<strong>173</strong>",
                 "A melhor relação entre evidência e risco desta tabela. O extrato é caro e adulteração é comum — açafrão é uma das especiarias mais falsificadas do mundo"],
                ["Nicotina (fora do cigarro)", "7 mg/24 h transdérmica nos ensaios em não fumante", "Atenção, memória de trabalho", "<strong>155</strong>",
                 "<strong>Dependência.</strong> O efeito cognitivo é real e pequeno; o custo é uma substância que cria dependência física. Não é item de uso casual"],
                ["Pycnogenol", "75–200 mg/dia", "Cognição, circulação, pele", "<strong>92</strong>",
                 "Extrato patenteado de casca de pinheiro marítimo. Boa parte dos ensaios é financiada pelo detentor da marca"],
                ["Tianeptina", "<strong>não publicada aqui</strong>", "Depressão, humor", "<strong>55</strong>",
                 "<strong>Medicamento de prescrição, e o item mais perigoso desta página.</strong> Ver a seção de segurança abaixo"],
                ["Gotu kola (<em>Centella asiatica</em>)", "60 mg 2×/dia a 1.200 mg/dia, conforme o extrato", "Ansiedade, cognição, cicatrização, circulação", "<strong>52</strong>",
                 "Os extratos padronizados (ECa 233, TTFCA) não são intercambiáveis com a erva a granel, e as doses não se transferem entre eles"],
                ["Melissa officinalis", "700–1.000 mg/dia", "Ansiedade, sono, humor", "<strong>48</strong>",
                 "Sedativa. Boa parte dos ensaios é em ansiedade com depressão associada, não em pessoa saudável"],
                ["Taurina", "1–3 g/dia; 2–4 g em dose única antes do esforço", "Desempenho, cognição, cardiovascular", "<strong>48</strong>",
                 "Muito segura. O efeito cognitivo isolado é o menos demonstrado — a base forte é cardiometabólica"],
                ["Benfotiamina", "300–900 mg/dia", "Neuropatia diabética, metabolismo da glicose", "<strong>37</strong>",
                 "Tiamina lipossolúvel. <strong>Um ensaio de 24 meses com 300 mg/dia não mostrou efeito na função nervosa periférica</strong> — o volume não fechou a questão"],
                ["Vinpocetina", "10 mg 3×/dia; 30–60 mg/dia nos ensaios", "Fluxo cerebral, memória", "<strong>36</strong>",
                 "<strong>Sinal de toxicidade no desenvolvimento</strong> — ver a seção de segurança. Vendida como suplemento, o que torna o dado mais grave, não menos"],
                ["Cafeína + L-teanina", "40 mg + 97 mg; 50 mg + 100 mg; até 150 mg + 250 mg", "Atenção sustentada, redução da agitação", "<strong>31</strong>",
                 "A evidência é da <strong>combinação</strong>, com cafeína em dose baixa. Somar 200 mg de cafeína e chamar de mesma coisa não é o que foi testado"],
            ])),
        dict(h="Faixa B — a evidência existe, mas é fina", tipo="p", corpo=[
            "De 3 a 29 ensaios. É onde mora a maior parte do que se vende como nootrópico: base real, pequena, "
            "e quase sempre em doença, não em pessoa saudável.",
        ], tabela=dict(
            cap="Nootrópicos com 3 a 29 ensaios randomizados ou metanálises",
            linhas=[
                ["Item", "Faixa dos estudos", "Para quê", "ECR/meta", "Ressalva"],
                ["Sálvia (<em>S. officinalis</em>, <em>S. lavandulaefolia</em>)", "330 mg/dia; 500 mg a cada 8 h", "Memória, humor, sintomas de menopausa", "<strong>29</strong>",
                 "Restringindo a consulta a desfecho cognitivo, sobram 7 ensaios. As duas espécies não são a mesma coisa"],
                ["Huperzina A", "200–400 mcg 2×/dia", "Alzheimer, memória", "<strong>23</strong>",
                 "<strong>O ensaio multicêntrico de 210 pessoas falhou no desfecho primário com 200 mcg 2×/dia.</strong> É inibidor de acetilcolinesterase de verdade — não combinar com donepezila e afins"],
                ["Oxiracetam", "800 mg 2×/dia; até 2.400 mg/dia", "Demência vascular, memória", "<strong>22</strong>",
                 "O racetam com mais ensaios depois do piracetam. Sem registro na ANVISA, como todos desta família"],
                ["Eleuthero (<em>Eleutherococcus senticosus</em>)", "300–1.200 mg/dia do extrato", "Fadiga, desempenho, adaptógeno", "<strong>19</strong>",
                 "Não é ginseng, apesar do apelido \"ginseng siberiano\". Boa parte dos ensaios usa fórmula combinada, não o extrato isolado"],
                ["DMAE / deanol", "1.000 mg/dia (deanol); 100–200 mg (meclofenoxato)", "Humor, atenção", "<strong>16</strong>",
                 "A literatura mistura deanol e meclofenoxato, que não são a mesma molécula. Boa parte dos ensaios é dos anos 1970 e 1980"],
                ["L-tirosina", "2 g em dose única; 100–150 mg/kg/dia", "Cognição sob estresse, frio, privação de sono", "<strong>14</strong>",
                 "<strong>O efeito aparece sob estresse ou depleção, não em repouso.</strong> Em condição confortável, os ensaios não mostram ganho"],
                ["Schisandra chinensis", "1.000 mg/dia do extrato", "Fadiga, fígado, adaptógeno", "<strong>13</strong>",
                 "Quase sempre estudada dentro de fórmulas combinadas (ADAPT-232), o que impede atribuir o efeito a ela"],
                ["Reishi (<em>Ganoderma lucidum</em>)", "1,44–6 g/dia; Ganopoly 1.800 mg 3×/dia", "Fadiga, sono, imunidade", "<strong>13</strong>",
                 "A contagem bruta é 29; restrita a desfecho humano, 13. <strong>Pode potencializar anticoagulante</strong>"],
                ["Cordyceps", "1 g agudo; 6 g/dia nos protocolos longos", "Desempenho aeróbio, fadiga", "<strong>12</strong>",
                 "A contagem bruta é 46; restrita a desfecho de exercício ou fadiga, 12. O <em>C. sinensis</em> selvagem e o <em>C. militaris</em> cultivado não têm a mesma composição"],
                ["Aniracetam", "1 g/dia; 200 mg 2×/dia", "Memória, demência, ansiedade", "<strong>12</strong>",
                 "Os ensaios são em demência, dos anos 1990. Nenhum em pessoa saudável. Meia-vida curta"],
                ["Centrofenoxina / meclofenoxato", "200 mg até 2 g/dia", "Cognição no envelhecimento", "<strong>10</strong>",
                 "Um dos ensaios usou 2 g/dia por 8 semanas. É colinérgico e compartilha a literatura com o DMAE"],
                ["Mucuna pruriens", "15–30 g do pó", "Parkinson (fonte natural de levodopa)", "<strong>8</strong>",
                 "<strong>É levodopa.</strong> Não é nootrópico de rotina: os ensaios comparam a mucuna com levodopa/carbidopa em Parkinson avançado. Interação séria com IMAO e antipsicótico"],
                ["Oxaloacetato", "500 mg 2×/dia a 1.000 mg 3×/dia", "Fadiga em EM/SFC e covid longa", "<strong>8</strong>",
                 "O estudo maior é aberto e sem randomização, feito pelo fabricante. Base promissora e frágil ao mesmo tempo"],
                ["Bromantano (Ladasten)", "50–100 mg/dia; 15 mg em dose única", "Astenia, fadiga, ansiedade", "<strong>6</strong>",
                 "<strong>Proibido pela WADA.</strong> Toda a literatura é russa e do próprio desenvolvedor"],
                ["PQQ", "20–21,5 mg/dia", "Sono, fadiga, biogênese mitocondrial", "<strong>6</strong>",
                 "A contagem bruta é 12; restrita a desfecho humano, 6. Boa parte da literatura restante é em frango de corte"],
                ["Sulbutiamina", "400–600 mg/dia", "Fadiga pós-infecciosa, inibição psicocomportamental", "<strong>5</strong>",
                 "<strong>O ensaio maior, com 326 pacientes, não separou as doses do placebo no desfecho principal.</strong> Relatos de tolerância com uso contínuo"],
                ["Forskolina (<em>Coleus forskohlii</em>)", "250 mg de extrato a 10%, 2×/dia; 10 mg/dia em asma", "Composição corporal, asma, pressão intraocular", "<strong>5</strong>",
                 "A contagem bruta de 30 era artefato: forskolina é reagente padrão de laboratório. Os ensaios de composição corporal usam fórmula combinada"],
                ["Pramiracetam", "400 mg 3×/dia; 600 mg 2×/dia", "Memória, TCE", "<strong>4</strong>",
                 "Quatro ensaios, um deles concluindo que <strong>até 4.000 mg dificilmente trazem benefício em Alzheimer</strong>"],
                ["Nefiracetam", "600–900 mg/dia", "Apatia e depressão pós-AVC", "<strong>3</strong>",
                 "Curiosidade honesta: o efeito apareceu com 900 mg e <strong>não</strong> com 600 mg. Desenvolvimento interrompido por achado de toxicidade animal"],
                ["Polygala tenuifolia", "300 mg/dia (extrato BT-11)", "Memória, cognição", "<strong>3</strong>",
                 "Praticamente toda a evidência humana vem de um único extrato padronizado coreano"],
                ["Uridina monofosfato", "<strong>não levantada</strong>", "Alegação de sinapse e colina", "<strong>6</strong>",
                 "Abri os seis: são lipoatrofia por antirretroviral e quimioterapia com tegafur-uracila. <strong>Nenhum é de cognição.</strong> A dose não foi publicada aqui porque não existe ensaio cognitivo de onde tirá-la"],
            ])),
        dict(h="Faixa C — o que a comunidade usa e não tem nada por trás", tipo="p", corpo=[
            "Doze compostos com <strong>zero ou um</strong> ensaio randomizado. Não há dose aqui, e não é omissão: "
            "não existe ensaio de onde transportar um número. O que circula em fórum é extrapolação de estudo "
            "animal, quando há estudo.",
        ], tabela=dict(
            cap="Nootrópicos sem base de ensaio randomizado",
            linhas=[
                ["Item", "O que é", "Artigos no PubMed", "ECR/meta", "O que existe de fato"],
                ["Noopept (omberacetam)", "Dipeptídeo russo, análogo de cicloprolilglicina", "<strong>115</strong>", "<strong>0</strong>",
                 "115 artigos e nenhum ensaio randomizado indexado. É o caso mais desproporcional entre fama e evidência desta página"],
                ["Agmatina", "Metabólito da arginina", "1.934 <strong>(inflado)</strong>", "<strong>0</strong>",
                 "A contagem alta é neurociência básica do receptor de imidazolina. Restrita a uso psiquiátrico ou cognitivo: zero"],
                ["Celastrus paniculatus", "Óleo de semente da medicina ayurvédica", "<strong>73</strong>", "<strong>0</strong>",
                 "Toda a literatura é pré-clínica, em rato"],
                ["Shankhpushpi (<em>Convolvulus prostratus</em>)", "Erva ayurvédica para memória", "<strong>67</strong>", "<strong>0</strong>",
                 "Mesmo caso. E o nome comercial cobre pelo menos quatro espécies botânicas diferentes"],
                ["IDRA-21", "Ampacina, modulador de AMPA", "<strong>26</strong>", "<strong>0</strong>",
                 "Literatura de primata e roedor. Nunca entrou em ensaio humano"],
                ["Dihexa", "Peptídeo derivado da angiotensina IV", "<strong>18</strong>", "<strong>0</strong>",
                 "Dezoito artigos, todos pré-clínicos. Vendido como se fosse produto acabado"],
                ["9-Me-BC", "9-metil-beta-carbolina", "<strong>14</strong>", "<strong>0</strong>",
                 "Só cultura de célula e roedor. É também inibidor de MAO — o risco de interação é real e não testado em gente"],
                ["Fasoracetam", "Racetam, agonista de mGluR", "<strong>5</strong>", "<strong>0</strong>",
                 "Cinco artigos no total. Chegou a fase clínica em TDAH com variante genética, sem resultado publicado indexado"],
                ["Coluracetam", "Racetam, captação de colina de alta afinidade", "<strong>1</strong>", "<strong>0</strong>",
                 "<strong>Um artigo.</strong> É o menor número de toda esta referência"],
                ["NSI-189", "Molécula neurogênica", "<strong>14</strong>", "<strong>1</strong>",
                 "Um ensaio. O programa de desenvolvimento em depressão não avançou"],
                ["Adrafinil", "Pró-fármaco do modafinil", "<strong>43</strong>", "<strong>1</strong>",
                 "<strong>Vira modafinil no fígado</strong> — carrega o efeito e a hepatotoxicidade da conversão, com menos previsibilidade que o próprio modafinil, que é de prescrição"],
                ["PRL-8-53", "Composto de 1978", "<strong>1</strong>", "<strong>1</strong>",
                 "Existe um único artigo, e é o mesmo estudo de 1978 que a internet cita há décadas. Nunca foi replicado"],
            ])),
        dict(h="Três achados que a contagem sozinha esconde", tipo="p", corpo=[
            "<strong>1. Armodafinil não tem contagem própria.</strong> O PubMed expande a busca por "
            "<em>armodafinil</em> para o termo MeSH <em>modafinil</em>: a consulta devolve 2.437 contra 2.411 do "
            "modafinil — quase o mesmo conjunto de artigos. Restringindo a título e resumo, armodafinil tem "
            "<strong>260</strong> e modafinil tem <strong>2.150</strong>. É a mesma armadilha do Ovagen e da "
            "cocarboxilase, em outra família.",
            "<strong>2. Tianeptina tem mais literatura de dano do que a maioria tem de eficácia.</strong> São "
            "<strong>204 artigos</strong> cruzando o composto com abuso, dependência, intoxicação ou abstinência. "
            "Títulos indexados de 2025 incluem <em>\"Gas station heroin — tianeptine and its impact: a systematic "
            "review and exploratory analysis\"</em> e <em>\"Tianeptine Exposures Reported to United States Poison "
            "Centers, 2015-2023\"</em>. É agonista de receptor mu-opioide em dose alta, o que explica o padrão.",
            "<strong>3. Vinpocetina tem sinal de toxicidade no desenvolvimento.</strong> Artigo de maio de 2026: "
            "<em>\"Developmental Toxicity Evaluation of the Dietary Supplement Vinpocetine Using Mouse and Human 3D "
            "Gastruloids\"</em>. O agravante está no próprio título — ela é vendida como suplemento alimentar, sem "
            "a advertência que um medicamento carregaria.",
        ]),
        dict(h="Os três itens de tarja", tipo="li", corpo=[
            "<strong>Modafinil, tianeptina e adrafinil aparecem sem posologia</strong>, pela mesma decisão tomada "
            "na página de itens de tarja: são medicamentos de prescrição, e publicar dose de prescrição fora de "
            "prescrição não é informar, é facilitar.",
            "<strong>A nicotina fora do cigarro é o caso limite.</strong> Adesivo e goma são de venda livre no "
            "Brasil e a dose dos ensaios está publicada acima, porque é a mesma da bula. O que não muda é que ela "
            "cria dependência física.",
            "<strong>Vinpocetina e bromantano não são tarja aqui</strong>, mas nenhum dos dois tem registro na "
            "ANVISA. Circulam por importação, sem controle de lote e sem bula em português.",
        ]),
        dict(h="O que ficou de fora", tipo="li", corpo=[
            "<strong>Li resumos, não artigos completos</strong> — salvo os seis de uridina e os títulos de "
            "tianeptina e vinpocetina citados acima, que abri para conferir.",
            "<strong>Contagem não é qualidade.</strong> Vale aqui a mesma limitação declarada nas outras páginas: "
            "um número alto pode ser muitos ensaios pequenos e mal feitos.",
            "<strong>Não conferi a situação regulatória na ANVISA item a item.</strong> Onde afirmo ausência de "
            "registro, é para os racetams, o bromantano e a vinpocetina, que são de importação declarada.",
            "<strong>Não há registro do ClinicalTrials.gov nesta página.</strong> O levantamento foi de literatura "
            "publicada; ensaios em andamento não entraram.",
        ]),
    ],
    referencias=[
        ("Contagens obtidas no PubMed em 4 de setembro de 2026, com o filtro Randomized Controlled Trial[Publication Type] OR Meta-Analysis[Publication Type], uma consulta por item. Onde a consulta ampla estava inflada, a consulta restrita está declarada no texto.",
         "https://pubmed.ncbi.nlm.nih.gov/"),
        ("Faixas de dose extraídas dos resumos dos próprios ensaios recuperados em cada consulta, via E-utilities do NCBI.",
         "https://www.ncbi.nlm.nih.gov/books/NBK25501/"),
        ("Tianeptina, exposições relatadas a centros de intoxicação dos Estados Unidos entre 2015 e 2023, e revisão sistemática de 2025 sobre uso não médico.",
         "https://pubmed.ncbi.nlm.nih.gov/?term=tianeptine+AND+(poison+center+OR+abuse)"),
        ("Vinpocetina, avaliação de toxicidade no desenvolvimento em gastruloides 3D de camundongo e humanos, maio de 2026.",
         "https://pubmed.ncbi.nlm.nih.gov/42167926/"),
        ("Lista de substâncias proibidas da Agência Mundial Antidopagem, que inclui bromantano e modafinil.",
         "https://www.wada-ama.org/en/prohibited-list"),
    ],
),
}
