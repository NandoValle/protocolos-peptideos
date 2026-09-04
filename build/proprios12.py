# -*- coding: utf-8 -*-
"""CRISPR: o que a evidencia mostra.

Levantamento proprio, no PubMed (via E-utilities do NCBI), no
ClinicalTrials.gov, nas paginas oficiais de FDA, EMA, MHRA, NICE, CMS e OMS,
e na base publica de peticoes da ANVISA.

Os 12 artigos fundadores foram conferidos um a um por PMID: titulo, revista,
ano e DOI sao os do registro, nao de memoria.

A varredura da ANVISA foi feita no endpoint publico de peticoes
(consultas.anvisa.gov.br/api/documento/tecnico), por codigo de assunto e por
CNPJ. Dados brutos arquivados fora do repositorio.
"""

from datas import DATA_APURACAO as _DT

CRISPR = {
"proprio_crispr": dict(
    secoes=[

        dict(h="Por que CRISPR está nesta referência", tipo="p", corpo=[
            "Todo o resto deste site descreve compostos que circulam sem aprovação, com dose vinda de comunidade e "
            "frasco de procedência incerta. CRISPR é o contrário disso, e é por isso que vale a página: é o único "
            "lugar onde a promessa de reescrever o genoma virou <strong>medicamento aprovado por agência "
            "reguladora</strong>, com ensaio de fase 3, bula e preço.",
            "O que interessa aqui não é a molécula — não há dose, não há reconstituição, não há ciclo. O que "
            "interessa é <strong>quanto custou, em evidência, sair da promessa e chegar ao paciente</strong>. Esse "
            "número é a melhor régua disponível para ler o resto desta referência.",
            "A resposta curta: catorze anos, 64.641 artigos, um produto aprovado — e um limite que não é da "
            "tecnologia, é da quimioterapia que precisa vir antes dela.",
        ]),

        dict(h="O que é, em termos verificáveis", tipo="p", corpo=[
            "CRISPR-Cas é um sistema de <strong>imunidade adaptativa de bactérias e arqueias</strong>. Funciona em "
            "três etapas: a bactéria guarda um pedaço do DNA do vírus invasor como “espaçador” no próprio genoma; "
            "transcreve esse arquivo em RNAs-guia; e usa uma nuclease Cas dirigida por esse RNA para cortar o "
            "invasor quando ele voltar.",
            "O achado que virou ferramenta: em <em>Streptococcus pyogenes</em>, dois RNAs pareados dirigem a "
            "<strong>Cas9</strong> a cortar as duas fitas do DNA-alvo — o domínio HNH corta a fita complementar, o "
            "domínio RuvC-like corta a outra. E o par funciona quando fundido numa <strong>única molécula de RNA "
            "quimérico</strong>. Foi essa fusão que tornou a coisa programável: mudar o alvo passou a ser mudar "
            "uma sequência de RNA, não desenhar uma proteína nova.",
            "A parte que quase nunca é contada: <strong>a tesoura é precisa, o conserto não é</strong>. Quem repara "
            "a quebra é a própria célula, e o modo mais comum de reparo gera pequenas inserções e deleções que "
            "desligam o gene. Escrever uma sequência nova no lugar é bem menos eficiente. Boa parte dos problemas "
            "de segurança mais adiante nesta página vem dessa segunda metade, não da primeira.",
        ]),

        dict(h="Cronologia verificada", tipo="p", corpo=[
            "Cada linha abaixo foi conferida no PubMed pelo identificador do artigo. Duas coisas que a versão "
            "popular da história costuma apagar aparecem aqui: <strong>passaram-se 25 anos entre ver e "
            "entender</strong> — as repetições estavam publicadas desde 1987 e ninguém sabia o que eram — e "
            "<strong>a demonstração de que aquilo era um sistema imune saiu de uma fabricante de iogurte</strong>, "
            "resolvendo um problema industrial de fermento morto por bacteriófago.",
        ], tabela=dict(
            cap="Marcos, com a publicação que os estabeleceu",
            linhas=[
                ["Ano", "O que foi estabelecido", "Publicação"],
                ["1987", "Primeira observação das repetições, em <em>E. coli</em> — num artigo sobre um gene de "
                         "fosfatase alcalina. Aparecem como curiosidade de sequência, sem função conhecida",
                 "Ishino, <em>J Bacteriol</em>"],
                ["2005", "Três grupos, independentes, descobrem que os espaçadores <strong>vêm de vírus e "
                         "plasmídeos</strong> — a pista de que aquilo era defesa",
                 "Mojica, <em>J Mol Evol</em> · Bolotin e Pourcel, <em>Microbiology</em>"],
                ["2007", "Demonstração experimental de que CRISPR <strong>confere resistência adquirida a "
                         "vírus</strong>. Feito na Danisco, empresa de fermento lácteo",
                 "Barrangou, <em>Science</em>"],
                ["2010", "O sistema cliva DNA de fago e de plasmídeo — o alvo é DNA", "Garneau, <em>Nature</em>"],
                ["2011", "Descoberta do tracrRNA e da maturação do RNA-guia", "Deltcheva, <em>Nature</em>"],
                ["2012", "<strong>Cas9 programável por RNA, e o guia único quimérico.</strong> É o artigo do Nobel",
                 "Jinek, <em>Science</em>"],
                ["2012", "Publicação independente, no mesmo ano, do complexo Cas9-RNA que cliva DNA",
                 "Gasiunas, <em>PNAS</em>"],
                ["jan/2013", "Dois artigos <strong>no mesmo número da <em>Science</em></strong> levam a Cas9 para "
                             "célula humana. Taxas de edição de 2% a 25%, conforme o tipo celular",
                 "Cong (Broad) e Mali (Harvard), <em>Science</em>"],
                ["2015", "Cas12a: nuclease de RNA único, amplia o repertório de alvos", "Zetsche, <em>Cell</em>"],
                ["2016", "Cas13a: efetor cujo alvo é <strong>RNA</strong>, não DNA", "Abudayyeh, <em>Science</em>"],
                ["2016", "<strong>Edição de base</strong>: troca uma base por outra <em>sem cortar</em> a dupla-fita",
                 "Komor, <em>Nature</em>"],
                ["2017", "Editor de base de adenina, completando as quatro transições possíveis",
                 "Gaudelli, <em>Nature</em>"],
                ["2019", "<strong>Prime editing</strong>: escreve sequência nova sem quebra de dupla-fita e sem "
                         "molde doador", "Anzalone, <em>Nature</em>"],
                ["out/2020", "<strong>Nobel de Química</strong> a Emmanuelle Charpentier e Jennifer Doudna, "
                             "“pelo desenvolvimento de um método de edição de genomas”", "Comitê Nobel"],
                ["nov/2023", "<strong>Primeira aprovação regulatória do mundo</strong> de uma terapia CRISPR: a "
                             "MHRA autoriza o Casgevy no Reino Unido", "MHRA"],
            ])),

        dict(h="O tamanho real do campo", tipo="p", corpo=[
            f"Busca no PubMed em {_DT}, com o termo no título ou no resumo. O último número da tabela é o que "
            "importa para calibrar qualquer manchete sobre CRISPR.",
        ], tabela=dict(
            cap="Volume de literatura sobre CRISPR",
            linhas=[
                ["Recorte", "Registros"],
                ["Total", "<strong>64.641</strong>"],
                ["Publicados em 2012", "139"],
                ["Publicados em 2015", "1.252"],
                ["Publicados em 2026 (ano corrente, incompleto)", "7.738"],
                ["Termo “base editing”", "2.251"],
                ["Termo “prime editing”", "1.080"],
                ["CRISPR <strong>com tipo de publicação “Clinical Trial”</strong>", "<strong>67</strong>"],
            ])),

        dict(h="Leitura desses números", tipo="li", corpo=[
            "<strong>De 64.641 artigos, 67 são ensaios clínicos.</strong> São 0,10%. O campo é esmagadoramente "
            "pré-clínico — o que não é crítica, é a idade da tecnologia. Mas é o denominador correto.",
            "<strong>O crescimento é real e recente.</strong> De 139 artigos em 2012 para 7.738 só no ano "
            "corrente. Volume de publicação, porém, não é volume de evidência clínica: as duas curvas não andam "
            "juntas.",
            "<strong>As duas gerações seguintes já têm literatura própria</strong> — 2.251 artigos de edição de "
            "base e 1.080 de prime editing. Elas não são refinamento cosmético: existem como resposta direta a um "
            "problema de segurança, que está mais abaixo nesta página.",
        ]),

        dict(h="O único produto aprovado", tipo="p", corpo=[
            "Um só chegou aqui: <strong>Casgevy</strong> (exagamglogene autotemcel). É terapia celular autóloga "
            "não-viral. Colhem-se as células-tronco do sangue do próprio paciente; edita-se <em>fora do corpo</em>, "
            "com CRISPR-Cas9, a região que controla o gene <strong>BCL11A</strong>; e reinfunde-se depois de "
            "quimioterapia mieloablativa com bussulfano.",
            "A lógica é indireta e elegante: o BCL11A é o que desliga a hemoglobina fetal depois do nascimento. "
            "Desligando o BCL11A, a hemoglobina fetal volta — e compensa a hemoglobina adulta defeituosa. "
            "<strong>Não se conserta o gene doente; contorna-se ele religando um gene de reserva.</strong>",
        ], tabela=dict(
            cap="Aprovações regulatórias verificadas nas páginas das agências",
            linhas=[
                ["Data", "Agência", "Escopo"],
                ["15 de novembro de 2023", "MHRA (Reino Unido)",
                 "<strong>Primeira autorização do mundo.</strong> Falciforme e beta-talassemia dependente de "
                 "transfusão, a partir de 12 anos"],
                ["8 de dezembro de 2023", "FDA (Estados Unidos)",
                 "Doença falciforme com crises vaso-oclusivas recorrentes, a partir de 12 anos"],
                ["16 de janeiro de 2024", "FDA (Estados Unidos)", "Segunda indicação"],
                ["9 de fevereiro de 2024", "Comissão Europeia / EMA",
                 "Autorização <strong>condicional</strong>. Titular: Vertex Pharmaceuticals (Ireland) Limited. "
                 "Ambas as indicações, a partir de 12 anos, quando o transplante é apropriado e <strong>não há "
                 "doador familiar compatível</strong>"],
                ["1º de julho de 2026", "FDA (Estados Unidos)", "Ampliação para <strong>2 anos ou mais</strong>"],
                ["—", "ANVISA (Brasil)",
                 "<strong>Não registrado, e sem pedido de registro.</strong> Ver a seção do Brasil, adiante"],
            ])),

        dict(h="Os números de eficácia, e o que eles não dizem", tipo="p", corpo=[
            "Os dois ensaios de fase 3 são de braço único e abertos — <strong>não há grupo de comparação</strong>. "
            "Isso limita a leitura e precisa ser dito antes dos números, não depois.",
        ], tabela=dict(
            cap="Fase 3 do Casgevy — desfechos publicados no <em>New England Journal of Medicine</em>",
            linhas=[
                ["", "Doença falciforme", "Beta-talassemia dependente de transfusão"],
                ["Pacientes tratados", "44", "52"],
                ["Seguimento mediano", "19,3 meses (0,8 a 48,1)", "20,4 meses (2,1 a 48,1)"],
                ["Enxertia de neutrófilos e plaquetas", "<strong>em todos</strong>", "<strong>em todos</strong>"],
                ["Desfecho primário",
                 "livre de crise vaso-oclusiva grave por ≥12 meses seguidos<br>"
                 "<strong>29 de 30 avaliáveis (97%)</strong>, IC95% 83–100",
                 "independência de transfusão por ≥12 meses<br>"
                 "<strong>32 de 35 avaliáveis (91%)</strong>, IC95% 77–98"],
                ["Desfecho secundário",
                 "livre de internação por crise: <strong>30 de 30 (100%)</strong>, IC95% 88–100",
                 "hemoglobina total média 13,1 g/dL; hemoglobina fetal média 11,9 g/dL, presente em "
                 "<strong>≥94% das hemácias</strong>"],
                ["Mortes / cânceres", "nenhum câncer", "nenhuma morte, nenhum câncer"],
            ])),

        dict(h="O gargalo não é o CRISPR — é o bussulfano", tipo="p", corpo=[
            "Esta é a parte mais importante da página, e a que menos aparece nas manchetes.",
            "<strong>A edição funcionou em 100% dos pacientes.</strong> Nos dois ensaios, todos enxertaram. O que "
            "limita o alcance da terapia não é a etapa de edição: é o <strong>transplante autólogo em volta "
            "dela</strong>. Os eventos adversos mais frequentes que a FDA lista são mucosite e febre neutropênica "
            "— quimioterapia, não edição genômica. A rotulagem traz ainda advertência para falha de enxertia de "
            "neutrófilos e para edição fora do alvo.",
            "Quem recebe Casgevy passa por um transplante autólogo completo, com toda a morbidade de um. É isso "
            "que separa “cura funcional” de “cura”.",
            "E há um custo que não aparece em nenhuma tabela de eficácia. O bussulfano é gonadotóxico — isso não é "
            "efeito adverso raro, é o fármaco funcionando como esperado. Numa experiência de centro único com 40 "
            "pacientes submetidos a terapia gênica:",
        ], tabela=dict(
            cap="Preservação de fertilidade e desfecho gonadal, 40 pacientes",
            linhas=[
                ["Achado", "Número"],
                ["Mulheres com captação de oócitos bem-sucedida", "todas as 23, mediana de 1,3 a 1,4 ciclos"],
                ["Trombose durante estimulação ovariana (7 tinham histórico de evento trombótico)",
                 "<strong>nenhuma</strong>, todas com profilaxia anticoagulante"],
                ["Frascos de sêmen criopreservados, mediana",
                 "<strong>2</strong> na falciforme contra 6 na talassemia"],
                ["Concentração de espermatozoides, mediana",
                 "<strong>7,1 milhões/mL</strong> na falciforme contra 80,4 milhões/mL na talassemia"],
                ["Mulheres com mais de 1 ano de seguimento que apresentaram <strong>falência ovariana</strong>, "
                 "com hormônio antimülleriano indetectável",
                 "<strong>17 de 17</strong>"],
            ])),

        dict(h="Dezessete de dezessete", tipo="li", corpo=[
            "<strong>Esse número precisa ser dito com o mesmo destaque que os 97%.</strong> Uma paciente jovem que "
            "aceita o Casgevy está, na evidência publicada até aqui, trocando as crises vaso-oclusivas por "
            "falência ovariana.",
            "<strong>A menos que passe antes por preservação de fertilidade</strong> — que é mais um procedimento, "
            "mais custo, mais tempo e mais um serviço especializado que precisa existir na cidade dela. Os autores "
            "concluem exatamente isso: preservação é segura, factível e deve ser considerada antes.",
            "<strong>A doença falciforme já compromete a fertilidade masculina antes de qualquer tratamento.</strong> "
            "A mediana de 2 frascos contra 6, e de 7,1 milhões/mL contra 80,4, é diferença entre as duas doenças, "
            "não efeito da terapia. Quem chega para a colheita já chega com menos.",
        ]),

        dict(h="Por que existem edição de base e prime editing", tipo="p", corpo=[
            "Entre 2018 e 2021, uma série de resultados corrigiu o otimismo da primeira fase. Todos abaixo foram "
            "conferidos no PubMed.",
        ], tabela=dict(
            cap="O que a literatura de segurança documenta",
            linhas=[
                ["Ano", "Achado", "Publicação"],
                ["2018", "O reparo das quebras gera, além de indels pequenos, <strong>deleções de milhares de "
                         "bases e rearranjos complexos</strong> — e esses eventos <strong>escapam da genotipagem "
                         "por PCR curta</strong>. Parte do dano não era vista porque não se olhava longe o bastante",
                 "Kosicki, <em>Nat Biotechnol</em>"],
                ["2018", "A edição por Cas9 dispara resposta de dano ao DNA mediada por <strong>p53</strong>, o que "
                         "reduz a eficiência", "Haapaniemi, <em>Nat Med</em>"],
                ["2018", "Em células-tronco pluripotentes humanas, o p53 inibe a edição — o que implica que as "
                         "células que <strong>editam melhor podem ser as com p53 comprometido</strong>. Risco "
                         "oncogênico embutido na própria seleção", "Ihry, <em>Nat Med</em>"],
                ["2021", "A edição pode causar <strong>cromotripse</strong> — fragmentação e remontagem caótica de "
                         "um cromossomo inteiro — como consequência <strong>no alvo certo</strong>, não fora dele",
                 "Leibowitz, <em>Nat Genet</em>"],
            ])),

        dict(h="A lógica que liga os quatro", tipo="p", corpo=[
            "O problema central de segurança da nuclease CRISPR <strong>não é “a tesoura errar de lugar”</strong>. "
            "É que cortar a dupla-fita <em>no lugar certo</em> já é, por si, um evento genotóxico. Melhorar a "
            "pontaria do guia não resolve.",
            "É exatamente por isso que a <strong>edição de base</strong> (2016) e o <strong>prime editing</strong> "
            "(2019) existem: os dois foram desenhados para editar <strong>sem quebrar a dupla-fita</strong>. Não "
            "são melhoria de conveniência — são resposta de engenharia a este bloco de literatura.",
            "<strong>E a pergunta sobre câncer secundário ainda não tem resposta.</strong> Nenhum ensaio citado "
            "aqui tem seguimento longo o bastante para excluí-lo. Os próprios estudos de acompanhamento declaram o "
            "prazo: o de longo prazo do Casgevy tem conclusão primária prevista para <strong>2039</strong>; o de "
            "um concorrente, para 2040. Até lá, “nenhum câncer ocorreu” significa “nenhum câncer em até 48 meses”, "
            "e nada além disso.",
        ]),

        dict(h="O que mudou em 2026: saiu do transplante e entrou na veia", tipo="p", corpo=[
            "O Casgevy edita células fora do corpo. A geração seguinte edita <strong>dentro</strong> — nanopartícula "
            "lipídica que carrega o RNA mensageiro da Cas9 e o guia até o fígado, por infusão intravenosa. Sem "
            "colheita de célula, sem quimioterapia, sem transplante.",
            "E essa geração já tem <strong>fase 3 controlada por placebo</strong>, o que o Casgevy nunca teve.",
        ], tabela=dict(
            cap="Terapias CRISPR aplicadas dentro do corpo, com resultado publicado",
            linhas=[
                ["Produto e alvo", "Estudo", "Resultado verificado"],
                ["<strong>Lonvoguran ziclumeran</strong> — angioedema hereditário",
                 "<strong>Fase 3</strong>, duplo-cego, randomizado 2:1, 80 pacientes (52 tratados, 28 placebo), "
                 "dose única de 50 mg",
                 "Taxa mensal de crises entre as semanas 5 e 28: <strong>0,26</strong> contra <strong>2,10</strong> "
                 "no placebo. Diferença relativa de <strong>−87%</strong> (IC95% −93 a −78), p&lt;0,001"],
                ["<strong>Nexiguran ziclumeran</strong> — amiloidose por transtirretina",
                 "Fase 1, 36 pacientes com cardiomiopatia, ≥12 meses de seguimento",
                 "Redução média da proteína-alvo no sangue: <strong>−89%</strong> em 28 dias e <strong>−90%</strong> "
                 "em 12 meses. 5 reações à infusão e 2 elevações transitórias de enzimas hepáticas"],
                ["<strong>NTLA-2002</strong> — angioedema hereditário",
                 "Fase 2 randomizada, 27 pacientes",
                 "Redução de <strong>75%</strong> e <strong>77%</strong> na taxa de crises contra placebo. Livres "
                 "de crise sem tratamento adicional: 40% e <strong>73%</strong>"],
                ["<strong>Edição de base sob medida</strong> — deficiência de CPS1",
                 "Relato de caso, <strong>n=1</strong>, 7 semanas de seguimento",
                 "Recém-nascido com doença de ~50% de letalidade na primeira infância. Terapia desenhada e "
                 "fabricada <strong>para a variante dele</strong>, duas infusões aos ~7 e ~8 meses. Passou a "
                 "tolerar mais proteína na dieta com metade da dose do sequestrante de nitrogênio. Nenhum evento "
                 "adverso grave"],
            ])),

        dict(h="O caso do lactente, lido pelo que ele é", tipo="li", corpo=[
            "<strong>Não é demonstração de eficácia.</strong> É n=1, com sete semanas de acompanhamento, e os "
            "próprios autores escrevem que seguimento mais longo é necessário.",
            "<strong>O que ele demonstra é logístico e regulatório</strong>: um medicamento de edição genômica "
            "desenhado para <em>uma única pessoa</em> foi fabricado, aprovado e infundido em meses. Esse é o "
            "precedente.",
            "<strong>Se isso se repetir, o modelo de “um medicamento, um ensaio, uma população” deixa de descrever "
            "o campo.</strong> E, com ele, deixa de valer a lógica de evidência que este site usa para julgar todo "
            "o resto.",
        ]),

        dict(h="O cemitério", tipo="p", corpo=[
            f"Levantamento no ClinicalTrials.gov em {_DT}: <strong>119 estudos registrados</strong> com CRISPR "
            "como intervenção. Uma amostra de 60 foi examinada registro a registro. O padrão que aparece não é "
            "aleatório.",
        ], tabela=dict(
            cap="Programas encerrados ou retirados, na amostra examinada",
            linhas=[
                ["Produto", "Patrocinador", "Situação"],
                ["CTX110 — anti-CD19 alogênico", "CRISPR Therapeutics", "<strong>Encerrado</strong>, 93 pacientes"],
                ["CTX120 — anti-BCMA", "CRISPR Therapeutics", "<strong>Encerrado</strong>, 26 pacientes"],
                ["CTX130 — anti-CD70", "CRISPR Therapeutics", "<strong>Encerrado</strong>, 49 pacientes"],
                ["CB-012 — leucemia mieloide aguda", "Caribou Biosciences", "<strong>Encerrado</strong>, 12 pacientes"],
                ["NYCE T cells", "Universidade da Pensilvânia", "<strong>Encerrado</strong>, 3 pacientes"],
                ["PACE CART19", "Universidade da Pensilvânia", "<strong>Retirado</strong>, nenhum paciente"],
                ["CheckCell-2", "Intima Bioscience", "<strong>Retirado</strong>, nenhum paciente"],
                ["EDIT-101 — primeiro CRISPR aplicado dentro do olho humano", "Editas Medicine",
                 "Situação <strong>desconhecida</strong>, 34 pacientes"],
            ])),

        dict(h="O que o cemitério mostra", tipo="li", corpo=[
            "<strong>Um bloco inteiro de terapia celular alogênica editada por CRISPR foi descontinuado.</strong> "
            "Não é acaso estatístico: é a área onde a promessa de “célula de prateleira” bateu na rejeição "
            "imunológica e na persistência celular curta.",
            "<strong>O que segue vivo tem outro perfil</strong>: doenças monogênicas com alvo único e bem "
            "definido, e edição no fígado por nanopartícula. Fase 3 em andamento para amiloidose por transtirretina "
            "e para angioedema hereditário.",
            "<strong>A fronteira nova é a mais arriscada.</strong> Já há ensaio registrado em 2026 de edição "
            "<em>in vivo</em> do gene da angiotensinogênio para tratar <strong>hipertensão</strong> — doença comum, "
            "crônica, com dezenas de tratamentos baratos existentes. Uma edição genômica permanente para uma "
            "condição que se controla com comprimido diário muda inteiramente o cálculo de risco aceitável.",
        ]),

        dict(h="Preço e acesso: o gargalo declarado não é o dinheiro", tipo="p", corpo=[
            "O Casgevy tem preço de lista de <strong>£1.651.000</strong> por tratamento no Reino Unido — o mesmo "
            "nas duas indicações, com desconto ao serviço público cujo tamanho é <strong>sigilo comercial "
            "declarado</strong> — e de <strong>US$ 2,2 milhões</strong> nos Estados Unidos. Antes da aprovação, o "
            "instituto americano de avaliação de tecnologias em saúde havia calculado um teto de US$ 1,35 a 2,05 "
            "milhões. O preço saiu <strong>acima do topo dessa faixa</strong>.",
            "Mas o número que realmente explica o acesso não é esse. Quando o NICE, na Inglaterra, projeta quantas "
            "pessoas serão tratadas, ele <strong>não cita custo</strong> como motivo da adesão baixa. Cita "
            "“a internação hospitalar longa necessária para o processo envolvido”.",
            "Esta seção é um resumo. O levantamento inteiro — quem paga, sob que condições, o comparador "
            "mais barato que ganha em 100% das simulações, o que o Brasil sabe e o que não sabe sobre a "
            "própria população de pacientes — está em <a href=\"proprio_casgevy.html\">Casgevy — preço e "
            "acesso</a>.",
        ], tabela=dict(
            cap="O funil de elegibilidade na Inglaterra, doença falciforme",
            linhas=[
                ["Etapa", "Efeito"],
                ["População com doença falciforme", "—"],
                ["Têm um dos três genótipos elegíveis", "~70%"],
                ["Desses, tiveram ≥2 crises por ano nos 2 anos anteriores", "48%"],
                ["Desses, estão aptos ao procedimento", "54%"],
                ["Desses, <strong>não têm doador familiar compatível</strong>", "85%"],
                ["= <strong>pessoas elegíveis</strong>", "<strong>1.794</strong>"],
                ["Concluem o tratamento no 1º ano", "<strong>23</strong>"],
                ["Concluem o tratamento no ano de pico", "<strong>78 por ano</strong>"],
            ])),

        dict(h="Três coisas que esse funil revela", tipo="li", corpo=[
            "<strong>O Casgevy não é alternativa ao transplante — é o que sobra para quem não achou doador.</strong> "
            "A própria autorização exige que o transplante seja apropriado e que não haja doador familiar "
            "compatível. A indicação foi desenhada dentro do nicho que o transplante deixou vazio.",
            "<strong>E existe um comparador mais barato que ganha em 100% das simulações.</strong> Análise de "
            "custo-efetividade publicada em 2026 comparou padrão de cuidado, transplante haploidêntico e terapia "
            "gênica: o padrão rende 14,3 anos de vida ajustados por qualidade a US$ 1,22 milhão; o transplante "
            "haploidêntico rende <strong>20,1 a US$ 1,15 milhão</strong>; a terapia gênica rende 22,1 a "
            "<strong>US$ 2,75 milhões</strong>. O haploidêntico venceu a terapia gênica em "
            "<strong>10.000 de 10.000 iterações</strong> de Monte Carlo. A terapia gênica é clinicamente melhor e "
            "economicamente perdedora — e o haploidêntico é justamente a técnica que dispensa compatibilidade "
            "total, ou seja, ataca o nicho da indicação por dentro.",
            "<strong>A distância entre onde estão os pacientes e onde está a terapia é de ordem de grandeza.</strong> "
            "Nascem <strong>515.000 bebês por ano</strong> com doença falciforme no mundo, majoritariamente na "
            "África subsaariana e no Caribe; são 7,74 milhões de pessoas vivendo com a doença e uma carga de "
            "mortalidade de 376.000 mortes por ano, das quais 81.100 em menores de 5 anos. O mesmo estudo de "
            "custo-efetividade estimou o teto de preço custo-efetivo da terapia gênica na Nigéria, na Índia e na "
            "Tanzânia em <strong>US$ 4.200 a US$ 22.000</strong>. O preço de lista é 520 vezes o piso dessa faixa. "
            "Nenhum desconto confidencial fecha isso.",
        ]),

        dict(h="No Brasil: não é fila lenta, é fila não iniciada", tipo="p", corpo=[
            f"Consulta em {_DT} à base pública de petições da ANVISA — o sistema “Situação de Documentos” de "
            "<code>consultas.anvisa.gov.br</code>, que permite filtrar por CNPJ e por código de assunto.",
            "Terapia gênica e celular não entra no cadastro de medicamentos: é <strong>Produto de Terapia "
            "Avançada</strong> (PTA), com registro separado, sob a RDC 505 de 2021. Buscar “exagamglogene” na base "
            "aberta de medicamentos devolve zero — e isso não significa nada, porque é a base errada.",
        ], tabela=dict(
            cap="Petições de registro de Produto de Terapia Avançada na ANVISA — o universo completo",
            linhas=[
                ["Código de assunto", "O que é", "Petições"],
                ["11586", "Registro de PTA Classe I", "1 — e é de “EMPRESA DE TESTE LTDA. (VS01)”, registro de "
                          "teste do próprio sistema"],
                ["11587", "Registro de PTA <strong>Classe II</strong>", "<strong>11</strong>"],
                ["11614", "Registro de PTA Classe I com dados e provas adicionais", "<strong>0</strong>"],
                ["11615", "Registro de PTA Classe II com dados e provas adicionais", "1"],
                ["", "<strong>Universo real, em toda a história da Agência</strong>",
                 "<strong>12 petições, de 9 empresas</strong>"],
            ])),

        dict(h="A varredura que fecha a pergunta", tipo="p", corpo=[
            "As 12 petições são de Novartis (3, deferidas), Gilead (2, deferidas), PTC, Janssen, Roche, BioMarin "
            "(cancelada), Bristol-Myers Squibb, Ferring e Ultragenyx — estas três últimas ainda em análise. "
            "<strong>Nenhuma é da Vertex</strong>, detentora do Casgevy.",
            "Para eliminar a hipótese de a petição estar sob outro assunto, a varredura foi refeita por CNPJ. A "
            "<strong>Vertex Farmacêutica do Brasil Ltda.</strong> — identificada pelo CNPJ que consta como "
            "detentora dos registros de Trikafta, Symdeko, Orkambi e Kalydeco, todos medicamentos de fibrose "
            "cística — tem <strong>541 petições</strong> no sistema da ANVISA.",
        ], tabela=dict(
            cap="Tudo o que a Vertex já protocolou no Brasil",
            linhas=[
                ["Recorte", "Petições"],
                ["Total no sistema da ANVISA", "<strong>541</strong>"],
                ["Com assunto de <strong>Produto de Terapia Avançada</strong>", "<strong>0</strong>"],
                ["De terapia gênica, celular avançada ou engenharia tecidual", "<strong>0</strong>"],
                ["De ensaio clínico com produto de terapia avançada", "<strong>0</strong>"],
            ])),

        dict(h="O que isso significa, e o que não significa", tipo="li", corpo=[
            "<strong>Não existe pedido de registro do Casgevy no Brasil.</strong> E não existe nem pedido de "
            "ensaio clínico, nem uso compassivo, nem acesso expandido. Não é caso de “está na fila e demora”: não "
            "entrou na fila.",
            "<strong>As fontes em português que afirmam aprovação da ANVISA “no início de 2024” estão erradas.</strong> "
            "Agora dá para dizer isso por evidência positiva, não por ausência de prova.",
            "<strong>Sem registro, o SUS não pode nem avaliar.</strong> O Decreto 7.646/2011, no artigo 15, exige "
            "que o pedido de incorporação instrua o processo com o número e a validade do registro na ANVISA. O "
            "debate brasileiro sobre preço do Casgevy não está travado no preço — está travado três degraus antes.",
            "<strong>E, se um dia destravar, avaliaremos no escuro.</strong> A melhor estimativa oficial de quantas "
            "pessoas têm doença falciforme no Brasil é de <strong>2007</strong> e varia entre 25 mil e 50 mil. O "
            "protocolo clínico do Ministério da Saúde de 2024 diz textualmente que “dados recentes não foram "
            "identificados”. O Reino Unido publicou 1.794 elegíveis com o funil inteiro aberto; aqui não há "
            "denominador.",
            "<strong>O que não foi verificado:</strong> se alguma petição foi protocolada por outra pessoa "
            "jurídica em nome do produto. A consulta é por CNPJ e por assunto, e a interface pública não devolve "
            "nome comercial. A busca textual por “exagamglogene” exigiria a Pesquisa Pública do SEI, que pede "
            "CAPTCHA e não foi usada.",
        ]),

        dict(h="Uma distinção que o debate público perde", tipo="p", corpo=[
            "Tudo nesta página é <strong>edição somática</strong>: altera células do próprio paciente, não é "
            "herdável, morre com ele. É o que está aprovado, o que está em ensaio e o que tem preço.",
            "O que costuma dominar a conversa sobre CRISPR é outra coisa — a <strong>edição germinativa "
            "hereditária</strong>, que altera o genoma transmitido aos descendentes. Em 2018 um pesquisador chinês "
            "anunciou o nascimento de gêmeas cujos embriões haviam sido editados, episódio que gerou literatura "
            "acadêmica própria e levou a Organização Mundial da Saúde a publicar, em julho de 2021, um marco de "
            "governança e um conjunto de recomendações em nove áreas, resultado de mais de dois anos de consulta "
            "global.",
            "<strong>São regimes éticos e legais completamente distintos.</strong> Confundir os dois é a principal "
            "fonte de ruído no debate — e faz parecer que a terapia aprovada carrega um problema moral que ela não "
            "tem.",
        ]),

        dict(h="O que esta página ensina para o resto do site", tipo="li", corpo=[
            "<strong>Quatorze anos, 64.641 artigos, 67 ensaios clínicos, 1 produto aprovado.</strong> Essa é a "
            "escala real de uma tecnologia que funcionou. Qualquer composto desta referência que prometa efeito "
            "comparável com uma fração dessa evidência está prometendo a partir do nada.",
            "<strong>A evidência que convence uma agência é de outra ordem.</strong> Dois ensaios de fase 3, "
            "96 pacientes somados, seguimento de até 48 meses, enxertia documentada em todos, e ainda assim a "
            "aprovação europeia saiu <em>condicional</em> e o Reino Unido só liberou com coleta de dados "
            "continuada. Compare com “doses relatadas por usuários em fórum”.",
            "<strong>O efeito adverso mais grave costuma vir do procedimento, não da molécula.</strong> Aqui é o "
            "bussulfano, não o CRISPR. Vale como lente para ler qualquer relato de dano: a pergunta é sempre o que "
            "mais estava sendo feito ao mesmo tempo.",
            "<strong>“Nenhum evento adverso grave” tem prazo de validade.</strong> Os estudos de longo prazo desta "
            "terapia terminam em 2039 e 2040. Um composto que existe há três anos e “não deu problema em ninguém” "
            "não disse absolutamente nada.",
            "<strong>E aprovação em outro país não é aprovação aqui.</strong> Três agências aprovaram o Casgevy. "
            "No Brasil não há registro, não há petição, não há ensaio. A distância entre “existe no mundo” e "
            "“existe legalmente para você” é exatamente o assunto do resto desta referência.",
        ]),
    ],

    referencias=[
        ("Jinek M et al., 2012 — uma endonuclease de DNA programável por RNA duplo na imunidade bacteriana adaptativa. É o artigo do Nobel. Science 337(6096):816-821.",
         "https://doi.org/10.1126/science.1225829"),
        ("Ishino Y et al., 1987 — sequência do gene iap em E. coli. Primeira observação publicada das repetições, sem função conhecida. J Bacteriol 169(12):5429-5433.",
         "https://doi.org/10.1128/jb.169.12.5429-5433.1987"),
        ("Mojica FJM et al., 2005 — as sequências intercalares derivam de elementos genéticos externos. J Mol Evol 60(2):174-182.",
         "https://doi.org/10.1007/s00239-004-0046-3"),
        ("Barrangou R et al., 2007 — CRISPR confere resistência adquirida contra vírus em procariotos. Trabalho feito na Danisco. Science 315(5819):1709-1712.",
         "https://doi.org/10.1126/science.1138140"),
        ("Deltcheva E et al., 2011 — maturação do RNA CRISPR por RNA pequeno codificado em trans e RNase III do hospedeiro. Nature 471(7340):602-607.",
         "https://doi.org/10.1038/nature09886"),
        ("Cong L et al., 2013 — engenharia genômica múltipla usando sistemas CRISPR/Cas. Science 339(6121):819-823.",
         "https://doi.org/10.1126/science.1231143"),
        ("Mali P et al., 2013 — engenharia do genoma humano guiada por RNA via Cas9. Publicado no mesmo número. Science 339(6121):823-826.",
         "https://doi.org/10.1126/science.1232033"),
        ("Komor AC et al., 2016 — edição programável de uma base no DNA genômico sem clivagem da dupla-fita. Nature 533(7603):420-424.",
         "https://doi.org/10.1038/nature17946"),
        ("Gaudelli NM et al., 2017 — edição programável de base A•T para G•C sem clivagem do DNA. Nature 551(7681):464-471.",
         "https://doi.org/10.1038/nature24644"),
        ("Anzalone AV et al., 2019 — prime editing: edição de genoma por busca e substituição, sem quebras de dupla-fita nem DNA doador. Nature 576(7785):149-157.",
         "https://doi.org/10.1038/s41586-019-1711-4"),
        ("Frangoul H et al., 2024 — exagamglogene autotemcel para doença falciforme grave. Fase 3, 44 pacientes. N Engl J Med 390(18):1649-1662.",
         "https://doi.org/10.1056/NEJMoa2309676"),
        ("Locatelli F et al., 2024 — exagamglogene autotemcel para beta-talassemia dependente de transfusão. Fase 3, 52 pacientes. N Engl J Med 390(18):1663-1676.",
         "https://doi.org/10.1056/NEJMoa2309673"),
        ("Frangoul H et al., 2021 — edição CRISPR-Cas9 para doença falciforme e beta-talassemia. Os dois primeiros pacientes. N Engl J Med 384(3):252-260.",
         "https://doi.org/10.1056/NEJMoa2031054"),
        ("Kosicki M et al., 2018 — o reparo das quebras induzidas por CRISPR-Cas9 leva a deleções grandes e rearranjos complexos. Nat Biotechnol 36(8):765-771.",
         "https://doi.org/10.1038/nbt.4192"),
        ("Haapaniemi E et al., 2018 — a edição por CRISPR-Cas9 induz resposta de dano ao DNA mediada por p53. Nat Med 24(7):927-930.",
         "https://doi.org/10.1038/s41591-018-0049-z"),
        ("Ihry RJ et al., 2018 — o p53 inibe a engenharia por CRISPR-Cas9 em células-tronco pluripotentes humanas. Nat Med 24(7):939-946.",
         "https://doi.org/10.1038/s41591-018-0050-6"),
        ("Leibowitz ML et al., 2021 — cromotripse como consequência no alvo da edição por CRISPR-Cas9. Nat Genet 53(6):895-905.",
         "https://doi.org/10.1038/s41588-021-00838-7"),
        ("Cohn DM et al., 2026 — lonvoguran ziclumeran: edição CRISPR in vivo no angioedema hereditário. Fase 3 controlada por placebo, 80 pacientes. N Engl J Med.",
         "https://doi.org/10.1056/NEJMoa2600931"),
        ("Cohn DM et al., 2025 — terapia baseada em CRISPR para angioedema hereditário. Fase 2 randomizada, 27 pacientes. N Engl J Med 392(5):458-467.",
         "https://doi.org/10.1056/NEJMoa2405734"),
        ("Gillmore JD et al., 2021 — edição gênica CRISPR-Cas9 in vivo para amiloidose por transtirretina. Primeiro ensaio in vivo publicado. N Engl J Med 385(6):493-502.",
         "https://doi.org/10.1056/NEJMoa2107454"),
        ("Fontana M et al., 2024 — nexiguran ziclumeran na cardiomiopatia por amiloidose ATTR. Fase 1, 36 pacientes. N Engl J Med 391(23):2231-2241.",
         "https://doi.org/10.1056/NEJMoa2412309"),
        ("Musunuru K et al., 2025 — edição gênica in vivo específica para um paciente, no tratamento de uma doença genética rara. Relato de caso, n=1. N Engl J Med 392(22):2235-2243.",
         "https://doi.org/10.1056/NEJMoa2504747"),
        ("Hmaidan S et al., 2025 — segurança, viabilidade e desfechos de preservação de fertilidade em pacientes com doença falciforme e beta-talassemia submetidos a terapia gênica. 40 pacientes. Transplant Cell Ther.",
         "https://doi.org/10.1016/j.jtct.2025.08.004"),
        ("Chetlapalli K et al., 2026 — transplante haploidêntico, terapia gênica e padrão de cuidado na doença falciforme: análise de custo-efetividade. Blood.",
         "https://doi.org/10.1182/blood.2025032290"),
        ("GBD 2021 Sickle Cell Disease Collaborators, 2023 — prevalência global, regional e nacional e carga de mortalidade da doença falciforme, 2000-2021. Lancet Haematol 10(8):e585-e599.",
         "https://doi.org/10.1016/S2352-3026(23)00118-7"),
        ("MHRA — autorização mundial inédita de terapia gênica para doença falciforme e beta-talassemia dependente de transfusão, 15 de novembro de 2023.",
         "https://www.gov.uk/government/news/mhra-authorises-world-first-gene-therapy-that-aims-to-cure-sickle-cell-disease-and-transfusion-dependent-thalassemia"),
        ("FDA — página do produto CASGEVY, com as datas de aprovação e de cada suplemento.",
         "https://www.fda.gov/vaccines-blood-biologics/casgevy"),
        ("FDA — aprovação da primeira terapia gênica para crianças pequenas com doença falciforme, 1º de julho de 2026.",
         "https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapy-young-children-sickle-cell-disease"),
        ("EMA — relatório público de avaliação do Casgevy, com a data e o tipo da autorização europeia.",
         "https://www.ema.europa.eu/en/medicines/human/EPAR/casgevy"),
        ("NICE — orientação TA1044, exagamglogene autotemcel para doença falciforme grave. Traz o preço de lista, o sigilo do desconto e o funil de elegibilidade.",
         "https://www.nice.org.uk/guidance/ta1044"),
        ("NICE — orientação TA1003, exagamglogene autotemcel para beta-talassemia dependente de transfusão.",
         "https://www.nice.org.uk/guidance/ta1003"),
        ("OMS — recomendações sobre edição do genoma humano, publicadas em 12 de julho de 2021.",
         "https://www.who.int/news/item/12-07-2021-who-issues-new-recommendations-on-human-genome-editing-for-the-advancement-of-public-health"),
        ("Greely HT, 2019 — bebês editados: edição germinativa do genoma humano no caso He Jiankui. J Law Biosci 6(1):111-183.",
         "https://doi.org/10.1093/jlb/lsz010"),
        ("Decreto nº 7.646, de 21 de dezembro de 2011 — artigo 15: o pedido de incorporação ao SUS exige o número e a validade do registro na ANVISA.",
         "https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/decreto/d7646.htm"),
        ("CONITEC — Relatório de Recomendação nº 924, Protocolo Clínico e Diretrizes Terapêuticas da Doença Falciforme, 2024. Fonte da epidemiologia brasileira citada.",
         "https://www.gov.br/conitec/pt-br/midias/relatorios/2024/relatorio-de-recomendacao-no-924-protocolo-clinico-e-diretrizes-terapeuticas-doenca-falciforme/@@display-file/file"),
        (f"ANVISA — base pública de petições, sistema “Situação de Documentos”. Consultas por código de assunto (11586, 11587, 11614, 11615) e por CNPJ, feitas em {_DT}.",
         "https://consultas.anvisa.gov.br/"),
    ],
),
}
