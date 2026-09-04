# -*- coding: utf-8 -*-
"""Os 18 medicamentos do leste europeu do catalogo de importacao.

Contagens conferidas no PubMed e no ClinicalTrials.gov em 04/09/2026.
"""

from datas import DATA_APURACAO as _DT

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
            f"PubMed e ClinicalTrials.gov, consultados em {_DT}, um composto por vez.",
            "A coluna <strong>Consulta</strong> traz o termo exato que produziu o número ao lado. Copie no PubMed e o resultado tem que ser o mesmo — se não for, o número aqui está velho, e o que vale é o que a base devolver a você.",
            "A coluna <strong>ECR/meta</strong> é a mesma consulta somada ao filtro "
            "<code>Randomized Controlled Trial[Publication Type] OR Meta-Analysis[Publication Type]</code>. "
            "No ClinicalTrials.gov a busca foi por intervenção, com os mesmos sinônimos.",
        ], tabela=dict(
            cap="Evidência por composto",
            linhas=[
                ["Composto", "O que é", "Consulta no PubMed", "Artigos no PubMed", "ECR/meta", "Ensaio registrado"],
                ["Mexidol", "Etilmetilhidroxipiridina succinato (emoxipina)", "<code>mexidol OR emoxypine OR \"ethylmethylhydroxypyridine succinate\"</code>", "614", "59", "Sim — 6 vistos, fases 2 a 4"],
                ["Cytoflavin", "Ácido succínico + inosina + nicotinamida + riboflavina", "<code>cytoflavin</code>", "309", "59", "Sim — 5 vistos, fase 3"],
                ["Actovegin", "Hemoderivado desproteinizado de sangue de bezerro", "<code>actovegin</code>", "180", "26", "Sim — 2 de fase 3, patrocínio ocidental"],
                ["Pantogam / Pantocalcin", "Ácido hopantênico / hopantenato de cálcio", "<code>pantogam OR \"hopantenic acid\" OR \"calcium hopantenate\"</code>", "165", "7", "não visto"],
                ["Afobazol", "Fabomotizol, ansiolítico não benzodiazepínico", "<code>afobazole OR fabomotizole</code>", "158", "5", "Sim — 1, fase 4, recrutando"],
                ["Neuromidin", "Ipidacrina (amiridina), inibidor de colinesterase", "<code>neuromidin OR ipidacrine OR amiridine</code>", "148", "19", "não visto"],
                ["Cortexin", "Polipeptídeos corticais bovinos", "<code>cortexin</code>", "217", "19", "não visto"],
                ["Stresam", "Etifoxina, ansiolítico", "<code>stresam OR etifoxine</code>", "118", "12", "Sim — 2, incluindo comparação com lorazepam"],
                ["Polyoxidonium", "Azoximer brometo, imunomodulador", "<code>polyoxidonium OR azoximer</code>", "98", "6", "Sim — 3, incluindo fase 2/3 em covid com 394 participantes"],
                ["Picamilon", "Nicotinoil-GABA", "<code>picamilon OR \"nicotinoyl-GABA\"</code>", "56", "3", "não visto"],
                ["Derinat", "Desoxirribonucleato de sódio", "<code>derinat OR \"sodium deoxyribonucleate\"</code>", "43", "1", "não visto"],
                ["Nanotropil", "Fenilpiracetam (fonturacetam, carfedon)", "<code>phenylpiracetam OR fonturacetam OR carphedon OR nanotropil</code>", "34", "2", "não visto"],
                ["Galavit", "Aminodihidroftalazinediona sódica", "<code>galavit OR \"aminodihydrophthalazinedione\"</code>", "29", "2", "não visto"],
                ["Memoprove", "N-PEP-12, derivado peptídico", "<code>\"N-PEP-12\" OR memoprove</code>", "16", "3", "não visto"],
                ["Etoxidol", "Etilmetilhidroxipiridina malato", "<code>etoxidol OR \"ethylmethylhydroxypyridine malate\"</code>", "11", "0", "não visto"],
                ["Cocarboxilase", "Tiamina pirofosfato", "<code>cocarboxylase OR \"thiamine pyrophosphate\"</code>", "3301", "24", "não visto"],
                ["Citocromo C", "Citocromo c injetável", "<code>\"cytochrome c\"</code>", "62067", "95", "não visto"],
                ["Meldonium", "Já tem página própria nesta referência", "<code>meldonium OR mildronate</code>", "357", "22", "Sim — 7"],
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
            "A coluna de ensaios randomizados está fechada para os dezoito. Fechá-la mudou três coisas. <strong>Cortexin "
            "estava com o total errado</strong>: a página trazia 26 artigos e a contagem real é <strong>127</strong> "
            "restrita ao fármaco, com 16 ensaios randomizados, entre eles estudos multicêntricos em AVC isquêmico. "
            "O erro era meu, não da fonte. <strong>Cocarboxilase e citocromo C ficaram em zero</strong>: abri os "
            "resultados e nenhum é do injetável — são bioquímica do metabolismo e da apoptose, exatamente o que a "
            "marca de contagem inflada já indicava. E <strong>Etoxidol não tem nenhum ensaio randomizado</strong>: "
            "os onze artigos são todos pré-clínicos, em rato e em cultura.",
            "Dos 29 ensaios registrados, examinei 20 — os 9 restantes continuam contados no total e não foram lidos.",
        ]),
    ],
    referencias=[
        ("Kuzuhara S. [Iatrogenic diseases in the elderly]. Nihon Ronen Igakkai Zasshi. 1991;28(4):493-8. PMID 1942629 — a fonte dos 47 casos e 11 mortes por encefalopatia associada ao hopantenato de cálcio.",
         "https://pubmed.ncbi.nlm.nih.gov/1942629/"),
        ("Noda S. [Delayed type malignant syndrome and Parkinson's syndrome due to tiapride, Reye-like syndrome induced by calcium hopantenate]. Ryoikibetsu Shokogun Shirizu. 1999;(27 Pt 2):538-41. PMID 10434717",
         "https://pubmed.ncbi.nlm.nih.gov/10434717/"),
        ("Ensaios de fase 3 do Actovegin: NCT01582854 (Takeda, 503 participantes) e NCT00483730 (Nycomed, 569 participantes).",
         "https://clinicaltrials.gov/study/NCT01582854"),
        (f"Ensaios registrados do bloco, consultados por intervenção no ClinicalTrials.gov em {_DT}: 29 no total, 20 examinados.",
         "https://clinicaltrials.gov/search?intr=Mexidol%20OR%20Cytoflavin%20OR%20Actovegin%20OR%20Polyoxidonium"),
        (f"Contagens do PubMed obtidas em {_DT}, uma consulta por composto.",
         "https://pubmed.ncbi.nlm.nih.gov/"),
    ],
),
}
