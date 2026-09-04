# -*- coding: utf-8 -*-
"""SARMs: moduladores seletivos do receptor androgenico.

Levantamento proprio em 04/09/2026, no PubMed e no ClinicalTrials.gov.
Os resultados dos ensaios POWER foram extraidos da API v2 do
ClinicalTrials.gov, porque nao existe publicacao em revista.
"""

SARM = {
"proprio_sarms": dict(
    secoes=[
        dict(h="A pergunta desta página", tipo="p", corpo=[
            "SARM não é peptídeo. É molécula pequena, oral, que age no <strong>receptor androgênico</strong> — a "
            "mesma via da testosterona, com a promessa de agir no músculo e no osso sem agir na próstata e no couro "
            "cabeludo. Entra nesta referência porque circula nos mesmos lugares, é comprada nos mesmos sites e é "
            "empilhada nos mesmos ciclos que o resto do material daqui.",
            "A pergunta que esta página responde é a mesma das outras páginas de fonte primária: "
            "<strong>quanta evidência existe em gente</strong>. Mas com um agravante que os peptídeos não têm — "
            "no caso dos SARMs, existe medição do que vem <em>dentro do frasco</em>, e ela muda a conversa inteira.",
            "Por isso a página começa pelo frasco, e só depois fala de molécula.",
        ]),

        dict(h="Comece pelo frasco, não pela molécula", tipo="p", corpo=[
            "Duas análises químicas independentes compraram produtos vendidos como SARM e mediram o que havia "
            "dentro. Os números abaixo são delas, não meus.",
        ], tabela=dict(
            cap="O que a análise química encontrou em produtos vendidos como SARM",
            linhas=[
                ["Achado", "<em>JAMA</em>, 2017 — 44 produtos<br><small>comprados nos EUA pela internet</small>",
                 "<em>Sex Med</em>, 2024 — 13 produtos<br><small>comprados na Itália pela internet</small>"],
                ["Continha o SARM declarado", "<strong>23 de 44 (52%)</strong>", "cerca de <strong>70%</strong>"],
                ["Continha <strong>outro</strong> SARM, não o do rótulo", "—", "<strong>23%</strong>"],
                ["Continha outro fármaco não aprovado",
                 "<strong>17 de 44 (39%)</strong> — ibutamoren (MK-677), GW501516 ou SR9009",
                 "<strong>30%</strong> — tamoxifeno, clomifeno, testosterona, epimetandienona, tadalafila"],
                ["Não continha ativo nenhum", "<strong>4 de 44 (9%)</strong>", "1 amostra"],
                ["Trazia substância fora do rótulo", "11 de 44 (25%)", "mais de um ativo em <strong>&gt;60%</strong>"],
                ["Dose batia com o rótulo", "<strong>18 de 44 (41%)</strong>",
                 "teor entre <strong>30% e 90%</strong> do declarado"],
            ])),

        dict(h="Por que isso vem antes de tudo", tipo="li", corpo=[
            "<strong>Discutir o perfil de um SARM específico pressupõe que o frasco contenha aquele SARM.</strong> "
            "Na maior análise publicada, isso valeu para pouco mais da metade das amostras.",
            "<strong>Quem recebeu MK-677, GW501516 ou SR9009 no lugar não tomou sequer um SARM</strong> — são "
            "secretagogo de GH, agonista de PPARδ e agonista de REV-ERB. Mecanismo diferente, literatura diferente, "
            "risco diferente. A bula mental que a pessoa leu não descreve o que ela tomou.",
            "<strong>O problema atinge quem nem procurou SARM.</strong> Num levantamento com 170 adolescentes de "
            "academia em Atenas, <strong>9% dos usuários de suplemento</strong> consumiam produtos contaminados com "
            "esteroides anabolizantes, pró-hormônios, SARMs e inibidores de aromatase <strong>não declarados no "
            "rótulo</strong>. 63% compraram pela internet, e nenhum havia falado com médico ou nutricionista.",
            "<strong>Tudo o que vem abaixo descreve moléculas.</strong> A tabela acima descreve mercadoria. As duas "
            "coisas não são a mesma, e a segunda é a que chega em casa.",
        ]),

        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
            "Levantamento feito no PubMed e no ClinicalTrials.gov em 4 de setembro de 2026. A coluna que decide não "
            "é a de artigos: é a de <strong>ensaio registrado em humano</strong>.",
        ], tabela=dict(
            cap="Evidência em humano — SARMs",
            linhas=[
                ["Composto", "Artigos no PubMed", "Ensaios em humano registrados", "Fase máxima atingida"],
                ["<strong>Enobosarm</strong><br><small>ostarina · MK-2866 · GTx-024 · S-22</small>",
                 "116", "<strong>17</strong>", "<strong>Fase 3</strong> — dois ensaios, concluídos em 2013"],
                ["<strong>LGD-4033</strong><br><small>ligandrol · VK5211</small>",
                 "50", "1 de fase 2 <small>(fratura de quadril, n=108)</small> + fase 1 publicada",
                 "Fase 2"],
                ["<strong>GSK2881078</strong>", "15", "3 <small>(duas de fase 1, uma de fase 2a em DPOC, n=97)</small>",
                 "Fase 2a"],
                ["<strong>MK-0773</strong> <small>(Merck)</small>", "—",
                 "3 <small>(duas de fase 1, uma de fase 2a em sarcopenia, n=170)</small>", "Fase 2a"],
                ["<strong>OPK-88004</strong> <small>(OPKO)</small>", "—",
                 "1 de fase 2 <small>(hiperplasia prostática, n=114)</small> — <strong>encerrada</strong>", "Fase 2"],
                ["<strong>PF-06260414</strong> <small>(Pfizer)</small>", "—",
                 "1 de fase 1 <small>(n=72)</small>; a segunda foi retirada com n=0", "Fase 1"],
                ["<strong>RAD140</strong><br><small>testolona · vosilasarm</small>", "43",
                 "<strong>1 em toda a história do composto</strong> <small>(fase 1, n=20)</small>", "Fase 1"],
                ["<strong>Andarina</strong> <small>(S-4 · GTx-007)</small>", "41", "<strong>0</strong>", "—"],
                ["<strong>YK-11</strong>", "20", "<strong>0</strong>", "—"],
                ["<strong>S-23</strong>", "12 <small>(com filtro de receptor androgênico)</small>",
                 "<strong>0</strong>", "—"],
                ["<strong>ACP-105 · LGD-3303 · RAD-150</strong> <small>(somados)</small>", "22",
                 "<strong>0</strong>", "—"],
            ])),

        dict(h="O que essa tabela quer dizer", tipo="li", corpo=[
            "<strong>O ranking de evidência é quase o inverso do ranking de vendas.</strong> O composto com fase 3 "
            "(enobosarm) não é o que se vende; o mais vendido e mais discutido em fórum de treino, o "
            "<strong>RAD140</strong>, tem a base humana inteira em <strong>20 pacientes oncológicas, uma vez, "
            "em 2020</strong>.",
            "<strong>Quatro compostos populares têm zero ensaio clínico registrado</strong>: andarina, YK-11, S-23 e "
            "o bloco ACP-105 / LGD-3303 / RAD-150. A literatura deles é roedor, cultura de célula e química "
            "analítica antidoping — não estudo em pessoa.",
            "<strong>A revisão sistemática que cobre o campo lista seis SARMs</strong> — LGD-4033, PF-06260414, "
            "GSK2881078, GTx-024, MK-0773 e OPK-88004 — reunindo <strong>9 ensaios randomizados e 970 pacientes</strong>, "
            "idade média de <strong>57,1 anos</strong> e seguimento médio de <strong>80 dias</strong>. Note quem "
            "<em>não</em> está nessa lista: RAD140, andarina, YK-11 e S-23.",
            "<strong>A população estudada é doente e é velha.</strong> Os desfechos são caquexia oncológica, "
            "sarcopenia, fratura de quadril, DPOC, hiperplasia prostática e câncer de mama. "
            "<strong>Ninguém estudou o homem de trinta anos que treina.</strong>",
            "<strong>Nenhum SARM foi aprovado por nenhuma agência, em lugar nenhum</strong>, para nenhuma indicação.",
        ]),

        dict(h="Os dois únicos ensaios de fase 3 do campo", tipo="p", corpo=[
            "Os ensaios <strong>POWER 1</strong> e <strong>POWER 2</strong> testaram enobosarm contra placebo em "
            "perda muscular por câncer de pulmão, com <strong>651 pacientes somados</strong>. São o topo da pirâmide "
            "de evidência de todos os SARMs.",
            "<strong>E não existe artigo sobre eles.</strong> Nenhuma publicação de resultados foi indexada no "
            "PubMed nem consta vinculada aos próprios registros — a única referência ligada aos dois é o artigo de "
            "<em>desenho</em>. Os números abaixo foram extraídos da <strong>API v2 do ClinicalTrials.gov</strong> em "
            "4 de setembro de 2026, que é o único lugar onde eles existem.",
            "Os dois ensaios tinham <strong>desfechos coprimários</strong>, medidos no dia 84 como percentual de "
            "respondedores: ganho de <strong>≥10% na potência de subida de escada</strong> para função física, e "
            "variação <strong>≥0%</strong> (isto é, não perder) para massa magra.",
        ], tabela=dict(
            cap="POWER 1 e POWER 2 — desfechos coprimários no dia 84",
            linhas=[
                ["Ensaio", "Desfecho coprimário", "Enobosarm", "Placebo"],
                ["<strong>POWER 1</strong><br><small>NCT01355484 · platina + taxano<br>160 vs. 161</small>",
                 "Função física", "29,4% <small>(IC95% 22,4–37,1)</small>", "24,2% <small>(IC95% 17,8–31,6)</small>"],
                ["", "Massa magra", "41,9% <small>(IC95% 34,1–49,9)</small>", "30,4% <small>(IC95% 23,4–38,2)</small>"],
                ["<strong>POWER 2</strong><br><small>NCT01355497 · platina + não-taxano<br>159 vs. 161</small>",
                 "Função física", "<strong>19,5%</strong> <small>(IC95% 13,6–26,5)</small>",
                 "<strong>24,8%</strong> <small>(IC95% 18,4–32,3)</small>"],
                ["", "Massa magra", "46,5% <small>(IC95% 38,6–54,6)</small>", "37,9% <small>(IC95% 30,4–45,9)</small>"],
                ["<strong>Eventos adversos graves</strong>", "POWER 1", "56 de 160", "60 de 161"],
                ["", "POWER 2", "109 de 165", "113 de 165"],
            ])),

        dict(h="Como ler esses números sem forçar a barra", tipo="li", corpo=[
            "<strong>O registro não posta nenhuma análise estatística, nenhum valor de p e nenhum desfecho "
            "secundário</strong> — só as proporções e seus intervalos. Por isso esta página <strong>não afirma "
            "significância em direção alguma</strong>.",
            "<strong>Na função física o efeito não aparece.</strong> No POWER 1 os intervalos se sobrepõem em quase "
            "toda a extensão. No POWER 2 a <strong>estimativa da droga fica abaixo da do placebo</strong> — 19,5% "
            "contra 24,8%.",
            "<strong>Na massa magra a droga fica à frente nos dois</strong>, com diferenças de 11,5 e 8,6 pontos "
            "percentuais — mas os intervalos ainda se sobrepõem em ambos.",
            "<strong>Como os desfechos eram coprimários</strong>, uma função física que não se separa do placebo já "
            "basta para o programa não entregar o que precisava. O que veio depois é coerente com isso: nenhum "
            "pedido de aprovação para caquexia, e o enobosarm migrou para câncer de mama e, agora, para preservação "
            "de massa magra em quem usa GLP-1.",
            "<strong>Sem sinal de segurança contra a droga</strong>: eventos adversos graves praticamente idênticos "
            "entre os braços nos dois ensaios.",
            "<strong>Os resultados do POWER 2 só foram postados em 09/11/2020</strong> — sete anos e meio depois da "
            "conclusão primária, em maio de 2013. Os do POWER 1 saíram em 03/03/2016.",
            "<strong>Ambos os registros declaram acordo restritivo de publicação</strong>: o patrocinador recebe "
            "cópia antecipada de qualquer comunicação de resultados com 60 dias de antecedência, tem 60 dias para "
            "pedir alterações e pode pedir mais 60 de adiamento; o investigador não apresenta dados antes da "
            "publicação pelo patrocinador ou de 18 meses após o fim do estudo.",
        ]),

        dict(h="Os números de eficácia que existem, e o tamanho deles", tipo="p", corpo=[
            "Fora dos POWER, três ensaios publicados sustentam quase tudo o que se afirma sobre SARM. Vale ver o "
            "que cada um mediu, em quem, e por quanto tempo.",
        ], tabela=dict(
            cap="Os ensaios publicados que sustentam o campo",
            linhas=[
                ["Ensaio", "Composto", "Quem", "O que achou", "Ressalva"],
                ["Basaria 2013<br><small>J Gerontol A · duplo-cego, controlado por placebo</small>",
                 "<strong>LGD-4033</strong>", "76 homens saudáveis de 21 a 50 anos, <strong>21 dias</strong>, "
                 "0,1 / 0,3 / 1,0 mg",
                 "Massa magra subiu de forma dose-dependente; gordura não mudou. Bem tolerado, sem evento adverso "
                 "grave. PSA, hemoglobina, AST, ALT e intervalo QT sem alteração",
                 "<strong>Supressão dose-dependente de testosterona total, SHBG, HDL e triglicerídeos.</strong> FSH e "
                 "testosterona livre caíram só na dose de 1,0 mg. Tudo voltou ao basal após a suspensão. "
                 "<strong>Vinte e um dias</strong> não dizem nada sobre um ciclo de doze semanas"],
                ["Dobs 2013<br><small>Lancet Oncol · fase 2, duplo-cego</small>",
                 "<strong>Enobosarm</strong>", "159 pacientes com câncer e perda de peso, <strong>113 dias</strong>",
                 "Massa magra total vs. basal: <strong>+1,5 kg</strong> na dose de 1 mg (p=0,0012) e "
                 "<strong>+1,0 kg</strong> na de 3 mg (p=0,046). Placebo: +0,02 kg, não significativo",
                 "O desfecho é variação <strong>contra o próprio basal</strong>, não contra o placebo. E repare na "
                 "<strong>não-monotonicidade</strong>: a dose maior rendeu menos que a menor"],
                ["Palmieri 2024<br><small>Lancet Oncol · fase 2, aberto, 35 centros, 9 países</small>",
                 "<strong>Enobosarm</strong>", "136 randomizadas / 102 avaliáveis, câncer de mama avançado "
                 "RE+/HER2−/RA+",
                 "Benefício clínico em 24 semanas: <strong>32%</strong> na dose de 9 mg e <strong>29%</strong> na de 18 mg",
                 "Estudo <strong>aberto</strong>, sem braço de placebo. Eventos adversos grau 3–4 relacionados em 8% e "
                 "16% — o mais frequente foi <strong>elevação de transaminases</strong>. As duas fases 3 seguintes "
                 "foram <strong>encerradas precocemente</strong>, com 52 e 5 pacientes recrutados"],
            ])),

        dict(h="A revisão que procurou efeito em gente saudável e não achou", tipo="p", corpo=[
            "É o achado mais desconfortável desta página, e não é meu: é de uma revisão guarda-chuva de revisões "
            "sistemáticas e metanálises sobre sete intervenções farmacológicas de melhora de desempenho em "
            "<strong>atletas saudáveis</strong>.",
            "Os SARMs estavam no protocolo de busca. O resultado: <strong>nenhum estudo sobre SARMs atendeu aos "
            "critérios de inclusão</strong>. Não houve o que revisar.",
            "Na mesma revisão, a <strong>creatina</strong> é a única intervenção com benefício de desempenho "
            "considerado seguro nas doses controladas — e ela custa uma fração, é legal e tem bula.",
            "Ou seja: para a pessoa saudável que treina, que é quem compra, o nível de evidência agregada de SARM é "
            "<strong>zero revisão sistemática elegível</strong>. Enquanto isso, o dano já tem série de casos, "
            "hospitalização e um transplante — a seção seguinte.",
        ]),

        dict(h="Segurança: o que está documentado", tipo="p", corpo=[
            "Ao contrário da eficácia, o dano tem número, tem série de casos e tem desfecho duro.",
        ], tabela=dict(
            cap="O que a literatura de segurança registra",
            linhas=[
                ["Levantamento", "O que encontrou"],
                ["<strong>Revisão sistemática de segurança</strong><br><small>Vignali 2023 · 33 estudos, 2.136 "
                 "pacientes, <strong>1.447 expostos</strong></small>",
                 "Nos relatos de caso: <strong>15 de lesão hepática induzida por fármaco (DILI)</strong>, 1 ruptura "
                 "de tendão de Aquiles, 1 rabdomiólise, 1 elevação reversível de enzimas. Nos ensaios clínicos, "
                 "elevação de ALT em média <strong>7,1%</strong> dos expostos, e <strong>2 casos de rabdomiólise</strong> "
                 "com GSK2881078. Conclusão dos autores: o uso recreativo deve ser fortemente desencorajado"],
                ["<strong>Revisão sistemática do abuso por atletas</strong><br><small>Vasireddi 2025 · 72 artigos, "
                 "2003 a 2022</small>",
                 "Prevalência estimada de <strong>1% a 3%</strong>. Treze relatos descrevendo 15 casos: "
                 "<strong>todos homens</strong>, mediana de 32 anos, todos por via oral, curso médio de 8 semanas. "
                 "<strong>Cinco pacientes negaram explicitamente uso de droga ilícita</strong> — acreditavam estar "
                 "dentro da lei. Doses relatadas <strong>muito acima</strong> das estudadas clinicamente"],
                ["<strong>Série de lesão hepática</strong><br><small>Nash 2024 · 9 hospitais terciários na "
                 "Austrália, 2017–2023</small>",
                 "23 casos envolvendo 40 fármacos, <strong>14 deles SARMs</strong>. 22 de 23 homens, mediana de 30 "
                 "anos. Latência mediana de <strong>58 dias</strong>. <strong>17 de 23 internados.</strong> Tempo "
                 "mediano até a bioquímica normalizar: <strong>175 dias</strong>. <strong>Um transplante "
                 "hepático.</strong> Nenhuma morte"],
                ["<strong>Padrão da lesão</strong><br><small>Mohideen 2022 · revisão dedicada</small>",
                 "Colestase <em>branda</em>: icterícia de instalação insidiosa, <strong>hiperbilirrubinemia "
                 "marcada</strong> e elevação apenas leve de enzimas, com pouca lesão de ducto, inflamação ou "
                 "necrose. <strong>Não há tratamento estabelecido</strong> — a melhora costuma vir da suspensão"],
            ])),

        dict(h="No Brasil, isto é proibido — e a proibição inclui a manipulação", tipo="p", corpo=[
            "Esta é a diferença prática entre a página de SARM e quase todas as outras deste site. Aqui não existe "
            "zona cinzenta de importação pessoal ou de fórmula manipulada: existe uma resolução que fecha as duas "
            "portas.",
        ], tabela=dict(
            cap="Status regulatório dos SARMs",
            linhas=[
                ["Jurisdição", "Situação", "Detalhe verificado"],
                ["<strong>Brasil</strong> <small>(ANVISA)</small>", "<strong>Proibido</strong>",
                 "A <strong>Resolução (RE) 791/2021</strong>, publicada em <strong>23/02/2021</strong>, proibiu a "
                 "comercialização, a distribuição, a fabricação, a importação, a <strong>manipulação</strong>, a "
                 "propaganda e o uso de produtos com SARM, e determinou <strong>apreensão e inutilização</strong>. "
                 "Aplica-se a produto industrializado e manipulado, importado e nacional, em meio físico e remoto. "
                 "A própria ANVISA registra que <strong>não há medicamento com SARM registrado</strong> na Agência"],
                ["<strong>Antidopagem</strong> <small>(WADA / ABCD)</small>",
                 "<strong>Proibido em todo tempo</strong>",
                 "Lista Proibida 2026, em vigor desde <strong>01/01/2026</strong>, seção <strong>S1.2 — Outros "
                 "Agentes Anabolizantes</strong>. O texto nomeia <strong>andarina, enobosarm (ostarina), LGD-4033 "
                 "(ligandrol), RAD140, S-23 e YK-11</strong>. Categoria S1 vale <strong>dentro e fora de "
                 "competição</strong>"],
                ["<strong>Estados Unidos</strong> <small>(FDA)</small>",
                 "<strong>Não aprovado; ilegal como suplemento</strong>",
                 "A FDA registra que SARMs não podem ser legalmente comercializados nos EUA nem como suplemento "
                 "alimentar nem como medicamento. Riscos que a Agência lista: infarto e AVC, psicose e alucinações, "
                 "distúrbio de sono, disfunção sexual, <strong>lesão hepática e falência hepática aguda</strong>, "
                 "infertilidade, aborto espontâneo e atrofia testicular"],
            ])),

        dict(h="Os três que são vendidos como SARM e não são", tipo="p", corpo=[
            "Os três apareceram como substituto ou adulterante nos produtos analisados pelo <em>JAMA</em>. Nenhum "
            "age no receptor androgênico.",
        ], tabela=dict(
            cap="Vendidos como SARM, com outro mecanismo",
            linhas=[
                ["Composto", "O que é de fato", "Literatura no PubMed"],
                ["<strong>MK-677 · ibutamoren</strong>",
                 "<strong>Secretagogo de GH</strong> — agonista do receptor de grelina. Não toca no receptor "
                 "androgênico", "Literatura clínica própria, antiga, de outro campo"],
                ["<strong>GW501516 · cardarine</strong>", "<strong>Agonista de PPARδ</strong>", "372 artigos"],
                ["<strong>SR9009 · stenabolic</strong>", "<strong>Agonista de REV-ERB</strong>",
                 "<strong>1 artigo</strong> que traz os dois termos"],
            ])),

        dict(h="O que esta página não fez", tipo="li", corpo=[
            "<strong>Não traz dose, meia-vida, protocolo de ciclo nem esquema de reconstituição</strong>, por "
            "decisão. É a segunda página do site sem posologia, depois da de itens de tarja. Descrever um esquema "
            "de uso para substância cuja manipulação a ANVISA proibiu seria escrever o que não deve ser seguido.",
            "<strong>Não conferi o inteiro teor da RE 791/2021.</strong> O número, a data e o alcance da medida "
            "vieram da página oficial da ANVISA; a lista nominal de produtos apreendidos, que circula em fontes "
            "secundárias, <strong>não foi conferida no texto da resolução</strong>.",
            "<strong>Não há teste formal de hipótese nos POWER.</strong> O registro não posta valor de p. Toda a "
            "leitura desta página se limita a comparar estimativas e intervalos.",
            "<strong>Não busquei os desfechos secundários dos POWER</strong> porque eles não existem publicamente: "
            "o desenho previa durabilidade no dia 147 e análise combinada de sobrevida, e <strong>nada disso foi "
            "postado</strong>.",
            "<strong>Não conferi a interrupção do desenvolvimento do GW501516 por carcinogenicidade em roedores</strong>, "
            "que é amplamente citada no campo. Não busquei a fonte primária, e por isso não é afirmação desta página.",
            "<strong>Não há dado brasileiro de prevalência de uso.</strong> A estimativa de 1% a 3% é de atletas, em "
            "literatura internacional.",
        ]),

        dict(h="O que sobra depois de tudo", tipo="li", corpo=[
            "<strong>O topo da pirâmide de evidência deste campo nunca passou por revisão por pares.</strong> Os "
            "dois únicos ensaios de fase 3 de qualquer SARM, 651 pacientes somados, existem só como tabela em "
            "registro público — sem artigo, sem valor de p, sem desfecho secundário, e um deles com sete anos e meio "
            "de atraso na postagem. Quando se diz que falta evidência sobre SARM, não é só ausência de estudo: é "
            "<strong>evidência produzida e não publicada</strong>.",
            "<strong>Onde há número de eficácia, ele é modesto e estranho</strong> — +1,5 kg de massa magra em 113 "
            "dias no melhor caso, com a dose maior rendendo menos que a menor.",
            "<strong>A ausência de evidência em pessoa saudável é formal, não impressionista.</strong> Uma revisão "
            "guarda-chuva procurou e não achou um único estudo elegível.",
            "<strong>O risco, ao contrário, tem número</strong>: 15 casos de DILI numa revisão, 23 numa série "
            "australiana com 17 internações e um transplante, 58 dias de latência mediana, 175 dias até o fígado "
            "normalizar.",
            "<strong>E o risco maior nem é farmacológico.</strong> Metade dos produtos não contém o que diz conter. "
            "Antes de escolher a molécula, há um problema de mercadoria a resolver — e ele não se resolve lendo "
            "sobre a molécula.",
        ]),
    ],
    referencias=[
        ("Van Wagoner RM et al., 2017 — análise química de 44 produtos vendidos pela internet como SARM. JAMA 318(20):2004-2010. É a fonte da tabela que abre esta página.",
         "https://doi.org/10.1001/jama.2017.17069"),
        ("Gaudiano MC et al., 2024 — produtos ilegais com SARM comprados na Itália: análise por espectrometria de massas e RMN quantitativa. Sex Med 12(2):qfae018.",
         "https://doi.org/10.1093/sexmed/qfae018"),
        ("Tsarouhas K et al., 2018 — suplementos contaminados com substâncias dopantes em atletas adolescentes de Atenas. Food Chem Toxicol 115:447-450.",
         "https://doi.org/10.1016/j.fct.2018.03.043"),
        ("Wen J et al., 2024 — revisão sistemática dos SARMs sobre desempenho físico: 9 ensaios randomizados, 970 pacientes, seis compostos. Clin Endocrinol 102(1):3-27.",
         "https://doi.org/10.1111/cen.15135"),
        ("Vignali JD et al., 2023 — revisão sistemática de segurança dos SARMs em adultos saudáveis, com implicações para uso recreativo. J Xenobiot 13(2):218-236.",
         "https://doi.org/10.3390/jox13020017"),
        ("Vasireddi N et al., 2025 — revisão sistemática do abuso de SARMs por atletas. Am J Sports Med 53(4):999-1009.",
         "https://doi.org/10.1177/03635465241252435"),
        ("Warrier AA et al., 2023 — revisão guarda-chuva de revisões sistemáticas sobre drogas de melhora de desempenho em atletas saudáveis. Nenhum estudo de SARM atendeu aos critérios de inclusão. Sports Health 16(5):695-705.",
         "https://doi.org/10.1177/19417381231197389"),
        ("Nash E et al., 2024 — lesão hepática por SARMs, esteroides anabolizantes e suplementos de musculação na Austrália: 23 casos, um transplante. Aliment Pharmacol Ther 59(8):953-961.",
         "https://doi.org/10.1111/apt.17906"),
        ("Mohideen H et al., 2022 — SARMs como toxina hepática emergente: padrão colestático da lesão. J Clin Transl Hepatol 11(1):188-196.",
         "https://doi.org/10.14218/JCTH.2022.00207"),
        ("Basaria S et al., 2013 — segurança, farmacocinética e efeitos do LGD-4033 em homens jovens saudáveis, 21 dias. J Gerontol A Biol Sci Med Sci 68(1):87-95.",
         "https://doi.org/10.1093/gerona/gls078"),
        ("Dobs AS et al., 2013 — efeito do enobosarm sobre perda muscular e função física em pacientes com câncer: ensaio de fase 2. Lancet Oncol 14(4):335-345.",
         "https://doi.org/10.1016/S1470-2045(13)70055-X"),
        ("Palmieri C et al., 2024 — atividade e segurança do enobosarm em câncer de mama avançado RA+/RE+/HER2−: fase 2. Lancet Oncol 25(3):317-325.",
         "https://doi.org/10.1016/S1470-2045(24)00004-4"),
        ("Crawford J et al., 2016 — desenho e justificativa do programa de fase 3 do enobosarm (ensaios POWER). É a única publicação vinculada aos dois registros. Curr Oncol Rep 18(6):37.",
         "https://doi.org/10.1007/s11912-016-0522-0"),
        ("ClinicalTrials.gov, registro NCT01355484 (POWER 1) — resultados dos desfechos coprimários, extraídos da API v2 em 4 de setembro de 2026.",
         "https://clinicaltrials.gov/study/NCT01355484"),
        ("ClinicalTrials.gov, registro NCT01355497 (POWER 2) — resultados dos desfechos coprimários, postados em 9 de novembro de 2020.",
         "https://clinicaltrials.gov/study/NCT01355497"),
        ("ANVISA — 'Medida proíbe comercialização de produtos que contenham SARM', notícia oficial que descreve a Resolução (RE) 791/2021, publicada em 23 de fevereiro de 2021.",
         "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2021/medida-proibe-comercializacao-de-produtos-que-contenham-sarm"),
        ("Autoridade Brasileira de Controle de Dopagem — Código Mundial Antidopagem, Lista Proibida 2026, em vigor desde 1º de janeiro de 2026. Seção S1.2, página 6.",
         "https://www.gov.br/abcd/pt-br/composicao/atletas/substancias-e-metodos-proibidos/arquivos-lista-de-substancias-proibidas/lista_proibida_2026_pt-br_v-3.pdf"),
        ("FDA — 'FDA Warns of Use of Selective Androgen Receptor Modulators (SARMs) Among Teens, Young Adults', página datada de 26 de abril de 2023.",
         "https://www.fda.gov/consumers/consumer-updates/fda-warns-use-selective-androgen-receptor-modulators-sarms-among-teens-young-adults"),
    ],
),
}
