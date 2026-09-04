# -*- coding: utf-8 -*-
"""Ajuste de dose por funcao hepatica -- o par da pagina renal.

Mesmo metodo: secao 8.7 extraida do endpoint de rotulos da openFDA, transcrita.
A diferenca em relacao a pagina renal e que aqui existe dano documentado, e ele
atinge exatamente o publico deste site: suplemento de fisiculturismo e SARM.

O achado que inverte a leitura: o unico composto citado neste site que a bula
manda EVITAR em qualquer grau de insuficiencia hepatica e um remedio de rim.
"""

from datas import DATA_APURACAO as _DT

HEPATICA = {

"proprio_dose_hepatica": dict(
    titulo="Fígado — ajuste de dose, e o que de fato machuca",
    nota_refs=(
        "O texto de cada bula foi extraído por mim do endpoint de rótulos da openFDA "
        "(<code>api.fda.gov/drug/label.json</code>), campos <code>use_in_specific_populations</code> e "
        f"<code>boxed_warning</code>, em {_DT}, e está transcrito acima em tradução literal. Os dados de "
        "lesão hepática por suplemento vêm do PubMed e do LiverTox, base do National Institute of "
        "Diabetes and Digestive and Kidney Diseases, com DOI e identificador."
    ),
    secoes=[

# ------------------------------------------------------------------ 0. porque
dict(h="O par da página renal — e por que este lado é pior", tipo="p", corpo=[
    "A página de <a href=\"proprio_dose_renal.html\">ajuste de dose por função renal</a> terminou "
    "dizendo que não cobria o fígado. Esta cobre, pelo mesmo método: seção 8.7 de cada bula, extraída "
    "do endpoint de rótulos da FDA e transcrita sem corte.",
    "A diferença entre as duas é grande e desconfortável. No lado renal, o levantamento devolveu "
    "sobretudo <em>lacuna</em>: onde havia dado, ele mandava não ajustar nada. Aqui há lacuna também — "
    "mas há, além dela, <strong>dano documentado, com nome, número e desfecho</strong>. E ele atinge "
    "em cheio o público deste site: homens jovens, tomando coisa comprada pela internet para ganhar "
    "músculo.",
    "Há ainda uma inversão que vale registrar antes de tudo: <strong>o único composto citado neste "
    "site que a bula manda evitar em qualquer grau de insuficiência hepática é um remédio de "
    "rim</strong>.",
]),

# --------------------------------------------------------- 1. o que a bula diz
dict(h="O que a bula diz, literalmente", tipo="p", corpo=[
    f"Extraído do mesmo endpoint, em {_DT}, seção 8.7 de cada rótulo.",
], tabela=dict(
    cap="Seção 8.7 — insuficiência hepática",
    linhas=[
        ["Composto", "Produto", "O que a bula determina", "Detalhe"],
        ["Semaglutida", "Ozempic / Rybelsus",
         "<strong>A dose recomendada em pacientes com insuficiência hepática é a mesma de quem tem "
         "função hepática normal.</strong>",
         "Num estudo com diferentes graus de insuficiência hepática, não se observou mudança "
         "clinicamente relevante na farmacocinética"],
        ["Tirzepatida", "Mounjaro",
         "<strong>Nenhum ajuste de dose é recomendado.</strong>",
         "Em estudo de farmacologia clínica com graus variados de insuficiência hepática, não se "
         "observou mudança na farmacocinética"],
        ["Bremelanotida", "Vyleesi",
         "Nenhum ajuste em insuficiência hepática <strong>leve a moderada</strong> (Child-Pugh A e B, "
         "escore 5–9).",
         "<strong>Não foi avaliada</strong> na insuficiência hepática grave. Usar com cautela em "
         "Child-Pugh C (escore 10–15), porque esses pacientes podem ter aumento na incidência e na "
         "gravidade das reações adversas"],
        ["Tesamorelina", "Egrifta SV",
         "<strong>Não estabelecida.</strong>",
         "O mesmo trecho que declara a lacuna renal declara a hepática: a farmacocinética em pacientes "
         "com insuficiência renal <em>ou hepática</em> não foi estabelecida"],
        ["Sparsentana", "Filspari",
         "<strong>Evitar o uso em pacientes com qualquer grau de insuficiência hepática</strong> "
         "(Child-Pugh A a C), pelo risco potencial de lesão hepática grave.",
         "Tem <strong>tarja preta</strong> por hepatotoxicidade e só é distribuído sob programa "
         "restrito, com inscrição obrigatória de quem prescreve, de quem dispensa e do próprio paciente"],
    ])),

# ------------------------------------------------------------- 2. a inversao
dict(h="A tarja preta do remédio de rim", tipo="p", corpo=[
    "A sparsentana é um dos seis medicamentos da página de <a href=\"proprio_rim.html\">doença "
    "renal</a> — aprovada para nefropatia por IgA e, desde 2026, para glomeruloesclerose segmentar e "
    "focal. A tarja preta dela não fala de rim. Fala de fígado, e a frase da bula merece ser lida "
    "inteira:",
    "<em>\"Alguns antagonistas do receptor de endotelina causaram elevações de aminotransferases, "
    "hepatotoxicidade e falência hepática.\"</em>",
    "Repare no sujeito da frase: não é <em>este medicamento</em>, é <strong>a classe</strong>. O "
    "risco foi herdado de parentes químicos, e a bula o assume por precaução antes de o produto ter "
    "acumulado casos próprios. É o oposto exato do raciocínio que circula sobre peptídeo de pesquisa, "
    "onde a ausência de caso relatado é apresentada como prova de segurança — quando quase sempre é "
    "só ausência de vigilância.",
    "E há a lição de escala: um medicamento com ensaio de fase 3, agência, bula e programa de "
    "acompanhamento obrigatório <strong>ainda assim</strong> carrega risco hepático a ponto de exigir "
    "cadastro de paciente. Aprovação não é ausência de risco; é risco medido, nomeado e vigiado.",
]),

# ------------------------------------------------------------- 3. child-pugh
dict(h="Por que você não consegue se classificar sozinho", tipo="p", corpo=[
    "Toda bula acima fala em <strong>Child-Pugh A, B ou C</strong>. É aqui que o lado hepático se "
    "separa do renal de um jeito que quase ninguém percebe.",
    "No rim, a classificação sai de uma conta: creatinina, idade e sexo entram na equação CKD-EPI e "
    "sai um número. O laboratório já entrega a TFGe impressa no laudo. No fígado, não existe "
    "equivalente. O Child-Pugh é um <strong>escore clínico</strong>, e dois dos seus cinco componentes "
    "não são exame — são achado de exame físico e de avaliação neurológica.",
], tabela=dict(
    cap="Os cinco componentes do escore de Child-Pugh, 1 a 3 pontos cada",
    linhas=[
        ["Componente", "1 ponto", "2 pontos", "3 pontos", "De onde vem"],
        ["Bilirrubina", "abaixo de 2 mg/dL", "2 a 3 mg/dL", "acima de 3 mg/dL", "Exame de sangue"],
        ["Albumina", "acima de 3,5 g/dL", "2,8 a 3,5 g/dL", "abaixo de 2,8 g/dL", "Exame de sangue"],
        ["INR", "abaixo de 1,7", "1,7 a 2,2", "acima de 2,2", "Exame de sangue"],
        ["Ascite", "ausente", "leve", "moderada", "<strong>Exame físico / imagem</strong>"],
        ["Encefalopatia", "ausente", "graus 1 e 2", "graus 3 e 4", "<strong>Avaliação clínica</strong>"],
    ])),

dict(h="A consequência prática disso", tipo="li", corpo=[
    "<strong>Escore de 5 a 15 pontos:</strong> 5–6 é classe A, 7–9 é classe B, 10–15 é classe C.",
    "<strong>Três dos cinco componentes você consegue pedir; dois, não.</strong> Ascite e "
    "encefalopatia dependem de alguém examinar a pessoa. Não existe \"tirar o Child-Pugh no "
    "laboratório\" como se tira a TFGe.",
    "<strong>Por isso a bula que diz \"Child-Pugh C\" está falando com o médico, não com você.</strong> "
    "Quem tenta se enquadrar sozinho vai usar só a parte que dá para medir — e a parte que falta é "
    "justamente a que indica doença avançada.",
]),

# --------------------------------------------------------- 4. armadilha do TGO
dict(h="A armadilha simétrica: musculação faz o exame de fígado ficar horrível", tipo="p", corpo=[
    "Na página renal, a armadilha era a creatinina inflada por massa muscular e creatina. Aqui ela "
    "tem um irmão maior, e mais dramático.",
    "Segundo o PubMed, um estudo publicado no <em>British Journal of Clinical Pharmacology</em> pegou "
    "<strong>15 homens saudáveis</strong>, acostumados a atividade física moderada mas não a "
    "musculação, e aplicou <strong>uma hora</strong> de treino de força. Cinco dos oito parâmetros "
    "medidos — AST, ALT, LDH, CK e mioglobina — subiram de forma significativa (P &lt; 0,01) e "
    "<strong>continuaram elevados por pelo menos sete dias</strong>. O título do artigo não é "
    "cauteloso: <em>exercício muscular pode causar exames de função hepática altamente "
    "patológicos em homens saudáveis</em>.",
    "Uma hora de treino. Sete dias de exame alterado. Em quem não tinha nada.",
]),

dict(h="O achado que salva o leitor: o que NÃO subiu", tipo="p", corpo=[
    "O mesmo estudo registra que <strong>bilirrubina, gama-GT e fosfatase alcalina permaneceram "
    "dentro da faixa normal</strong>. Isso não é detalhe: é o critério que separa músculo de fígado.",
    "Quando AST e ALT sobem <em>junto com</em> CK e mioglobina, e bilirrubina, GGT e fosfatase "
    "alcalina ficam normais, a origem provável é muscular. Quando bilirrubina e fosfatase alcalina "
    "sobem, a conversa é outra — e é a do fígado.",
    "O erro clássico aqui tem duas direções, e as duas custam caro. Uma é o susto: pessoa treinada "
    "faz exame na segunda-feira depois do treino de sábado, vê TGO e TGP alterados e passa semanas "
    "achando que tem hepatite. A outra é pior e é a que interessa a este site: <strong>pessoa que "
    "realmente está com lesão hepática por algo que tomou atribui o exame alterado ao treino</strong> "
    "e continua tomando.",
]),

# ------------------------------------------------------------- 5. o dano real
dict(h="Onde o dano hepático de verdade aparece neste público", tipo="p", corpo=[
    "Aqui os números deixam de ser sobre lacuna e passam a ser sobre caso contado, com desfecho.",
    "Segundo o PubMed, a Drug-Induced Liver Injury Network — rede de oito centros de referência nos "
    "Estados Unidos — acompanhou prospectivamente <strong>839 casos</strong> de lesão hepática por "
    "medicamento ou suplemento entre 2004 e 2013. Destes, <strong>130 (15,5%)</strong> foram "
    "atribuídos a ervas e suplementos alimentares, e a proporção <strong>subiu de 7% para 20%</strong> "
    "ao longo do período estudado (P &lt; 0,001).",
], tabela=dict(
    cap="Lesão hepática na DILIN, por tipo de agente",
    linhas=[
        ["Agente", "Casos", "Perfil e desfecho"],
        ["Medicamentos", "709", "3% de óbito ou transplante"],
        ["Suplementos de fisiculturismo", "<strong>45</strong>",
         "Icterícia prolongada — mediana de <strong>91 dias</strong> — em homens jovens. "
         "<strong>Nenhum óbito e nenhum transplante</strong>"],
        ["Demais suplementos e ervas", "85",
         "Lesão hepatocelular, predominantemente em mulheres de meia-idade. "
         "<strong>13% de óbito ou transplante</strong> — mais grave que a dos medicamentos"],
    ])),

dict(h="Como ler essa tabela sem escolher a metade conveniente", tipo="li", corpo=[
    "<strong>Suplemento de fisiculturismo não matou ninguém nessa série — e isso não é tranquilizante.</strong> "
    "Noventa e um dias de icterícia é a mediana, não o pior caso. Metade dos homens ficou amarelo por "
    "mais que três meses.",
    "<strong>O suplemento que mais mata não é o do fisiculturismo.</strong> É o outro grupo, de "
    "ervas e produtos de bem-estar, com 13% de óbito ou transplante — quatro vezes a taxa dos "
    "medicamentos de prescrição. A intuição de que \"remédio é perigoso, suplemento é leve\" está "
    "invertida nesses dados.",
    "<strong>A proporção quase triplicou em nove anos.</strong> De 7% para 20% dos casos de lesão "
    "hepática atendidos numa rede de referência. Não é fenômeno estável: é curva subindo.",
]),

# ------------------------------------------------------------------ 6. SARMs
dict(h="SARMs: o caso mais bem documentado, e ele é deste site", tipo="p", corpo=[
    "Este site já tem uma página de <a href=\"proprio_sarms.html\">SARMs</a>. O LiverTox — base de "
    "hepatotoxicidade do National Institute of Diabetes and Digestive and Kidney Diseases, ligado ao "
    "NIH — mantém uma entrada inteira sobre eles. O que segue foi conferido no texto da própria "
    "entrada, não em resumo dela.",
    "O primeiro achado desmonta a leitura tranquilizadora dos ensaios clínicos. Neles, os SARMs foram "
    "descritos como bem tolerados — mas nas doses maiores, as que mais aumentavam massa magra, houve "
    "elevação de aminotransferases em <strong>5% a 21%</strong> dos participantes, com casos de ALT "
    "isolada exigindo suspensão. Nenhum caso de icterícia apareceu nesses ensaios, e o LiverTox diz "
    "por quê: <em>a duração da terapia era curta, os pacientes eram monitorados regularmente, e uma "
    "pequena proporção interrompeu o tratamento por causa das elevações de ALT</em>.",
    "A icterícia apareceu depois, fora dos ensaios — em pessoas usando SARM por conta própria para "
    "musculação, sem supervisão médica.",
], tabela=dict(
    cap="Lesão hepática por SARM, segundo o texto do LiverTox",
    linhas=[
        ["Item", "O que está documentado"],
        ["Tempo até aparecer",
         "Latência <strong>tipicamente de 2 a 3 meses</strong>, com variação de algumas semanas a "
         "<strong>um ano</strong>"],
        ["Como começa",
         "Fadiga, perda de apetite, perda de peso, dor abdominal e coceira, seguidos de urina escura e "
         "icterícia"],
        ["Exames no início",
         "Bilirrubina total só moderadamente elevada (<strong>4,0 a 8,0 mg/dL</strong>), "
         "aminotransferases de <strong>2 a 5 vezes</strong> o limite superior do normal, e fosfatase "
         "alcalina e GGT <strong>minimamente elevadas ou normais</strong>"],
        ["Como evolui",
         "<strong>A bilirrubina sobe enquanto as aminotransferases caem</strong>, e a fosfatase "
         "alcalina sobe pouco. O resultado do exame depende de quanto tempo de doença já passou "
         "quando ele foi colhido"],
        ["O que a biópsia mostra",
         "Colestase canalicular moderada a grave, com inflamação leve ou mínima e sem perda de ductos "
         "biliares — a chamada <em>colestase branda</em>, o mesmo quadro da icterícia por esteroide "
         "anabolizante"],
        ["Quando a bilirrubina passa de 30 mg/dL",
         "Pode surgir <strong>disfunção renal com cilindros de bilirrubina</strong>, que às vezes "
         "exige diálise temporária — autolimitada, resolve quando a bilirrubina cai"],
        ["Desfecho",
         "Prolongado, porém autolimitado. <strong>Alguns pacientes com icterícia prolongada e sintomas "
         "incapacitantes chegaram a ser encaminhados para transplante de fígado</strong>, mas quase "
         "todos melhoraram espontaneamente e o transplante foi evitado. Com seguimento longo, "
         "espera-se resolução completa"],
        ["Classificação de causalidade",
         "<strong>Escore B</strong> do LiverTox: causa provável de lesão hepática clinicamente "
         "aparente, com icterícia"],
    ])),

dict(h="A dose dos casos não é a dose dos ensaios", tipo="p", corpo=[
    "O LiverTox publica uma tabela que raramente aparece em qualquer outro lugar: a dose usada nos "
    "ensaios clínicos ao lado da dose usada pelas pessoas que tiveram lesão hepática.",
], tabela=dict(
    cap="Doses, segundo a tabela do LiverTox",
    linhas=[
        ["Nome genérico", "Também chamado de", "Faixa em ensaios clínicos",
         "Faixa nos casos de lesão hepática"],
        ["Ligandrol", "LGD-4033, VK-5211", "0,1 a 2,0 mg", "<strong>4 a 30 mg</strong>"],
        ["Enobosarme", "MK-2866, S-22, GTx-024, Ostarina", "0,1 a 3,0 mg", "<strong>5 a 20 mg</strong>"],
        ["Vosilasarme", "RAD-140, Testolona", "50 a 150 mg", "5 a 30 mg"],
        ["Andarina", "GTx-007, S-4", "não reportada", "25 a 50 mg"],
    ])),

dict(h="O que essa tabela mostra, e o que eu não vou concluir dela", tipo="li", corpo=[
    "<strong>No Ligandrol e no Enobosarme, quem se machucou usava muito mais do que o testado.</strong> "
    "O Ligandrol foi estudado entre 0,1 e 2,0 mg; nos casos de lesão hepática a faixa foi de 4 a 30 mg "
    "— o teto é quinze vezes a dose máxima de ensaio.",
    "<strong>No Vosilasarme a relação aparece invertida</strong>, com faixa de ensaio maior que a dos "
    "casos. Reproduzo a tabela como ela está publicada e não tento explicar a inversão: não sei se é "
    "particularidade do composto, do desenho dos estudos ou da própria tabela.",
    "<strong>Nada disso autoriza a leitura de que existe dose segura.</strong> A tabela mostra o que "
    "as pessoas dos relatos tomaram, não um limiar abaixo do qual não há lesão.",
]),

dict(h="Dois achados que mudam a conduta", tipo="p", corpo=[
    "O primeiro está no caso clínico detalhado que a própria entrada traz, com a tabela de exames "
    "semana a semana. O homem parou o suplemento ao ficar sintomático. Quatro dias depois: bilirrubina "
    "7,9 mg/dL e ALT 177 U/L. Nas semanas seguintes, com o suplemento já suspenso, a "
    "<strong>ALT caiu para a faixa normal — 43, 47, 48 U/L, com limite de referência abaixo de "
    "50</strong> — enquanto a <strong>bilirrubina subia para 27,9, depois 29,3, e chegava ao pico de "
    "41,5 mg/dL</strong>.",
    "Quem estivesse acompanhando só TGO e TGP teria visto exames normalizando no exato período em que "
    "a pessoa piorava. Numa lesão colestática, o marcador que conta é a <strong>bilirrubina</strong> — "
    "e não adianta esperar pela fosfatase alcalina, que o próprio LiverTox descreve como minimamente "
    "elevada ou normal no início. Esse caso teve latência de cinco semanas e levou quatro meses para "
    "os exames voltarem ao normal.",
    "O segundo é a latência de 2 a 3 meses, que desmonta a lógica do ciclo. Quem faz oito semanas e "
    "para pode ficar ictérico <em>depois</em> de ter parado — foi o que aconteceu nesse caso — e não "
    "associar. E quem chega ao fim do primeiro ciclo sem sintoma nenhum não recebeu prova de "
    "segurança: recebeu um intervalo de tempo que ainda não terminou.",
]),

dict(h="O que o LiverTox diz sobre a regulação disso", tipo="li", corpo=[
    "<strong>Nenhum SARM é aprovado para uso humano pela FDA.</strong> A entrada lista pelo menos 16 "
    "agentes diferentes, muitos com vários nomes químicos e comerciais.",
    "<strong>A FDA publicou vários alertas clínicos</strong> sobre os perigos do uso de SARMs e sobre "
    "a falta de segurança e eficácia comprovadas, e agiu contra produtores do mercado clandestino — "
    "mas os produtos continuam disponíveis.",
    "<strong>O rótulo costuma dizer que o produto é apenas para pesquisa.</strong> O LiverTox explica "
    "a função dessa frase: é o que permite ao fabricante alegar que a venda não viola a exigência de "
    "aprovação regulatória. Não é uma descrição do produto, é uma manobra.",
    "<strong>O que está escrito no rótulo pode não ser confiável</strong>, segundo a própria entrada. "
    "E os SARMs são <strong>banidos pela Agência Mundial Antidopagem</strong>, tendo sido detectados "
    "em atletas de competição, que foram suspensos.",
]),

# ------------------------------------------------------------ 7. na pratica
dict(h="O que fazer, na ordem", tipo="li", corpo=[
    "<strong>Exame de base antes, não depois.</strong> AST, ALT, fosfatase alcalina, GGT, bilirrubina "
    "total e frações, albumina e INR. Sem valor anterior, um exame alterado no meio do uso não tem com "
    "o que ser comparado.",
    "<strong>Colete com pelo menos uma semana sem treino de força pesado.</strong> É a única forma de "
    "o número medir fígado em vez de músculo — o estudo mostra alteração persistindo por sete dias "
    "depois de <em>uma</em> sessão.",
    "<strong>Peça CK junto.</strong> É o que discrimina: CK alta com bilirrubina, GGT e fosfatase "
    "alcalina normais aponta para músculo.",
    "<strong>Não monitore só transaminase.</strong> No padrão colestático — o dos SARMs e dos "
    "anabolizantes — quem denuncia a piora é a <strong>bilirrubina</strong>, e ela pode subir com a "
    "ALT caindo. A fosfatase alcalina começa minimamente elevada ou normal, então esperar por ela "
    "atrasa o diagnóstico.",
    "<strong>Urina escura, fezes claras, coceira sem lesão de pele, olhos amarelados: parar e "
    "procurar atendimento no mesmo dia.</strong> Nessa ordem de sintomas, o exame vem depois da "
    "consulta, não antes.",
    "<strong>Leve a embalagem e o rótulo.</strong> Nas séries da DILIN e do LiverTox, boa parte da "
    "dificuldade diagnóstica veio de ninguém saber o que a pessoa tinha tomado. O nome do produto e o "
    "lote valem mais que a descrição de memória.",
]),

# ---------------------------------------------------------------- 8. limites
dict(h="O que esta página não é", tipo="li", corpo=[
    "<strong>Não é tabela de ajuste por Child-Pugh.</strong> Para os compostos deste site que têm "
    "bula, a resposta publicada está transcrita acima e na maioria é \"nenhum ajuste\"; para os que "
    "não têm bula, não existe número em lugar nenhum — como na página renal.",
    "<strong>Não é lista de compostos hepatotóxicos deste site.</strong> O que há é o que está "
    "documentado: SARMs, suplementos de fisiculturismo e a classe dos antagonistas de endotelina. "
    "Ausência de relato para os demais é ausência de relato, não atestado.",
    "<strong>Não cobre hepatites virais nem interação medicamentosa</strong> — que são, no mundo real, "
    "causa muito mais frequente de exame hepático alterado do que qualquer coisa catalogada aqui. "
    "Álcool e esteatose, que estavam nessa mesma lista, agora têm página própria: "
    "<a href=\"proprio_alcool_esteatose.html\">álcool e esteatose</a>.",
    "<strong>Não substitui a bula brasileira.</strong> O texto acima é o rótulo americano.",
]),
    ],
    referencias=[
        ("openFDA — Drug Label API. Endpoint usado para extrair a seção 8.7 e a tarja preta de cada rótulo citado",
         "https://open.fda.gov/apis/drug/label/"),
        ("DailyMed — FILSPARI (sparsentana): tarja preta de hepatotoxicidade, programa restrito REMS e a instrução de evitar uso em qualquer grau de insuficiência hepática",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=FILSPARI"),
        ("DailyMed — OZEMPIC (semaglutida), rótulo completo",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=OZEMPIC"),
        ("DailyMed — MOUNJARO (tirzepatida), rótulo completo",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=MOUNJARO"),
        ("DailyMed — VYLEESI (bremelanotida), rótulo completo",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=VYLEESI"),
        ("PubMed — Pettersson J, Hindorf U, Persson P, et al. Muscular exercise can cause highly pathological liver function tests in healthy men. Br J Clin Pharmacol. 2007;65(2):253-9. PMID 17764474 · doi:10.1111/j.1365-2125.2007.03001.x",
         "https://doi.org/10.1111/j.1365-2125.2007.03001.x"),
        ("PubMed — Navarro VJ, Barnhart H, Bonkovsky HL, et al. Liver injury from herbals and dietary supplements in the U.S. Drug-Induced Liver Injury Network. Hepatology. 2014;60(4):1399-408. PMID 25043597 · doi:10.1002/hep.27317",
         "https://doi.org/10.1002/hep.27317"),
        ("LiverTox — Selective Androgen Receptor Modulators. National Institute of Diabetes and Digestive and Kidney Diseases, NCBI Bookshelf NBK619971",
         "https://www.ncbi.nlm.nih.gov/books/NBK619971/"),
        ("StatPearls — Use of the Child Pugh Score in Liver Disease. NCBI Bookshelf NBK542308",
         "https://www.ncbi.nlm.nih.gov/books/NBK542308/"),
        ("ANVISA — Bulário eletrônico, para o texto que vale no Brasil",
         "https://consultas.anvisa.gov.br/#/bulario/"),
    ],
),
}
