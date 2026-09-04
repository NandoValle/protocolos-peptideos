# -*- coding: utf-8 -*-
"""Os 18 medicamentos do leste europeu do catalogo de importacao.

Contagens conferidas no PubMed e no ClinicalTrials.gov em 04/09/2026.
"""

LESTE = {
"proprio_leste": dict(
    secoes=[
        dict(h="O que é este bloco", tipo="p", corpo=[
            "Dezoito medicamentos registrados na Rússia, na Letônia ou no leste europeu, que chegam ao Brasil por "
            "importação. Nenhum tem registro na ANVISA. Vieram de um catálogo de importadora, e a lista original "
            "trazia 26 produtos — a diferença são variantes cápsula/injetável, uma duplicata, e Cerebrolisina, "
            "Selank e Semax, que já têm página própria nesta referência.",
            "<strong>Este bloco surpreendeu.</strong> Eu esperava encontrar o mesmo vazio dos bioreguladores de "
            "Khavinson, que somam zero ensaios registrados. Encontrei o contrário: <strong>29 ensaios registrados "
            "no ClinicalTrials.gov</strong>, vários de fase 3, alguns com centenas de participantes e desenho "
            "duplo-cego contra placebo.",
        ]),
        dict(h="O levantamento", tipo="p", corpo=[
            "PubMed e ClinicalTrials.gov, consultados em 4 de setembro de 2026, um composto por vez. A coluna "
            "<strong>ECR/meta</strong> usa o filtro de ensaio randomizado ou metanálise.",
        ], tabela=dict(
            cap="Evidência por composto",
            linhas=[
                ["Composto", "O que é", "PubMed", "ECR/meta", "Ensaio registrado"],
                ["Mexidol", "Etilmetilhidroxipiridina succinato (emoxipina)", "<strong>614</strong>", "<strong>59</strong>", "Sim — 6 vistos, fases 2 a 4"],
                ["Cytoflavin", "Ácido succínico + inosina + nicotinamida + riboflavina", "<strong>314</strong>", "não conferido", "Sim — 5 vistos, fase 3"],
                ["Actovegin", "Hemoderivado desproteinizado de sangue de bezerro", "<strong>185</strong>", "<strong>26</strong>", "Sim — 2 de fase 3, patrocínio ocidental"],
                ["Pantogam / Pantocalcin", "Ácido hopantênico / hopantenato de cálcio", "<strong>166</strong>", "não conferido", "não visto"],
                ["Afobazol", "Fabomotizol, ansiolítico não benzodiazepínico", "<strong>158</strong>", "<strong>5</strong>", "Sim — 1, fase 4, recrutando"],
                ["Neuromidin", "Ipidacrina (amiridina), inibidor de colinesterase", "<strong>148</strong>", "<strong>18</strong>", "não visto"],
                ["Stresam", "Etifoxina, ansiolítico", "<strong>118</strong>", "<strong>12</strong>", "Sim — 2, incluindo comparação com lorazepam"],
                ["Polyoxidonium", "Azoximer brometo, imunomodulador", "<strong>84</strong>", "não conferido", "Sim — 3, incluindo fase 2/3 em covid com 394 participantes"],
                ["Picamilon", "Nicotinoil-GABA", "<strong>60</strong>", "não conferido", "não visto"],
                ["Derinat", "Desoxirribonucleato de sódio", "<strong>36</strong>", "não conferido", "não visto"],
                ["Nanotropil", "Fenilpiracetam (fonturacetam, carfedon)", "<strong>34</strong>", "não conferido", "não visto"],
                ["Galavit", "Aminodihidroftalazinediona sódica", "<strong>28</strong>", "não conferido", "não visto"],
                ["Cortexin", "Polipeptídeos corticais bovinos", "<strong>26</strong>", "não conferido", "não visto"],
                ["Memoprove", "N-PEP-12, derivado peptídico", "<strong>16</strong>", "não conferido", "não visto"],
                ["Etoxidol", "Etilmetilhidroxipiridina malato", "<strong>11</strong>", "não conferido", "não visto"],
                ["Cocarboxilase", "Tiamina pirofosfato", "534 <strong>(contagem inflada)</strong>", "não conferido", "não visto"],
                ["Citocromo C", "Citocromo c injetável", "108 <strong>(contagem inflada)</strong>", "não conferido", "não visto"],
                ["Meldonium", "Já tem página própria nesta referência", "357", "35", "Sim — 7"],
            ])),
        dict(h="A armadilha da contagem, de novo", tipo="p", corpo=[
            "Duas linhas da tabela estão marcadas como <strong>contagem inflada</strong>, e vale explicar por quê.",
            "<strong>Cocarboxilase</strong> é tiamina pirofosfato — uma coenzima que todo organismo vivo usa. Os 534 "
            "artigos falam majoritariamente de bioquímica do metabolismo, não do medicamento injetável. "
            "<strong>Citocromo C</strong> é pior: os 108 artigos tratam sobretudo do papel da molécula na apoptose, "
            "assunto central da biologia celular e sem relação com a ampola.",
            "É o mesmo erro do <em>Ovagen</em>, registrado na página dos bioreguladores: buscar pelo nome comercial "
            "e contar tudo que o nome pega. Quando a molécula tem função biológica própria, a contagem mede a "
            "biologia, não o remédio.",
        ]),
        dict(h="Quem paga os ensaios", tipo="p", corpo=[
            "Aqui está a ressalva que equilibra o número. Dos ensaios registrados que examinei, a esmagadora "
            "maioria é <strong>patrocinada pelo próprio fabricante e conduzida na Rússia</strong>: Pharmasoft para o "
            "Mexidol, POLYSAN para o Cytoflavin, NPO Petrovax para o Polyoxidonium, Valenta para o Afobazol.",
            "Isso não invalida os estudos. Ensaio de registro é normalmente pago pelo fabricante, no mundo inteiro. "
            "Mas quando <em>todos</em> os ensaios de um composto vêm da mesma empresa, no mesmo país, sem replicação "
            "independente, o leitor precisa saber — do mesmo modo que precisa saber que o estudo de longevidade do "
            "Thymalin é assinado pelo próprio inventor.",
        ]),
        dict(h="O Actovegin é a exceção", tipo="p", corpo=[
            "Um composto deste bloco tem ensaio de fase 3 internacional, com patrocínio de farmacêutica ocidental "
            "de grande porte — coisa que nenhum outro item desta referência tem.",
        ], tabela=dict(
            cap="Os dois ensaios de fase 3 do Actovegin",
            linhas=[
                ["Registro", "Patrocinador", "Condição", "N", "Desenho", "Situação"],
                ["NCT01582854", "<strong>Takeda</strong>", "Comprometimento cognitivo pós-AVC", "<strong>503</strong>",
                 "Duplo-cego, placebo, 12 meses, 14 centros, intravenoso seguido de oral", "Concluído"],
                ["NCT00483730", "<strong>Nycomed</strong>", "Polineuropatia periférica diabética sintomática, DM2", "<strong>569</strong>",
                 "Duplo-cego, placebo, multicêntrico, grupos paralelos", "Concluído"],
            ])),
        dict(h="Dois sinais de segurança que o catálogo não menciona", tipo="p", corpo=[
            "Ao levantar este bloco, apareceram dois achados que mudam a leitura de risco de itens vendidos como "
            "banais. Segundo o PubMed:",
        ], tabela=dict(
            cap="Achados de segurança verificados",
            linhas=[
                ["Composto", "O achado", "Fonte"],
                ["<strong>Pantogam / Pantocalcin</strong><br><small>hopantenato de cálcio</small>",
                 "Os primeiros casos de <strong>encefalopatia tóxica</strong> foram relatados em 1986 no Japão. O quadro "
                 "lembrava a síndrome de Reye — coma, insuficiência hepática, acidose láctica e hipoglicemia — e era "
                 "<strong>frequentemente fatal</strong>. A revisão de Kuzuhara contabiliza <strong>mais de 47 casos, "
                 "com 11 mortes</strong>. O artigo também registra que essa classe de fármacos era muito prescrita no "
                 "Japão, raramente usada na Europa ocidental e <strong>inexistente no mercado dos Estados Unidos</strong>",
                 "Kuzuhara S, 1991 · Nihon Ronen Igakkai Zasshi 28(4):493-8 · PMID 1942629"],
                ["<strong>Nanotropil</strong><br><small>fenilpiracetam</small>",
                 "<strong>Proibido pela WADA.</strong> É o segundo item deste bloco na lista de substâncias proibidas, "
                 "junto com o meldonium. Tem apenas 34 artigos no PubMed — dos menores volumes da tabela",
                 "Lista de proibidos da WADA"],
                ["<strong>Stresam</strong><br><small>etifoxina</small>",
                 "Existem 4 artigos indexados especificamente sobre <strong>lesão hepática e hepatite</strong> associadas "
                 "à etifoxina. O sinal existe e está documentado; a magnitude do risco não foi avaliada nesta compilação",
                 "PubMed, 4 artigos"],
            ])),
        dict(h="Como ler este bloco", tipo="li", corpo=[
            "<strong>É o bloco mais bem estudado dos que entraram por catálogo de importação</strong> — muito acima "
            "dos bioreguladores russos, que têm zero ensaios registrados.",
            "<strong>Mas a evidência é quase toda do fabricante.</strong> Replicação independente é o que falta, e é "
            "justamente o que separa um fármaco aceito de um fármaco regional.",
            "<strong>Actovegin é o único com fase 3 de patrocínio ocidental</strong>, e mesmo assim não conseguiu "
            "registro nos EUA nem na União Europeia.",
            "<strong>Pantogam merece atenção especial.</strong> É vendido como nootrópico infantil em alguns lugares, "
            "e tem histórico de mortes por encefalopatia. Esse dado tem quase quarenta anos e sumiu do discurso "
            "comercial.",
            "<strong>Nenhum tem registro na ANVISA.</strong> Importar não transforma nenhum deles em medicamento "
            "aprovado no Brasil — muda apenas quem carrega o risco.",
        ]),
        dict(h="O que esta página não traz", tipo="p", corpo=[
            "Não traz posologia. Para todos os dezoito, a referência válida é a bula do país de registro — russa, "
            "letã ou francesa, conforme o caso — e não uma tabela montada aqui por tradução de revendedor.",
            "Nove compostos estão marcados como <em>não conferido</em> na coluna de ensaios randomizados: fiz a "
            "contagem total no PubMed para todos, mas não rodei o filtro de tipo de publicação em cada um. E dos 29 "
            "ensaios registrados, examinei 20 — os 9 restantes estão contados no total, mas não foram lidos.",
        ]),
    ],
    referencias=[
        ("Kuzuhara S. [Iatrogenic diseases in the elderly]. Nihon Ronen Igakkai Zasshi. 1991;28(4):493-8. PMID 1942629 — a fonte dos 47 casos e 11 mortes por encefalopatia associada ao hopantenato de cálcio.",
         "https://pubmed.ncbi.nlm.nih.gov/1942629/"),
        ("Noda S. [Delayed type malignant syndrome and Parkinson's syndrome due to tiapride, Reye-like syndrome induced by calcium hopantenate]. Ryoikibetsu Shokogun Shirizu. 1999;(27 Pt 2):538-41. PMID 10434717",
         "https://pubmed.ncbi.nlm.nih.gov/10434717/"),
        ("Ensaios de fase 3 do Actovegin: NCT01582854 (Takeda, 503 participantes) e NCT00483730 (Nycomed, 569 participantes).",
         "https://clinicaltrials.gov/study/NCT01582854"),
        ("Ensaios registrados do bloco, consultados por intervenção no ClinicalTrials.gov em 4 de setembro de 2026: 29 no total, 20 examinados.",
         "https://clinicaltrials.gov/search?intr=Mexidol%20OR%20Cytoflavin%20OR%20Actovegin%20OR%20Polyoxidonium"),
        ("Contagens do PubMed obtidas em 4 de setembro de 2026, uma consulta por composto.",
         "https://pubmed.ncbi.nlm.nih.gov/"),
    ],
),
}
