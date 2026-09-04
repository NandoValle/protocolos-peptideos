# -*- coding: utf-8 -*-
"""Alcool e esteatose -- a lacuna que as tres paginas anteriores declararam.

A pagina hepatica termina dizendo que nao cobre alcool nem esteatose, e que os
dois sao causa muito mais frequente de exame alterado do que qualquer coisa
catalogada no site. Esta cobre.

Tres coisas fecham circuito com o resto do site: a nomenclatura mudou em 2023 e
criou uma categoria para quem tem as duas causas ao mesmo tempo; a interacao
entre alcool e disfuncao metabolica e supra-aditiva, nao somatoria; e os dois
medicamentos aprovados para MASH sao APROVACAO ACELERADA sobre biopsia -- o
mesmo desenho da pagina de doenca renal, agora no figado.
"""

from datas import DATA_APURACAO as _DT

ALCOOL = {

"proprio_alcool_esteatose": dict(
    titulo="Álcool e esteatose — a causa que ninguém mede antes de começar",
    nota_refs=(
        "As indicações e as ressalvas de cada medicamento foram extraídas por mim do endpoint de rótulos "
        f"da openFDA (<code>api.fda.gov/drug/label.json</code>) e das notas de aprovação da FDA, em {_DT}. "
        "A nomenclatura e os limiares de álcool vêm do consenso Delphi multissociedade publicado no "
        "<em>Journal of Hepatology</em>; a definição de dose padrão, do NIAAA; a posição sobre nível "
        "seguro, da Organização Mundial da Saúde."
    ),
    secoes=[

# ------------------------------------------------------------------ 0. porque
dict(h="A lacuna que as três páginas anteriores declararam", tipo="p", corpo=[
    "A página de <a href=\"proprio_dose_hepatica.html\">fígado</a> termina dizendo que não cobre "
    "álcool nem esteatose — e que os dois são, no mundo real, causa muito mais frequente de exame "
    "hepático alterado do que qualquer coisa catalogada neste site. Esta página fecha essa lacuna, e "
    "com ela o bloco de quatro: <a href=\"proprio_rim.html\">doença renal</a>, "
    "<a href=\"proprio_dose_renal.html\">dose renal</a>, fígado e agora a causa de base.",
    "A ordem em que essas páginas foram escritas inverte a ordem em que deveriam ser lidas. Ninguém "
    "precisa de tabela de ajuste por Child-Pugh antes de saber se já tem gordura no fígado. E "
    "praticamente ninguém que começa um ciclo de qualquer coisa mediu isso antes.",
    "Há um dado da FDA que dimensiona o problema: <strong>cerca de 6% dos adultos americanos — "
    "14,9 milhões de pessoas — têm MASH</strong>, a forma inflamatória da esteatose. Não é doença "
    "rara de livro. É a linha de base da população que este site atrai.",
]),

# ----------------------------------------------------------- 1. nomenclatura
dict(h="A nomenclatura mudou em 2023, e a mudança não é cosmética", tipo="p", corpo=[
    "Se você procurar \"esteatose hepática não alcoólica\" ou \"NAFLD\", vai achar literatura "
    "abundante e desatualizada no nome. Em 2023, um consenso Delphi multissociedade — reunindo a "
    "associação americana, a europeia e a latino-americana de estudo do fígado — trocou a "
    "terminologia inteira.",
    "O motivo é mais interessante que a troca. O nome antigo definia a doença pelo que ela "
    "<em>não</em> era: não alcoólica. Isso obrigava a excluir quem bebia — e criava um limbo para a "
    "maioria real das pessoas, que tem disfunção metabólica <strong>e</strong> bebe. A nova "
    "classificação parou de tratar as duas causas como excludentes.",
], tabela=dict(
    cap="Como a doença hepática esteatótica é classificada desde 2023",
    linhas=[
        ["Sigla", "Nome", "O que define"],
        ["SLD", "Doença hepática esteatótica",
         "Termo guarda-chuva: qualquer acúmulo de gordura no fígado, de qualquer causa"],
        ["<strong>MASLD</strong>", "Esteatose associada a disfunção metabólica",
         "Gordura no fígado + <strong>pelo menos um</strong> dos cinco fatores de risco "
         "cardiometabólico, sem outra causa identificável. Substituiu a sigla NAFLD"],
        ["<strong>MetALD</strong>", "Doença hepática metabólica e associada ao álcool",
         "<strong>A categoria nova.</strong> Quem tem os critérios de MASLD <em>e</em> bebe acima de "
         "uma faixa definida — sem chegar ao patamar da doença alcoólica pura"],
        ["ALD", "Doença hepática alcoólica",
         "Consumo acima da faixa do MetALD"],
        ["<strong>MASH</strong>", "Esteato-hepatite associada a disfunção metabólica",
         "A MASLD que já inflamou e começou a cicatrizar. Substituiu a sigla NASH"],
    ])),

# ------------------------------------------------------------- 2. os numeros
dict(h="Os números que definem o MetALD, e o que eles são em copos", tipo="p", corpo=[
    "O consenso fixou a faixa em gramas de álcool por semana: <strong>140 a 350 g para mulheres</strong> "
    "e <strong>210 a 420 g para homens</strong>. Grama de álcool não é unidade que alguém use no "
    "sábado à noite, então converto — declarando a conta, porque a conta é minha e não do consenso.",
    "O NIAAA define <strong>dose padrão como 14 g de álcool puro</strong>. Dividindo uma coisa pela "
    "outra:",
], tabela=dict(
    cap="Faixa do MetALD convertida em doses padrão de 14 g",
    linhas=[
        ["", "Gramas por semana (consenso)", "Doses padrão por semana (conta minha)"],
        ["Mulheres", "140 a 350 g", "<strong>10 a 25 doses</strong>"],
        ["Homens", "210 a 420 g", "<strong>15 a 30 doses</strong>"],
    ])),

dict(h="O que essa conversão revela", tipo="li", corpo=[
    "<strong>Quinze doses por semana são pouco mais de duas por dia.</strong> Para um homem com "
    "gordura no fígado e um fator de risco metabólico, é onde começa o MetALD — uma categoria "
    "diagnóstica, não um vício.",
    "<strong>A faixa é larga porque é uma zona de sobreposição, não um limite de segurança.</strong> "
    "Abaixo dela a classificação é MASLD; acima, doença alcoólica. O consenso está separando causas "
    "para fins de nomenclatura, e isso é diferente de dizer que 14 doses semanais não fazem mal.",
    "<strong>A dose padrão de 14 g é a americana.</strong> A Organização Mundial da Saúde e vários "
    "países usam 10 g, o que muda a contagem em 40%. Uma lata de cerveja comum de 350 mL a 5% tem "
    "cerca de 14 g; uma long neck de 355 mL, algo próximo disso. Quem conta por \"quantas cervejas\" "
    "erra para menos se o copo for grande ou a bebida for artesanal, que costuma ter teor alcoólico "
    "mais alto.",
]),

# --------------------------------------------------------- 3. supra-aditivo
dict(h="Álcool e gordura no fígado não somam — multiplicam", tipo="p", corpo=[
    "Este é o achado que justifica a categoria nova, e é o mais importante desta página.",
    "A literatura epidemiológica é consistente em descrever efeito <strong>supra-aditivo</strong> "
    "entre consumo de álcool e componentes da síndrome metabólica na progressão da doença hepática. "
    "Em bom português: quem tem os dois não corre a soma dos dois riscos, corre bem mais que isso. "
    "Coortes grandes na Itália, França, Escócia, China e Coreia do Sul mostraram que pessoas obesas "
    "que bebem têm risco <strong>2 a 3 vezes maior</strong> de desenvolver esteato-hepatite, com "
    "progressão acentuada para fibrose e cirrose. Um estudo populacional finlandês encontrou efeito "
    "supra-aditivo entre síndrome metabólica e binge semanal — definido como 60 g de etanol ou mais "
    "numa única ocasião, o equivalente a pouco mais de quatro doses.",
    "A consequência prática é desconfortável para quem gosta de contabilidade: <strong>a mesma "
    "quantidade de álcool não representa o mesmo risco em duas pessoas diferentes</strong>. Num "
    "fígado magro, quinze doses semanais são uma coisa; num fígado com esteatose e resistência à "
    "insulina, são outra. Não existe um número universal de doses seguras a ser descoberto — existe "
    "um número que depende do fígado que recebe.",
]),

dict(h="A posição da OMS sobre nível seguro, e o que ela de fato diz", tipo="p", corpo=[
    "Em 4 de janeiro de 2023, a Organização Mundial da Saúde publicou declaração no <em>The Lancet "
    "Public Health</em> afirmando que <strong>não existe quantidade segura de álcool que não afete a "
    "saúde</strong>. O argumento central é oncológico, não hepático: o álcool é classificado pela "
    "Agência Internacional de Pesquisa em Câncer como <strong>carcinógeno do Grupo 1</strong> — a "
    "categoria de maior evidência, a mesma do amianto, da radiação ionizante e do tabaco — e causa "
    "pelo menos sete tipos de câncer.",
    "O raciocínio declarado é que a evidência disponível <em>não permite identificar um limiar</em> "
    "abaixo do qual o efeito carcinogênico não se manifesta. Repare na formulação: é uma afirmação "
    "sobre o que não foi possível estabelecer, não a demonstração de que uma taça faz mal. É uma "
    "distinção que os dois lados do debate costumam atropelar, e que registro porque o site inteiro "
    "se apoia em ler o que a fonte de fato afirmou.",
    "Para o assunto desta página, porém, a discussão sobre a taça isolada é secundária. Quem já tem "
    "esteatose com fator de risco metabólico não está na zona cinzenta do debate populacional: está "
    "na população em que a interação é supra-aditiva e documentada.",
]),

# --------------------------------------------------------------- 4. medir
dict(h="Por que a enzima não vê isso", tipo="p", corpo=[
    "A página do fígado mostrou que uma hora de musculação altera AST e ALT por sete dias. O problema "
    "aqui é o inverso e pior: <strong>a esteatose e mesmo a fibrose avançada convivem com "
    "transaminase normal</strong>. Enzima é marcador de lesão em curso, não de cicatriz acumulada — "
    "e a esteatose é diagnosticada por imagem ou biópsia, não por sangue.",
    "É por isso que existe o <strong>FIB-4</strong>, índice que a associação americana de estudo do "
    "fígado reconhece como ferramenta de rastreio de fibrose avançada. Ele não é exame novo: é uma "
    "conta feita com quatro coisas que você provavelmente já tem no último check-up.",
], tabela=dict(
    cap="FIB-4 — a conta e o que cada faixa significa",
    linhas=[
        ["Item", "Detalhe"],
        ["Fórmula", "<code>(idade × AST) ÷ (plaquetas × √ALT)</code> — precisa de idade, AST (TGO), "
                    "ALT (TGP) e contagem de plaquetas"],
        ["Abaixo de 1,3",
         "Fibrose avançada improvável. Acompanhamento na atenção primária — a cada 1 a 2 anos com "
         "diabetes, pré-diabetes ou dois ou mais fatores de risco metabólico; a cada 2 a 3 anos sem eles"],
        ["De 1,3 a 2,67",
         "<strong>Zona indeterminada</strong>, que captura cerca de 30% das pessoas. Exige segundo "
         "exame — elastografia ou equivalente"],
        ["Acima de 2,67", "<strong>Fibrose avançada provável.</strong> Encaminhamento"],
        ["⚠️ Limites do índice",
         "Menos confiável <strong>abaixo dos 35</strong> e <strong>acima dos 65 anos</strong>. Para "
         "quem tem 65 ou mais, o corte muda: abaixo de 2,0 torna fibrose avançada improvável, e de "
         "2,0 a 2,67 exige exame adicional"],
    ])),

dict(h="A leitura honesta do FIB-4", tipo="li", corpo=[
    "<strong>Ele usa AST e ALT — então herda a armadilha da página anterior.</strong> Um FIB-4 "
    "calculado dois dias depois de treino pesado de pernas está contaminado. A coleta precisa dos "
    "mesmos cuidados: pelo menos uma semana sem treino de força intenso.",
    "<strong>É triagem, não diagnóstico.</strong> Abaixo de 1,3 ele afasta fibrose avançada com "
    "razoável segurança; acima de 2,67 ele sinaliza, não confirma. A zona do meio, que pega quase um "
    "terço das pessoas, não responde nada sozinha.",
    "<strong>Se você tem menos de 35 anos, ele vale pouco</strong> — e boa parte do público deste "
    "site está nessa faixa. Nesse caso a conversa é sobre imagem, não sobre índice.",
]),

# ------------------------------------------------------------ 5. tratamento
dict(h="O que existe de tratamento — e o círculo que isso fecha", tipo="p", corpo=[
    "Até 2024 não havia nenhum medicamento aprovado para MASH. Hoje há dois, e o desenho regulatório "
    "dos dois vai parecer familiar a quem leu a página de doença renal.",
], tabela=dict(
    cap="Os dois medicamentos aprovados para MASH",
    linhas=[
        ["Medicamento", "Aprovação", "Indicação exata", "Sobre que desfecho"],
        ["<strong>Rezdiffra</strong> (resmetirom) — agonista do receptor beta do hormônio tireoidiano",
         "14 de março de 2024 — <strong>acelerada</strong>. Primeiro medicamento aprovado para a doença",
         "MASH não cirrótica com fibrose moderada a avançada (estágios F2 a F3), junto de dieta e "
         "exercício. <strong>Evitar em cirrose descompensada</strong> e em Child-Pugh B ou C",
         "Melhora de MASH e de fibrose em biópsia, em ensaio com 888 pacientes. A manutenção do "
         "registro depende de ensaio confirmatório"],
        ["<strong>Wegovy</strong> (semaglutida) — agonista de GLP-1, já catalogado neste site",
         "15 de agosto de 2025 — <strong>acelerada</strong>",
         "MASH não cirrótica com fibrose moderada a avançada (F2 a F3), com dieta de calorias "
         "reduzidas e mais atividade física",
         "Ensaio ESSENCE, semana 72: resolução de MASH sem piora da fibrose em <strong>63%</strong> "
         "contra <strong>34%</strong> do placebo (534 e 266 pessoas); melhora de fibrose sem piora da "
         "esteato-hepatite em <strong>37%</strong> contra <strong>22%</strong>"],
    ])),

dict(h="O padrão que se repete, e por que ele importa aqui", tipo="p", corpo=[
    "Os dois foram aprovados por via acelerada, sobre um desfecho de <strong>biópsia</strong> — "
    "aparência do tecido — e não sobre o que interessa ao paciente, que é não morrer do fígado e não "
    "precisar de transplante. No caso do Wegovy, os estudos seguem <strong>até a semana 240</strong> "
    "justamente para verificar se a melhora na lâmina se traduz nisso.",
    "É exatamente a estrutura da página de doença renal, com a palavra trocada: lá o substituto era "
    "proteinúria, aqui é histologia. Vale a mesma leitura, e a mesma paciência: são fármacos com "
    "evidência real de que mexem no marcador, e ainda sem prova de que mudam o desfecho.",
    "E vale um registro que interessa a quem já usa GLP-1 por outro motivo: <strong>a indicação de "
    "MASH é do Wegovy e tem critério de fibrose F2 a F3, estabelecido por biópsia</strong>. Usar "
    "semaglutida para emagrecer não é a mesma coisa que estar tratando MASH, e nem toda gordura no "
    "fígado é MASH com fibrose.",
]),

# ------------------------------------------------------------ 6. na pratica
dict(h="O que fazer, na ordem", tipo="li", corpo=[
    "<strong>Antes de qualquer ciclo, saber se já existe gordura ali.</strong> Ultrassom de abdome é "
    "barato, sem radiação e amplamente disponível. É o exame que responde à pergunta que nenhum "
    "hepatograma responde.",
    "<strong>Calcule o FIB-4 com o que você já tem.</strong> Idade, AST, ALT e plaquetas estão em "
    "qualquer check-up. A conta leva trinta segundos e diz se a conversa seguinte é com o clínico ou "
    "com o hepatologista.",
    "<strong>Conte a bebida em gramas, uma vez na vida.</strong> Doses por semana × 14 g. O número "
    "costuma surpreender quem responde \"socialmente\" no consultório — e é o número que separa MASLD "
    "de MetALD no prontuário.",
    "<strong>Se há esteatose, o álcool deixa de ser questão de contabilidade.</strong> A interação é "
    "supra-aditiva: a mesma quantidade que seria pouco num fígado limpo não é pouco nesse.",
    "<strong>Não empilhe.</strong> Este site documenta, na página de <a href=\"proprio_dose_hepatica.html\">"
    "fígado</a>, lesão colestática por SARM com pico de bilirrubina relatado em 41,5 mg/dL. Somar "
    "isso a esteatose e a álcool é a combinação que aparece nas séries de casos.",
    "<strong>Perder peso continua sendo o que mais move o desfecho</strong>, e é o que as duas bulas "
    "aprovadas exigem em conjunto com o medicamento — as duas indicações dizem, com todas as letras, "
    "<em>junto de dieta e exercício</em>.",
]),

# ---------------------------------------------------------------- 7. limites
dict(h="O que esta página não é", tipo="li", corpo=[
    "<strong>Não é orientação sobre quanto beber.</strong> Os números do consenso são critério de "
    "classificação diagnóstica, não recomendação de consumo, e estão reproduzidos aqui com essa "
    "função.",
    "<strong>Não cobre hepatites virais, hemocromatose, doença de Wilson, hepatite autoimune</strong> "
    "nem as demais causas de esteatose e de enzima alterada — que precisam ser excluídas por quem "
    "avalia, e são justamente o que a definição de MASLD chama de \"outra causa identificável\".",
    "<strong>Não substitui imagem.</strong> Nenhum índice calculado, FIB-4 incluído, diagnostica "
    "esteatose. Ele estima probabilidade de fibrose, que é outra coisa.",
    "<strong>Não é sobre dependência.</strong> Se a pergunta é sobre conseguir parar, e não sobre "
    "quanto, a referência é outra e o profissional também.",
]),
    ],
    referencias=[
        ("FDA. FDA Approves Treatment for Serious Liver Disease Known as 'MASH' — Wegovy (semaglutida), aprovação acelerada de 15/08/2025, dados do ensaio ESSENCE",
         "https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-treatment-serious-liver-disease-known-mash"),
        ("FDA. FDA Approves First Treatment for Patients with Liver Scarring Due to Fatty Liver Disease — Rezdiffra (resmetirom), aprovação acelerada de 14/03/2024, ensaio com 888 pacientes",
         "https://www.fda.gov/news-events/press-announcements/fda-approves-first-treatment-patients-liver-scarring-due-fatty-liver-disease"),
        ("DailyMed — REZDIFFRA (resmetirom), rótulo completo: indicação, limitação de uso em cirrose descompensada e seção 8.7",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=REZDIFFRA"),
        ("DailyMed — WEGOVY (semaglutida), rótulo completo",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=WEGOVY"),
        ("Rinella ME et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. Journal of Hepatology, 2023 — origem das siglas SLD, MASLD, MetALD e MASH e dos limiares de álcool",
         "https://www.journal-of-hepatology.eu/article/S0168-8278(23)00418-X/fulltext"),
        ("AASLD. New MASLD Nomenclature — página oficial da associação americana sobre a mudança",
         "https://www.aasld.org/new-masld-nomenclature"),
        ("NIAAA. What Is A Standard Drink? — a definição de 14 g de álcool puro por dose padrão",
         "https://www.niaaa.nih.gov/alcohols-effects-health/what-standard-drink"),
        ("Organização Mundial da Saúde. No level of alcohol consumption is safe for our health — declaração de 04/01/2023, publicada em The Lancet Public Health",
         "https://www.who.int/europe/news/item/04-01-2023-no-level-of-alcohol-consumption-is-safe-for-our-health"),
        ("The Lancet Public Health. Health and cancer risks associated with low levels of alcohol consumption — o texto da declaração",
         "https://www.thelancet.com/journals/lanpub/article/PIIS2468-2667(22)00317-6/fulltext"),
        ("Åberg F, Färkkilä M. Interaction Between Alcohol Use and Metabolic Risk Factors for Liver Disease: A Critical Review of Epidemiological Studies. PMID 31854001 — a revisão sobre efeito supra-aditivo",
         "https://pubmed.ncbi.nlm.nih.gov/31854001/"),
        ("AASLD Liver Fellow Network. Spare Me the Jab: Noninvasive Assessment of Patients with MASLD — o FIB-4, seus cortes e seus limites por faixa etária",
         "https://www.aasld.org/liver-fellow-network/core-series/clinical-pearls/spare-me-jab-noninvasive-assessment-patients-masld"),
    ],
),
}
