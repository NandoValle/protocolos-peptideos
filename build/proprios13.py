# -*- coding: utf-8 -*-
"""Casgevy: preco e acesso.

Segunda metade de proprios12 (CRISPR). Aquela pagina trata da ciencia e da
eficacia; esta trata do que acontece depois da aprovacao regulatoria.

Fontes: orientacoes TA1003 e TA1044 do NICE, incluindo os relatorios de
impacto de recursos; paginas oficiais do CMS; PubMed; relatorio oficial da
CONITEC; Decreto 7.646/2011; e a base publica de peticoes da ANVISA.

A secao de adocao real e a mais fraca da pagina e esta marcada como tal:
depende de comunicado da fabricante reproduzido por imprensa setorial.
"""

from datas import DATA_APURACAO as _DT

CASGEVY = {
"proprio_casgevy": dict(
    titulo="Casgevy — preço e acesso",
    nota_refs=("Cada cifra foi lida na publicação oficial da agência ou no resumo do artigo indicado, em "
               f"{_DT}. Onde a fonte é imprensa setorial ou comunicado de empresa, isso está dito na própria "
               "linha do texto."),
    secoes=[

        dict(h="O que esta página responde", tipo="p", corpo=[
            "A página de <a href=\"proprio_crispr.html\">CRISPR</a> mostra que a tecnologia funcionou: a edição "
            "pegou em 100% dos pacientes nos dois ensaios de fase 3, e 97% ficaram livres de crise vaso-oclusiva. "
            "Esta página começa onde aquela para. <strong>Funcionar e chegar são coisas diferentes</strong>, e a "
            "distância entre as duas é o assunto daqui.",
            "O resultado curto, e ele não é o que se espera: <strong>o gargalo declarado não é o preço</strong>. "
            "Quando o avaliador britânico explica por que projeta adesão baixa, ele não cita custo. Cita a "
            "internação.",
        ]),

        dict(h="O preço, nas duas moedas em que ele é público", tipo="p", corpo=[
            "O preço britânico está declarado em texto idêntico nas duas orientações do NICE — a da beta-talassemia, "
            "publicada em 11 de setembro de 2024, e a da doença falciforme, publicada em 26 de fevereiro de 2025.",
        ], tabela=dict(
            cap="Preço de lista do Casgevy",
            linhas=[
                ["Mercado", "Preço de lista", "O que se sabe do preço real"],
                ["Reino Unido", "<strong>£1.651.000</strong> por curso de tratamento, dose única — o mesmo nas "
                                "duas indicações",
                 "A empresa tem acordo comercial que dá desconto ao NHS. <strong>O tamanho do desconto é sigilo "
                 "comercial</strong>, declarado como tal pelo próprio NICE"],
                ["Estados Unidos", "<strong>US$ 2,2 milhões</strong> (preço de tabela, <em>wholesale acquisition "
                                   "cost</em>)",
                 "Preço antes de descontos e reembolsos. O concorrente lentiviral, lovotibeglogene autotemcel, "
                 "está em US$ 3,1 milhões"],
                ["Brasil", "não existe",
                 "Sem registro e sem pedido de registro. Ver a seção do Brasil, adiante"],
            ])),

        dict(h="O preço foi fixado acima do teto que o avaliador independente calculou", tipo="p", corpo=[
            "Antes da aprovação pela FDA e antes de qualquer preço anunciado, o instituto americano de avaliação de "
            "tecnologias em saúde publicou uma faixa de referência para o exa-cel e para o concorrente: "
            "<strong>US$ 1,35 a 2,05 milhões</strong>. É a faixa que o instituto descreve como o maior preço que um "
            "fabricante deveria cobrar antes que o custo passe a causar perda de saúde desproporcional em outros "
            "pacientes do mesmo sistema.",
            "O preço saiu em <strong>US$ 2,2 milhões</strong> — acima do topo dessa faixa.",
            "A ressalva importa: a faixa foi calculada <em>antes</em> do preço existir. É a comparação de uma "
            "estimativa prévia com um número posterior, não um julgamento do instituto sobre o preço final.",
        ]),

        dict(h="O funil de elegibilidade, com cada porcentagem exposta", tipo="p", corpo=[
            "O NICE publica a conta inteira. Vale seguir passo a passo, porque é aqui que “aprovado para doença "
            "falciforme” vira <strong>78 pessoas por ano</strong>.",
        ], tabela=dict(
            cap="Doença falciforme na Inglaterra — do total de pacientes ao número tratado",
            linhas=[
                ["Filtro", "Proporção que passa"],
                ["Têm genótipo βS/βS, βS/β+ ou βS/β0", "~70%"],
                ["Desses, tiveram ≥2 crises vaso-oclusivas por ano nos 2 anos anteriores", "48%"],
                ["Desses, estão aptos ao procedimento", "54%"],
                ["Desses, <strong>não têm doador aparentado com compatibilidade HLA</strong>", "85%"],
                ["<strong>= pessoas elegíveis (2025-26)</strong>",
                 "<strong>1.794</strong>, crescendo para 1.882 em 2029-30"],
            ])),

        dict(h="E do elegível para o tratado", tipo="p", corpo=[
            "A tabela seguinte é do mesmo relatório. A última linha é a que importa.",
        ], tabela=dict(
            cap="Projeção do NICE — doença falciforme, Inglaterra",
            linhas=[
                ["", "2025-26", "2026-27", "2027-28", "2028-29", "2029-30"],
                ["Selecionados para tratar (intenção de tratar)", "29", "72", "90", "96", "96"],
                ["Proporção que conclui o tratamento", "81%", "81%", "81%", "81%", "81%"],
                ["<strong>Concluem o tratamento</strong>", "<strong>23</strong>", "<strong>58</strong>",
                 "<strong>73</strong>", "<strong>78</strong>", "<strong>78</strong>"],
            ])),

        dict(h="O motivo que o NICE dá, e que ninguém repete", tipo="li", corpo=[
            "<strong>Ele não cita preço.</strong> A justificativa registrada para a adesão baixa é que "
            "“uma internação hospitalar longa é necessária para o processo envolvido”. O produto está pago, "
            "aprovado e disponível — e ainda assim são 23 pessoas no primeiro ano, de 1.794 elegíveis.",
            "<strong>Na beta-talassemia o quadro é o mesmo, em escala menor.</strong> São 475 elegíveis na prática "
            "atual, chegando a 498 em 2028-29, com participação de mercado projetada de 3% no primeiro ano subindo "
            "a 11% em cinco anos: <strong>14 pessoas tratadas no primeiro ano, 10 por ano depois</strong>.",
            "<strong>Repare no filtro do doador.</strong> A autorização exige que o transplante seja apropriado "
            "<em>e</em> que não haja doador aparentado compatível. O Casgevy não é alternativa ao transplante: é o "
            "que se oferece a quem já era candidato e não achou doador. A indicação foi desenhada dentro do nicho "
            "que o transplante deixou vazio — e isso volta a importar duas seções adiante.",
        ]),

        dict(h="Reino Unido: “acesso gerenciado” é uma forma educada de dizer que ainda não se sabe", tipo="p", corpo=[
            "Nas duas indicações, o NICE <strong>não recomendou para uso de rotina no NHS</strong>. Recomendou com "
            "acesso gerenciado — regime provisório de coleta de dados enquanto a incerteza não se resolve. A "
            "expressão que ele usa para as estimativas de custo-efetividade é “altamente incertas”.",
            "Na beta-talassemia a formulação é direta: algumas das estimativas mais prováveis estão <strong>acima "
            "do que o NICE normalmente considera uso aceitável de recursos do NHS</strong>, mesmo levando em conta "
            "o impacto sobre desigualdades em saúde. Por isso, não recomendado para rotina.",
            "Na doença falciforme, o NICE aceitou explicitamente <strong>mais incerteza e uma estimativa de "
            "custo-efetividade mais alta do que normalmente aceitaria</strong>, e nomeia os três motivos: as "
            "desigualdades em saúde enfrentadas por pessoas com a doença, o caráter inovador da tecnologia, e "
            "benefícios não capturados na qualidade de vida dos cuidadores.",
            "Em termos frios: <strong>o NHS pagou um prêmio de equidade e escreveu isso.</strong> Reconheceu que a "
            "população com doença falciforme é sistematicamente desassistida e ajustou o limiar por causa disso. É "
            "uma decisão defensável e explícita — e é também o reconhecimento formal de que, pelo critério "
            "econômico puro, o produto não passava.",
            "As incertezas que ele lista nas duas orientações são de fundo, não de detalhe: estrutura do modelo, "
            "desfechos de sobrevida e qualidade de vida, <strong>quanto tempo dura o efeito do tratamento</strong>, "
            "com que frequência as pessoas desistem antes da infusão, e a frequência de complicações.",
        ]),

        dict(h="Estados Unidos: um modelo federal desenhado para este problema", tipo="p", corpo=[
            "A doença falciforme, nos Estados Unidos, é desproporcionalmente uma doença de população coberta pelo "
            "Medicaid — seguro público, orçamento estadual. Um preço de US$ 2,2 milhões cai sobre orçamentos que "
            "não têm como absorvê-lo.",
            "A resposta foi criar um modelo em que o <strong>próprio governo federal negocia acordos baseados em "
            "desfecho</strong> com os fabricantes, em nome dos estados: os estados participantes recebem descontos "
            "e reembolsos garantidos <strong>caso a terapia não entregue o benefício prometido</strong>.",
            "Em anúncio de <strong>15 de julho de 2025</strong>: 33 estados, mais o Distrito de Colúmbia e Porto "
            "Rico, aderiram. O órgão federal afirma que <strong>84% dos beneficiários do Medicaid com doença "
            "falciforme</strong> residem em estados participantes.",
            "Mas há a conta, e ela é dura. Análise da perspectiva do Medicaid do Colorado, com dados reais de 2018 "
            "a 2023:",
        ], tabela=dict(
            cap="O que o Medicaid do Colorado gasta, e o que gastaria",
            linhas=[
                ["Medida", "Valor"],
                ["Custo médio anual do <strong>padrão de cuidado</strong> para falciforme grave (138 pacientes)",
                 "<strong>US$ 45.941</strong> por ano (desvio-padrão US$ 59.653)"],
                ["Saldo cumulativo em <strong>6 anos de contrato</strong>, com preço de lista, comparado ao padrão "
                 "de cuidado — exa-cel", "<strong>−US$ 2,11 milhões</strong> por paciente"],
                ["O mesmo, para o concorrente lentiviral", "<strong>−US$ 3,00 milhões</strong> por paciente"],
            ])),

        dict(h="O que essa conta significa", tipo="li", corpo=[
            "<strong>Dentro do horizonte de um contrato de pagador, a terapia não se paga.</strong> O padrão de "
            "cuidado custa cerca de US$ 46 mil por ano; a terapia custa o equivalente a 48 anos desse padrão, "
            "adiantados de uma vez.",
            "<strong>E quem adianta não é necessariamente quem colhe.</strong> Qualquer argumento de “economiza a "
            "longo prazo” tem que atravessar essa lacuna de caixa — e, nos Estados Unidos, pacientes trocam de "
            "plano. O pagador que financia a cura pode não ser o que deixa de pagar as internações evitadas.",
        ]),

        dict(h="O comparador que a discussão evitou", tipo="p", corpo=[
            "Esta é a peça mais dura do levantamento, e é de 2026. Uma análise de custo-efetividade publicada em "
            "<em>Blood</em> comparou três estratégias em adultos e crianças com doença falciforme: padrão de "
            "cuidado, <strong>transplante alogênico haploidêntico com condicionamento não-mieloablativo</strong> — "
            "aquele em que o doador é meio-compatível, um pai, uma mãe, um irmão — e terapia gênica.",
        ], tabela=dict(
            cap="Três estratégias, mesma população",
            linhas=[
                ["Estratégia", "Anos de vida ajustados por qualidade", "Custo"],
                ["Padrão de cuidado", "14,3", "US$ 1,22 milhão"],
                ["<strong>Transplante haploidêntico</strong>", "<strong>20,1</strong>",
                 "<strong>US$ 1,15 milhão</strong>"],
                ["Terapia gênica", "22,1", "US$ 2,75 milhões"],
                ["<strong>Resultado da comparação</strong>",
                 "O transplante haploidêntico foi a estratégia custo-efetiva contra a terapia gênica em "
                 "<strong>100% de 10.000 iterações de Monte Carlo</strong>, no caso-base e em <strong>todas</strong> "
                 "as análises de cenário", ""],
                ["<strong>Preço máximo custo-efetivo da terapia gênica</strong> contra o padrão de cuidado",
                 "<strong>US$ 1,4 milhão</strong> nos Estados Unidos",
                 "<strong>US$ 4.200 a US$ 22.000</strong> na Índia, Nigéria e Tanzânia, conforme o limiar de "
                 "disposição a pagar"],
            ])),

        dict(h="Três leituras, com o cuidado que o dado exige", tipo="li", corpo=[
            "<strong>A terapia gênica ganha em anos de vida ajustados por qualidade</strong> — 22,1 contra 20,1. O "
            "transplante haploidêntico não é clinicamente melhor. É <em>mais barato o suficiente</em> para vencer "
            "a comparação econômica com folga esmagadora.",
            "<strong>E ele ataca justamente o nicho da indicação.</strong> O Casgevy é aprovado para quem não tem "
            "doador aparentado com compatibilidade HLA — e o haploidêntico é exatamente a técnica que dispensa "
            "compatibilidade total. Se ele amadurecer como opção de rotina, a indicação do Casgevy "
            "<strong>encolhe por dentro</strong>.",
            "<strong>US$ 4.200 na Nigéria.</strong> O preço de lista americano é <strong>520 vezes</strong> esse "
            "teto. Não é questão de negociar desconto: é diferença de ordem de grandeza que nenhum acordo "
            "comercial fecha.",
        ]),

        dict(h="Onde estão os pacientes, e onde está a terapia", tipo="p", corpo=[
            "Estudo de Carga Global de Doença, 204 países e territórios, série de 2000 a 2021.",
        ], tabela=dict(
            cap="Doença falciforme no mundo, 2021",
            linhas=[
                ["Medida", "Valor"],
                ["Nascimentos de bebês com a doença, por ano",
                 "<strong>515.000</strong> (425.000–614.000) — alta de 13,7% desde 2000, puxada pelo crescimento "
                 "populacional no <strong>Caribe e na África subsaariana ocidental e central</strong>"],
                ["Pessoas vivendo com a doença",
                 "<strong>7,74 milhões</strong> (6,51–9,2) — alta de <strong>41,4%</strong> desde 2000"],
                ["Mortes atribuídas por causa específica", "34.400 (25.000–45.200)"],
                ["<strong>Carga total de mortalidade</strong> atribuível",
                 "<strong>376.000</strong> (303.000–467.000) — quase <strong>11 vezes</strong> a contagem por "
                 "causa específica"],
                ["Mortes em menores de 5 anos", "<strong>81.100</strong> (58.800–108.000)"],
                ["Posição entre todas as causas de morte estimadas",
                 "sobe da <strong>40ª</strong> para a <strong>12ª</strong> quando se conta a carga total em vez da "
                 "causa específica"],
            ])),

        dict(h="As duas metades, lado a lado", tipo="li", corpo=[
            "<strong>515.000 nascimentos por ano</strong>, majoritariamente na África subsaariana e no Caribe.",
            "<strong>78 pessoas por ano</strong> tratadas na Inglaterra, no cenário de pico projetado pelo NICE.",
            "<strong>Teto custo-efetivo estimado na Nigéria: US$ 4.200. Preço de lista: US$ 2,2 milhões.</strong>",
            "A doença falciforme é, por origem evolutiva, uma doença de populações de regiões com malária "
            "endêmica. A primeira terapia CRISPR do mundo foi aprovada para ela — e o preço foi fixado num patamar "
            "que exclui, por construção, os países onde nasce a esmagadora maioria dos pacientes. "
            "<strong>Não é acidente de mercado: é o resultado previsível do modelo de desenvolvimento.</strong>",
        ]),

        dict(h="Existe proposta técnica para mudar isso", tipo="p", corpo=[
            "Uma força-tarefa multidisciplinar publicou na <em>Nature</em>, em 2024, um roteiro para medicamentos "
            "genéticos acessíveis. A proposta central é uma estrutura de precificação que, segundo os autores, "
            "poderia <strong>reduzir o custo por paciente em dez vezes</strong>, somada a um modelo de negócio que "
            "distribui responsabilidades entre fontes de financiamento diversas, provisões de licenciamento "
            "acadêmico, inovação de manufatura e regulação de apoio.",
            "O argumento de fundo é factual e verificável: <strong>todas as terapias celulares e gênicas aprovadas "
            "nasceram em instituições acadêmicas ou governamentais</strong>. A dependência de empresas com fins "
            "lucrativos para o desenvolvimento posterior é o que produz preços calibrados para recuperar "
            "investimento, pagar pelos candidatos que falharam e atender expectativas de acionistas — e é isso, "
            "não o custo de fabricação, que os autores identificam como origem do patamar de preço da categoria.",
        ]),

        dict(h="O preço que não é cobrado em dinheiro", tipo="p", corpo=[
            "Está detalhado na página de <a href=\"proprio_crispr.html\">CRISPR</a>, mas precisa ser lembrado "
            "aqui, porque é parte do custo de acesso e não aparece em nenhuma tabela de preço.",
            "O condicionamento com bussulfano é gonadotóxico. Numa experiência de centro único com 40 pacientes "
            "submetidos a terapia gênica, <strong>as 17 mulheres com mais de um ano de seguimento apresentaram, "
            "todas, falência ovariana</strong>, com hormônio antimülleriano indetectável.",
            "Isso significa que o acesso real ao Casgevy pressupõe acesso prévio a um serviço de preservação de "
            "fertilidade — mais um procedimento, mais custo, mais tempo, e mais um serviço especializado que "
            "precisa existir na cidade da paciente. <strong>Também é acesso.</strong>",
        ]),

        dict(h="No Brasil: não é fila lenta, é fila não iniciada", tipo="p", corpo=[
            f"Consulta em {_DT} à base pública de petições da ANVISA — o sistema “Situação de Documentos”, que "
            "permite filtrar por CNPJ e por código de assunto.",
            "Terapia gênica e celular não entra no cadastro de medicamentos: é <strong>Produto de Terapia "
            "Avançada</strong>, com registro separado sob a RDC 505 de 2021. Buscar “exagamglogene” na base aberta "
            "de medicamentos devolve zero, e isso não significa nada — é a base errada.",
            "O universo completo de pedidos de registro de terapia avançada já protocolados na Agência, somando os "
            "quatro códigos de assunto que existem para isso, são <strong>12 petições, de 9 empresas</strong>. "
            "Estas são as 11 da Classe II:",
        ], tabela=dict(
            cap="Todos os pedidos de registro de Produto de Terapia Avançada Classe II na ANVISA",
            linhas=[
                ["Empresa", "Situação", "Processo"],
                ["Novartis Biociências", "Publicado deferimento", "25351530600202181"],
                ["Novartis Biociências", "Publicado deferimento", "25351520073201982"],
                ["Novartis Biociências", "Publicado deferimento", "25351030622202065"],
                ["PTC Farmacêutica do Brasil", "Publicado deferimento", "25351475925202356"],
                ["Janssen-Cilag Farmacêutica", "Publicado deferimento", "25351406211202136"],
                ["Gilead Sciences Farmacêutica do Brasil", "Publicado deferimento", "25351087303202374"],
                ["Gilead Sciences Farmacêutica do Brasil", "Publicado deferimento", "25351068316202263"],
                ["BioMarin Brasil Farmacêutica", "<strong>Cancelado</strong>", "25351322541202331"],
                ["Bristol-Myers Squibb Farmacêutica", "<strong>Em análise</strong>", "25351134682202641"],
                ["Laboratórios Ferring", "<strong>Em análise do cumprimento de exigência</strong>",
                 "25351069176202593"],
                ["Ultragenyx Brasil Farmacêutica", "<strong>Em exigência</strong>", "25351029768202653"],
            ])),

        dict(h="A varredura que fecha a pergunta", tipo="p", corpo=[
            "Nenhuma das 12 é da Vertex, detentora do Casgevy. Para eliminar a hipótese de a petição estar sob "
            "outro código de assunto, a varredura foi refeita por CNPJ.",
            "A <strong>Vertex Farmacêutica do Brasil</strong> — identificada pelo CNPJ que consta como detentora "
            "dos registros de Trikafta, Symdeko, Orkambi e Kalydeco, todos medicamentos de fibrose cística — tem "
            "541 petições no sistema da ANVISA. Todas foram baixadas e classificadas por assunto.",
        ], tabela=dict(
            cap="Tudo o que a Vertex já protocolou no Brasil",
            linhas=[
                ["Recorte", "Petições"],
                ["Total no sistema da ANVISA", "<strong>541</strong>"],
                ["Com assunto de <strong>Produto de Terapia Avançada</strong>", "<strong>0</strong>"],
                ["De terapia gênica, celular avançada ou engenharia tecidual", "<strong>0</strong>"],
                ["De <strong>ensaio clínico</strong> com produto de terapia avançada", "<strong>0</strong>"],
                ["De uso compassivo ou acesso expandido com produto de terapia avançada", "<strong>0</strong>"],
            ])),

        dict(h="O que isso significa para o SUS", tipo="li", corpo=[
            "<strong>Não existe pedido de registro do Casgevy no Brasil</strong>, e não existe nem pedido de "
            "ensaio clínico. Não é caso de “está na fila e demora”: não entrou na fila.",
            "<strong>As fontes em português que afirmam aprovação da ANVISA “no início de 2024” estão erradas.</strong> "
            "Agora isso se afirma por evidência positiva, não por ausência de prova.",
            "<strong>Sem registro, a comissão de incorporação não pode nem avaliar.</strong> O Decreto 7.646/2011, "
            "no artigo 15, exige que o pedido de incorporação ao SUS instrua o processo com o número e a validade "
            "do registro na ANVISA, além de evidência científica, avaliação econômica comparativa e o preço "
            "fixado pela câmara de regulação. <strong>O debate brasileiro sobre preço do Casgevy não está travado "
            "no preço — está travado três degraus antes.</strong>",
            "<strong>O que não foi verificado:</strong> se alguma petição foi protocolada por outra pessoa "
            "jurídica em nome do produto. A consulta é por CNPJ e por código de assunto, e a interface pública não "
            "devolve nome comercial. A busca textual por “exagamglogene” exigiria a Pesquisa Pública do SEI, que "
            "pede CAPTCHA e não foi usada.",
        ]),

        dict(h="E, se um dia destravar, avaliaremos no escuro", tipo="p", corpo=[
            "O Relatório de Recomendação nº 924 da CONITEC, de 2024, que estabelece o protocolo clínico da doença "
            "falciforme no SUS, traz a epidemiologia oficial brasileira — e o buraco dentro dela.",
        ], tabela=dict(
            cap="O que o Ministério da Saúde sabe sobre a doença falciforme no Brasil",
            linhas=[
                ["Medida", "Valor oficial"],
                ["População com traço falciforme", "estima-se <strong>4%</strong>, com distribuição heterogênea "
                                                   "entre as regiões"],
                ["Recém-nascidos diagnosticados pelo Programa Nacional de Triagem Neonatal, de 2014 a 2018",
                 "<strong>5.428</strong>"],
                ["Cobertura do Teste do Pezinho na rede pública, em 2014",
                 "mais de <strong>84%</strong> dos nascidos vivos, em todos os estados"],
                ["<strong>Total de pessoas com a doença no país</strong>",
                 "“Dados recentes não foram identificados, mas <strong>em 2007</strong> estimava-se que "
                 "<strong>25.000 a 50.000</strong> pessoas” tinham a doença — citação textual do relatório de 2024"],
            ])),

        dict(h="O denominador que não existe", tipo="li", corpo=[
            "<strong>Em 2024, a melhor estimativa oficial disponível é de 2007</strong>, e varia por um fator de "
            "dois. O país tem triagem neonatal universal com 84% de cobertura há mais de uma década e não sabe "
            "dizer o tamanho da própria população de pacientes.",
            "<strong>Consequência prática:</strong> se e quando o Casgevy chegar à mesa da comissão de "
            "incorporação, a avaliação de impacto orçamentário será feita sobre um denominador de 17 anos atrás, "
            "com incerteza de 100%.",
            "<strong>Compare com o Reino Unido.</strong> Lá foi possível publicar 1.794 elegíveis com o funil "
            "inteiro exposto — genótipo, número de crises, aptidão ao procedimento, ausência de doador — porque se "
            "sabe quem são. <strong>A lacuna de acesso, aqui, começa como lacuna de dado.</strong>",
        ]),

        dict(h="Adoção real — a seção mais fraca desta página", tipo="p", corpo=[
            "⚠️ Não localizei registro público independente de quantos pacientes receberam Casgevy no mundo. O que "
            "existe é comunicado da fabricante e imprensa setorial que o reproduz. A página de investidores da "
            "empresa devolveu erro de acesso nas tentativas desta apuração. <strong>Nada nesta seção foi conferido "
            "em fonte primária.</strong>",
            "Segundo imprensa setorial citando a fabricante, até <strong>30 de junho de 2025</strong>: 115 "
            "pacientes tiveram a primeira coleta de células e <strong>29 foram infundidos</strong>, sendo 16 dessas "
            "infusões no segundo trimestre. A receita reportada de Casgevy em 2025 foi de US$ 115,8 milhões.",
            "Se a receita e o preço de lista estiverem ambos corretos, a divisão dá cerca de <strong>53 "
            "tratamentos</strong> — mesma ordem de grandeza dos 29 infundidos até meados do ano, e coerente com o "
            "que o NICE projetou de forma independente para a Inglaterra. <strong>É checagem de consistência, não "
            "confirmação.</strong>",
            "O que se pode dizer sem depender desses números: a distância entre 115 coletas e 29 infusões, se "
            "real, é da mesma natureza que os 81% de conclusão que o NICE projeta. <strong>Entrar no processo e "
            "terminá-lo são coisas diferentes</strong>, e a diferença é medida em meses de hospital.",
        ]),

        dict(h="O que este levantamento mostra", tipo="li", corpo=[
            "<strong>O gargalo declarado não é o preço — é a cama de hospital.</strong> Quando o NICE explica por "
            "que projeta adesão baixa, cita a internação longa, não o custo. Um país rico, com o produto pago e "
            "disponível, trata 23 pessoas no primeiro ano de 1.794 elegíveis.",
            "<strong>O preço foi fixado acima do teto que o avaliador independente calculou.</strong> US$ 1,35 a "
            "2,05 milhões era a faixa; US$ 2,2 milhões foi o preço.",
            "<strong>Dentro do horizonte de um contrato de pagador, a terapia não se paga.</strong> Padrão de "
            "cuidado a US$ 45.941 por ano; saldo cumulativo de −US$ 2,11 milhões por paciente em 6 anos.",
            "<strong>Existe um comparador mais barato que ganha em 10.000 de 10.000 simulações</strong> — e que "
            "ataca justamente o nicho da indicação, porque dispensa a compatibilidade HLA total que define esse "
            "nicho.",
            "<strong>O NHS pagou um prêmio de equidade e disse isso por escrito.</strong> Aceitou incerteza maior "
            "e custo-efetividade pior do que normalmente aceita, por causa das desigualdades em saúde que atingem "
            "pessoas com doença falciforme. É honesto — e é o reconhecimento de que, pelo critério econômico puro, "
            "o produto não passava.",
            "<strong>A distância entre onde estão os pacientes e onde está a terapia é de ordem de grandeza.</strong> "
            "515.000 nascimentos por ano contra 78 tratamentos anuais projetados na Inglaterra; teto custo-efetivo "
            "de US$ 4.200 na Nigéria contra preço de US$ 2,2 milhões.",
            "<strong>E há um custo humano que nenhuma tabela de preço mostra:</strong> 17 de 17 mulheres com mais "
            "de um ano de seguimento tiveram falência ovariana.",
            "<strong>No Brasil, a fila nem começou</strong> — 541 petições da Vertex, zero de terapia avançada — "
            "<strong>e o denominador não existe</strong>: a melhor estimativa oficial de quantos pacientes há no "
            "país é de 2007 e varia entre 25 mil e 50 mil.",
        ]),
    ],

    referencias=[
        ("NICE — orientação TA1044, exagamglogene autotemcel para doença falciforme grave em pessoas de 12 anos ou mais, publicada em 26 de fevereiro de 2025. Seção 2 traz o preço de lista e o sigilo do desconto; seção 1 traz a recomendação com acesso gerenciado e os motivos do prêmio de equidade.",
         "https://www.nice.org.uk/guidance/ta1044"),
        ("NICE — relatório de impacto de recursos da TA1044. Fonte do funil de elegibilidade, dos 1.794 elegíveis, da projeção ano a ano e da justificativa da adesão baixa pela internação longa.",
         "https://www.nice.org.uk/guidance/ta1044/resources/resource-impact-summary-15250971565/chapter/Resource-impact-summary-report"),
        ("NICE — orientação TA1003, exagamglogene autotemcel para beta-talassemia dependente de transfusão, publicada em 11 de setembro de 2024.",
         "https://www.nice.org.uk/guidance/ta1003"),
        ("NICE — relatório de impacto de recursos da TA1003. Fonte dos 475 elegíveis e da projeção de 14 tratamentos no primeiro ano.",
         "https://www.nice.org.uk/guidance/ta1003/resources/resource-impact-summary-report-13544709805/chapter/Resource-impact-summary-report"),
        ("ICER — avaliação de terapias gênicas para doença falciforme, 2023. Fonte da faixa de referência de preço de US$ 1,35 a 2,05 milhões, calculada antes da aprovação e antes de qualquer preço anunciado.",
         "https://icer.org/assessment/sickle-cell-disease-2023/"),
        ("Zemplenyi A et al., 2025 — modelos de pagamento para terapias gênicas de doença falciforme no Medicaid. Fonte do custo do padrão de cuidado no Colorado, do saldo cumulativo em 6 anos e dos preços de lista americanos. Pharmacoeconomics.",
         "https://doi.org/10.1007/s40273-025-01474-3"),
        ("CMS — modelo de acesso a terapias celulares e gênicas: 33 estados, Distrito de Colúmbia e Porto Rico, anunciados em 15 de julho de 2025, cobrindo 84% dos beneficiários do Medicaid com doença falciforme.",
         "https://www.cms.gov/innovation-insight-cms-model-delivers-access-sickle-cell-gene-therapy-expansive-list-state"),
        ("Chetlapalli K et al., 2026 — transplante haploidêntico, terapia gênica e padrão de cuidado na doença falciforme: análise de custo-efetividade. Fonte dos anos de vida ajustados por qualidade, dos custos das três estratégias, das 10.000 iterações e do teto de preço por país. Blood.",
         "https://doi.org/10.1182/blood.2025032290"),
        ("GBD 2021 Sickle Cell Disease Collaborators, 2023 — prevalência global, regional e nacional e carga de mortalidade da doença falciforme, 2000-2021. Lancet Haematol 10(8):e585-e599.",
         "https://doi.org/10.1016/S2352-3026(23)00118-7"),
        ("Kliegman M et al., 2024 — um roteiro para medicamentos genéticos acessíveis. Fonte da proposta de reduzir o custo por paciente em dez vezes. Nature.",
         "https://doi.org/10.1038/s41586-024-07800-7"),
        ("Hmaidan S et al., 2025 — segurança, viabilidade e desfechos de preservação de fertilidade em pacientes com doença falciforme e beta-talassemia submetidos a terapia gênica. Fonte das 17 de 17 com falência ovariana. Transplant Cell Ther.",
         "https://doi.org/10.1016/j.jtct.2025.08.004"),
        ("Decreto nº 7.646, de 21 de dezembro de 2011 — artigo 15: o pedido de incorporação ao SUS exige o número e a validade do registro na ANVISA, evidência científica, avaliação econômica comparativa e o preço fixado pela CMED.",
         "https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/decreto/d7646.htm"),
        ("CONITEC — Relatório de Recomendação nº 924, Protocolo Clínico e Diretrizes Terapêuticas da Doença Falciforme, 2024. Fonte dos 4% com traço falciforme, dos 5.428 recém-nascidos diagnosticados de 2014 a 2018, da cobertura de 84% da triagem neonatal e da citação sobre a ausência de dados recentes.",
         "https://www.gov.br/conitec/pt-br/midias/relatorios/2024/relatorio-de-recomendacao-no-924-protocolo-clinico-e-diretrizes-terapeuticas-doenca-falciforme/@@display-file/file"),
        (f"ANVISA — base pública de petições, sistema “Situação de Documentos”. Consultas por código de assunto (11586, 11587, 11614 e 11615) e por CNPJ da Vertex Farmacêutica do Brasil, feitas em {_DT}.",
         "https://consultas.anvisa.gov.br/"),
        ("ANVISA — base aberta de medicamentos, usada para identificar o CNPJ da Vertex Farmacêutica do Brasil pelos registros de Trikafta, Symdeko, Orkambi e Kalydeco.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
