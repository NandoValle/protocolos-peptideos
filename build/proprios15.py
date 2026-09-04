# -*- coding: utf-8 -*-
"""Ajuste de dose por funcao renal.

Nasceu de uma lacuna que a pagina de doenca renal declarou: ela diz que nao
traz ajuste de dose e que a ausencia e deliberada. Esta pagina explica por que,
e mostra o pouco que existe.

O conteudo das bulas nao foi lido em resumo: veio do endpoint de rotulos da
openFDA (api.fda.gov/drug/label.json), campo a campo, e esta transcrito.
O levantamento do que NAO existe usou o mesmo endpoint.
"""

from datas import DATA_APURACAO as _DT

DOSE_RENAL = {

"proprio_dose_renal": dict(
    titulo="Ajuste de dose por função renal — o que a bula diz e o que ninguém sabe",
    nota_refs=(
        "O texto de cada bula foi extraído por mim do endpoint de rótulos da openFDA "
        "(<code>api.fda.gov/drug/label.json</code>), campo <code>use_in_specific_populations</code> e "
        f"<code>warnings_and_cautions</code>, em {_DT}, e está transcrito acima em tradução literal. "
        "A contagem de rótulos inexistentes veio do mesmo endpoint. Os artigos citados vieram do PubMed, "
        "com DOI."
    ),
    secoes=[

# ------------------------------------------------------------------ 0. porque
dict(h="O que esta página é — e o que ela se recusa a ser", tipo="p", corpo=[
    "A página de <a href=\"proprio_rim.html\">doença renal</a> deste site termina dizendo que não traz "
    "ajuste de dose para insuficiência renal, e que a ausência é deliberada. Esta página é a explicação "
    "dessa frase, e ela tem duas metades desconfortáveis.",
    "A primeira: <strong>para a maior parte dos compostos catalogados aqui, o ajuste renal não existe "
    "porque o dado não existe</strong> — não há estudo de farmacocinética em rim doente, não há rótulo "
    "de agência, não há nada a transcrever. Uma tabela de ajuste inventada por analogia teria a mesma "
    "aparência de autoridade das tabelas do resto do site e seria ficção.",
    "A segunda é mais contraintuitiva: <strong>onde o dado existe, ele quase sempre diz para não "
    "ajustar nada</strong>. Não porque o rim não importe, mas porque a coisa que machuca o rim, nesses "
    "casos, não é a molécula — é o vômito. Isso está escrito na mesma bula, poucas seções acima, e "
    "quase ninguém lê essa parte.",
]),

# --------------------------------------------------------- 1. o que a bula diz
dict(h="O que a bula diz, literalmente", tipo="p", corpo=[
    f"Extraí o texto direto do endpoint de rótulos da openFDA em {_DT}. Não é paráfrase de artigo nem "
    "resumo de bula: é a seção 8.6 de cada rótulo, traduzida sem cortes.",
], tabela=dict(
    cap="Seção 8.6 — insuficiência renal, nos compostos deste site que têm rótulo na FDA",
    linhas=[
        ["Composto", "Produto", "O que a bula determina", "Detalhe que a bula acrescenta"],
        ["Semaglutida", "Ozempic / Rybelsus",
         "<strong>A dose recomendada em pacientes com insuficiência renal é a mesma de quem tem função "
         "renal normal.</strong>",
         "A segurança foi avaliada em estudo de 26 semanas com <strong>324 pacientes com insuficiência "
         "renal moderada</strong> (TFGe de 30 a 59 mL/min/1,73 m²). Em pacientes com insuficiência "
         "renal <strong>incluindo doença renal em estágio terminal</strong>, não se observou mudança "
         "clinicamente relevante na farmacocinética"],
        ["Tirzepatida", "Mounjaro",
         "<strong>Nenhum ajuste de dose é recomendado</strong> para pacientes com insuficiência renal.",
         "Em pessoas com insuficiência renal <strong>incluindo doença renal em estágio terminal</strong>, "
         "não se observou mudança na farmacocinética. Mas a bula manda <strong>monitorar a função "
         "renal</strong> ao iniciar ou escalonar a dose em quem tem insuficiência renal e relata "
         "reações gastrointestinais adversas graves"],
        ["Bremelanotida", "Vyleesi",
         "Nenhum ajuste em insuficiência renal <strong>leve a moderada</strong> (TFGe 30–89 mL/min/1,73 m²).",
         "<strong>Usar com cautela na insuficiência renal grave</strong> (TFGe &lt; 30), porque esses "
         "pacientes podem ter aumento na incidência e na gravidade das reações adversas — náusea e "
         "vômito"],
        ["Tesamorelina", "Egrifta SV",
         "<strong>Não estabelecida.</strong>",
         "A bula diz, com todas as letras, que a farmacocinética da tesamorelina em pacientes com "
         "insuficiência renal ou hepática <em>não foi estabelecida</em>. É um peptídeo aprovado pela "
         "FDA, com bula em vigor, e o dado renal simplesmente não existe"],
        ["Ocitocina", "Pitocin",
         "Não há seção de insuficiência renal no rótulo.",
         "Os campos de populações específicas e de farmacologia clínica do rótulo não trazem trecho "
         "sobre função renal"],
    ])),

# ------------------------------------------------ 2. por que nao e permissao
dict(h="\"Nenhum ajuste\" não é o mesmo que \"pode usar tranquilo\"", tipo="p", corpo=[
    "É aqui que a leitura desatenta cobra caro. Quando a bula diz que não há ajuste de dose, ela está "
    "respondendo a <strong>uma</strong> pergunta: o rim doente faz o remédio se acumular no sangue? "
    "Para a semaglutida e a tirzepatida, a resposta medida foi não — nem em diálise.",
    "Ela não está respondendo à outra pergunta, que é a que importa: <em>este remédio pode piorar o "
    "meu rim?</em> Essa resposta está em outro lugar do mesmo documento.",
]),

dict(h="O risco real está três seções acima, na mesma bula", tipo="p", corpo=[
    "Os dois GLP-1 deste site carregam, na seção de advertências e precauções, um item com nome "
    "próprio: <strong>Lesão Renal Aguda por Depleção de Volume</strong>. O texto é praticamente "
    "idêntico nos dois rótulos:",
    "<em>\"Lesão Renal Aguda por Depleção de Volume: monitorar a função renal em pacientes que "
    "relatarem reações adversas capazes de levar à depleção de volume.\"</em>",
    "Traduzindo o mecanismo: o risco renal desses medicamentos não vem de eles serem eliminados pelo "
    "rim. Vem de <strong>náusea, vômito e diarreia</strong> — que a mesma bula lista como reações "
    "comuns — desidratarem a pessoa a ponto de o rim, que depende de volume para filtrar, entrar em "
    "falência aguda. Quem vomita por três dias e continua a dose porque \"não precisa ajustar em "
    "insuficiência renal\" leu a seção errada.",
    "Isso reorganiza a pergunta prática inteira. Não é <em>quanto reduzir a dose</em>. É <strong>em "
    "que momento parar e beber água</strong>.",
]),

# ------------------------------------------------------ 3. o que nao existe
dict(h="Onde não há bula, não há nada", tipo="p", corpo=[
    f"Consultei o mesmo endpoint da openFDA, em {_DT}, procurando qualquer rótulo — de qualquer "
    "fabricante, de qualquer época — para os demais compostos desta referência. O resultado é a tabela "
    "abaixo, e ela é o argumento inteiro desta página.",
], tabela=dict(
    cap="Rótulos localizados na base da FDA",
    linhas=[
        ["Composto", "Rótulos na base da FDA", "O que isso significa para ajuste renal"],
        ["Tirzepatida", "8", "Há seção 8.6 — o dado existe e está transcrito acima"],
        ["Semaglutida", "5", "Há seção 8.6 — o dado existe e está transcrito acima"],
        ["Timosina alfa-1 (timalfasina)", "<strong>0</strong>", "Nada a consultar"],
        ["Cerebrolisina", "<strong>0</strong>", "Nada a consultar"],
        ["Semax", "<strong>0</strong>", "Nada a consultar"],
        ["Selank", "<strong>0</strong>", "Nada a consultar"],
        ["Sermorelina", "<strong>0</strong>", "Nada a consultar"],
        ["BPC-157", "<strong>0</strong>", "Nada a consultar"],
        ["Epitalon", "<strong>0</strong>", "Nada a consultar"],
        ["Ipamorelina", "<strong>0</strong>", "Nada a consultar"],
        ["GHK-Cu", "<strong>0</strong>", "Nada a consultar"],
        ["Melanotana", "<strong>0</strong>", "Nada a consultar"],
    ])),

dict(h="A conclusão que essa tabela impõe, e o que ela não autoriza", tipo="li", corpo=[
    "<strong>Não existe ajuste renal publicado para a maioria dos compostos deste site.</strong> Não é "
    "que eu não tenha achado: é que não há rótulo, e sem estudo de farmacocinética em rim doente não "
    "há de onde derivar número.",
    "<strong>Isso não quer dizer que sejam perigosos para o rim.</strong> Ausência de dado não é dado "
    "de dano. Dizer \"não estudado, portanto tóxico\" é o mesmo erro de raciocínio que \"natural, "
    "portanto seguro\", só que com o sinal trocado.",
    "<strong>E não quer dizer que sejam seguros.</strong> A tesamorelina mostra que nem a aprovação "
    "por agência garante o dado: ela tem bula em vigor nos Estados Unidos e a própria bula declara que "
    "a farmacocinética em insuficiência renal não foi estabelecida.",
    "<strong>O que a tabela autoriza é uma frase só:</strong> quem tem função renal reduzida e "
    "pretende usar qualquer coisa desta lista está fora de qualquer referência publicada, e a decisão "
    "é clínica, individual, com exame na mão.",
]),

# ------------------------------------------------------- 4. como se mede
dict(h="Antes de ajustar qualquer coisa: o número que você tem é confiável?", tipo="p", corpo=[
    "Toda tabela de ajuste renal do mundo depende de uma estimativa da filtração do rim. Essa "
    "estimativa não é medida — é <strong>calculada</strong> a partir da creatinina do sangue, e a "
    "conta tem armadilhas que atingem em cheio o público deste site.",
    "A equação em vigor é a <strong>CKD-EPI 2021</strong>, publicada por Inker e colaboradores no "
    "<em>New England Journal of Medicine</em>. A novidade dela é o que foi retirado: o fator de "
    "correção por raça, que superestimava a filtração — em pessoas negras de forma mais acentuada — e "
    "com isso adiava diagnóstico e encaminhamento. A força-tarefa da National Kidney Foundation com a "
    "American Society of Nephrology recomendou que todos os laboratórios adotassem a versão sem raça "
    "e que o uso de <strong>cistatina C</strong> fosse ampliado.",
]),

dict(h="A armadilha que atinge quem treina", tipo="p", corpo=[
    "A creatinina do sangue não vem só do rim: vem do músculo. Quanto mais massa muscular, mais "
    "creatinina circula — com o rim perfeitamente saudável. O mesmo vale para dieta rica em proteína e "
    "para suplementação de creatina.",
    "Segundo o PubMed, uma revisão sistemática com meta-análise publicada na <em>BMC Nephrology</em> "
    "reuniu 21 estudos, dos quais 12 entraram na meta-análise (177 pessoas no grupo creatina e 263 nos "
    "controles). O achado: a creatina aumentou a creatinina sérica de forma pequena e estatisticamente "
    "significativa (diferença média de 0,07; IC 95% 0,01 a 0,12; p = 0,03) — e "
    "<strong>não produziu diferença estatisticamente significativa na taxa de filtração "
    "glomerular</strong>. A conclusão dos autores é que o aumento reflete renovação metabólica, não "
    "lesão renal.",
    "<strong>Ressalva sobre esse número, que registro em vez de corrigir:</strong> o resumo publicado "
    "declara a diferença média em µmol/L, unidade em que 0,07 seria uma variação sem significado "
    "clínico algum. Não sei se é erro de unidade no resumo ou efeito realmente ínfimo. Reproduzo como "
    "está publicado e sinalizo a dúvida — não conserto número de terceiro por dedução.",
    "A consequência prática independe dessa dúvida: <strong>quem levanta peso, come muita proteína ou "
    "toma creatina pode receber um laudo com TFGe pior do que a realidade</strong>. E, se alguém "
    "ajustar dose com base nesse laudo, ajustou pelo motivo errado.",
]),

dict(h="A saída: cistatina C", tipo="p", corpo=[
    "A cistatina C é uma proteína pequena, filtrada pelo rim, cuja concentração <strong>não depende de "
    "massa muscular</strong>. Uma revisão do <em>Cleveland Clinic Journal of Medicine</em> de setembro "
    "de 2025 é explícita: em atletas ou em pessoas usando suplemento de creatina, a cistatina C "
    "permanece inalterada, o que garante avaliação mais precisa. Ela é indicada quando massa muscular "
    "alterada, variação de dieta ou outras condições comprometem a estimativa baseada em creatinina — "
    "e o recomendado, nesses casos, é a equação combinada CKD-EPI com os dois marcadores.",
    "O mesmo artigo mostra por que isso não é preciosismo acadêmico: na dosagem de vancomicina, 50% "
    "dos pacientes do grupo com abordagem dupla atingiram nível terapêutico contra 28% no controle, e "
    "chegaram à concentração-alvo 25% mais rápido. Estimativa melhor da filtração muda a dose que a "
    "pessoa recebe.",
    "Também vale o inverso: quem perdeu massa muscular — internação prolongada, caquexia, amputação, "
    "lesão medular — tem creatinina baixa por falta de músculo, e a conta devolve uma função renal "
    "<em>melhor</em> do que a real. Nesse caso o erro é mais perigoso, porque tranquiliza.",
]),

# ------------------------------------------------------------ 5. na pratica
dict(h="O que fazer, na ordem", tipo="li", corpo=[
    "<strong>Saber o número antes, não depois.</strong> Creatinina e TFGe pela CKD-EPI 2021 são exame "
    "de rotina e baratos. Quem usa qualquer coisa deste site sem nunca ter visto a própria TFGe está "
    "decidindo no escuro por escolha, não por falta de acesso.",
    "<strong>Se você treina pesado, come muita proteína ou toma creatina, peça cistatina C junto.</strong> "
    "Não para receber um número melhor: para receber o número certo. Pode vir pior também.",
    "<strong>Não pare o exame numa medida só.</strong> Doença renal crônica é definida por alteração "
    "que persiste por mais de três meses. Uma TFGe isolada e ruim pode ser desidratação do dia.",
    "<strong>Peça albuminúria também.</strong> A quantidade de albumina na urina é o outro eixo da "
    "classificação, e ela pode estar alterada com TFGe ainda normal — é frequentemente o primeiro "
    "sinal, e não aparece no exame de creatinina.",
    "<strong>Nos GLP-1, o gatilho de ação não é a TFGe: é o vômito.</strong> Vômito, diarreia ou "
    "ingestão baixa de líquido por mais de um dia são o momento de procurar quem prescreveu — está "
    "escrito na advertência da bula, não é interpretação minha.",
    "<strong>Ajuste de dose é ato clínico.</strong> Esta página não traz tabela de redução percentual "
    "por faixa de TFGe, e não é omissão: para a maioria dos compostos daqui, essa tabela não existe em "
    "lugar nenhum, e para os que existem a resposta publicada é \"não ajuste\".",
]),

# ---------------------------------------------------------------- 6. limites
dict(h="O que esta página não é", tipo="li", corpo=[
    "<strong>Não é orientação para ajustar dose por conta própria</strong>, nem para deixar de "
    "ajustar. É a transcrição do que consta em rótulo e a contagem do que não consta em lugar nenhum.",
    "<strong>Não cobre insuficiência hepática</strong>, que é o outro caminho de eliminação e tem "
    "seção própria (8.7) nas mesmas bulas — essa está em "
    "<a href=\"proprio_dose_hepatica.html\">fígado: ajuste de dose, e o que de fato machuca</a>.",
    "<strong>Não cobre interação com medicamentos nefrotóxicos.</strong> Anti-inflamatórios não "
    "esteroides, contraste iodado, alguns antibióticos e a combinação deles com desidratação são "
    "causas frequentes de lesão renal aguda, e nada disso foi levantado aqui.",
    "<strong>Não substitui a bula brasileira.</strong> O que está acima é o rótulo americano. Para o "
    "que vale no Brasil, a fonte é o bulário da ANVISA — e a página dos GLP-1 contra a bula, neste "
    "mesmo site, mostra que os dois textos divergem em pontos que importam.",
]),
    ],
    referencias=[
        ("openFDA — Drug Label API. Endpoint usado para extrair a seção 8.6 (use in specific populations) e as advertências de cada rótulo citado",
         "https://open.fda.gov/apis/drug/label/"),
        ("DailyMed — OZEMPIC (semaglutida), rótulo completo",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=OZEMPIC"),
        ("DailyMed — MOUNJARO (tirzepatida), rótulo completo",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=MOUNJARO"),
        ("DailyMed — VYLEESI (bremelanotida), rótulo completo",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=VYLEESI"),
        ("DailyMed — EGRIFTA SV (tesamorelina), rótulo completo; declara que a farmacocinética em insuficiência renal não foi estabelecida",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=EGRIFTA"),
        ("PubMed — Kabiri Naeini E, Eskandari M, Mortazavi M, Gholaminejad A, Karevan N. Effect of creatine supplementation on kidney function: a systematic review and meta-analysis. BMC Nephrol. 2025;26(1):622. PMID 41199218 · doi:10.1186/s12882-025-04558-6",
         "https://doi.org/10.1186/s12882-025-04558-6"),
        ("Inker LA et al. New Creatinine- and Cystatin C–Based Equations to Estimate GFR without Race. N Engl J Med. 2021 — a equação CKD-EPI 2021",
         "https://www.nejm.org/doi/full/10.1056/NEJMoa2102953"),
        ("National Kidney Foundation. Recommendations for Implementing the CKD-EPI 2021 Race-Free eGFR Calculation: Guidelines for Clinical Laboratories",
         "https://www.kidney.org/recommendations-implementing-ckd-epi-2021-race-free-egfr-calculation-guidelines-clinical"),
        ("Cleveland Clinic Journal of Medicine, setembro de 2025;92(9):546. What is the role of cystatin C in estimating glomerular filtration rate and guiding medication dosing?",
         "https://www.ccjm.org/content/92/9/546"),
        ("ANVISA — Bulário eletrônico, para o texto que vale no Brasil",
         "https://consultas.anvisa.gov.br/#/bulario/"),
    ],
),
}
