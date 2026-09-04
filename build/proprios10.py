# -*- coding: utf-8 -*-
"""Varredura do registro sanitario brasileiro, composto a composto.

Fonte: DADOS_ABERTOS_MEDICAMENTOS.csv, dado aberto oficial da ANVISA,
43.489 registros, baixado em 04/09/2026. Busca por principio ativo e por
nome de produto, sem acento e sem caixa, contando so registro Ativo.
"""

from datas import DATA_APURACAO as _DT

ANV = {
"proprio_anvisa": dict(
    secoes=[
        dict(h="A pergunta desta página", tipo="p", corpo=[
            "As outras páginas de fonte primária perguntam <em>quanta evidência existe</em> e <em>a dose está "
            "certa</em>. Esta pergunta a mais simples das três, e a que ninguém responde: "
            "<strong>isso existe legalmente no Brasil?</strong>",
            "A auditoria dos GLP-1 só foi possível porque havia bula. Ao terminá-la, ficou a dúvida óbvia: "
            "<strong>quantos dos compostos deste site têm bula?</strong> Fui contar. Baixei o dado aberto oficial "
            "da ANVISA — <strong>43.489 registros de medicamento</strong> — e procurei cada composto por princípio "
            "ativo e por nome de produto.",
            "O resultado está agora <strong>em cada página de composto</strong>, numa linha logo abaixo do aviso "
            "geral. Esta página é o consolidado e o método.",
        ]),
        dict(h="O número", tipo="p", corpo=[
            "<strong>Dos 44 compostos de protocolo deste site, 40 não têm nenhum medicamento registrado no "
            "Brasil.</strong>",
            "Não é que o registro seja difícil, ou que a ANVISA seja lenta. É que <strong>quase nada disto foi "
            "sequer submetido</strong>. Não há bula brasileira, não há dose aprovada, não há lote fiscalizado e "
            "não há a quem reclamar. O que circula é importação pessoal ou manipulação.",
        ], tabela=dict(
            cap="Resumo da varredura",
            linhas=[
                ["Grupo", "Com registro ativo", "Sem nenhum", "Leitura"],
                ["Peptídeos e compostos de protocolo", "<strong>4</strong>", "<strong>40</strong>",
                 "Semaglutida, tirzepatida, ocitocina e azul de metileno. Todo o resto — BPC-157, TB-500, GHK-Cu, Epitalon, Ipamorelina, MOTS-c, NAD+, Melanotan II, Selank, Semax, retatrutida, cagrilintida, survodutida — <strong>zero</strong>"],
                ["Medicamentos do leste europeu", "<strong>1</strong>", "<strong>17</strong>",
                 "E o único é enganoso: a cocarboxilase aparece como <strong>componente de um polivitamínico injetável</strong> (CERNE-12), não como o produto que se importa"],
                ["Nootrópicos", "<strong>5</strong>", "<strong>9</strong>",
                 "São cinco compostos, não quatro: modafinila (STAVIGILE), armodafinila (NUVIGIL), piracetam (NOOTROPIL), sulbutiamina (ARCALION) e benfotiamina — esta última com <strong>seis produtos</strong> ativos, que é onde a contagem se confundiu. Tianeptina, vinpocetina, oxiracetam, aniracetam, huperzina A, citicolina e alfa-GPC: nenhum"],
                ["Itens de tarja <small>(grupo de controle)</small>", "<strong>4</strong>", "<strong>1</strong>",
                 "Metformina 77, finasterida 27, tadalafila 26, anastrozol 18. Só o <strong>clembuterol</strong> não tem — e é justamente o que a lista original vendia como emagrecedor"],
            ])),
        dict(h="Os quatro que existem", tipo="p", corpo=[
            "Vale olhar de perto, porque três deles surpreendem.",
        ], tabela=dict(
            cap="Compostos do site com medicamento registrado no Brasil",
            linhas=[
                ["Composto", "Registros ativos", "Produtos", "O que isso diz"],
                ["<strong>Semaglutida</strong>", "<strong>15</strong>",
                 "OZEMPIC, WEGOVY, RYBELSUS, EXTENSIOR, POVIZTRA, SEMAVY, ORSEMA, SEEMASUN, SEMACLIQUE, YLUMÉC, OWOZY, OZIVY, ZEMPNEO e dois genéricos chamados SEMAGLUTIDA",
                 "<strong>O achado mais inesperado da varredura.</strong> Já existem <strong>genérico e similar</strong> de semaglutida registrados — EMS, Germed, Sun, Ranbaxy, Cosmed, Brainfarma. A Novo Nordisk tem cinco, não três: além dos conhecidos, EXTENSIOR e POVIZTRA"],
                ["<strong>Tirzepatida</strong>", "<strong>2</strong>", "MOUNJARO e MOUNJARO MULTIDOSE",
                 "Marca única, sem genérico. O MULTIDOSE é apresentação, não molécula nova"],
                ["<strong>Ocitocina</strong>", "<strong>3</strong>", "OCITOCINA, OXITON, SYNTOCINON",
                 "Existe há décadas — mas como <strong>uterotônico injetável de uso hospitalar</strong>. Não tem relação com o uso social ou comportamental que circula em protocolo"],
                ["<strong>Azul de metileno</strong>", "4 registrados<br><small>+ 9 notificados</small>",
                 "CYSTEX, CYSTEX DUO, SEPURIN, PILULAS DE LUSSEN — e nove soluções a 1% apenas <strong>notificadas</strong>",
                 "Os registrados são <strong>combinações para trato urinário</strong>, não azul de metileno isolado. As soluções a 1% entram por <strong>notificação</strong>, a via de baixo risco, que não passa pela mesma análise de um registro"],
            ])),
        dict(h="Registro e notificação não são a mesma coisa", tipo="p", corpo=[
            "A base tem duas situações que parecem iguais e não são. <strong>Registro</strong> passa por análise de "
            "eficácia, segurança e qualidade, e recebe um número. <strong>Notificação</strong> é a via de baixo "
            "risco: o fabricante comunica, e o produto entra sem o mesmo escrutínio — na base ele aparece "
            "<strong>sem número de registro</strong>.",
            "Isso deu trabalho, e quase estragou a conta. Como os notificados não têm número, uma primeira versão "
            "desta varredura os agrupou todos numa linha só e <strong>subcontou o azul de metileno</strong>. "
            "Corrigi separando as duas colunas. Onde a página diz <em>notificado</em>, é isso que quer dizer.",
        ]),
        dict(h="Como conferir o que está aqui", tipo="p", corpo=[
            "O método inteiro cabe em três passos, e qualquer pessoa pode repetir:",
        ], tabela=dict(
            cap="O método, para ser refeito",
            linhas=[
                ["Passo", "O que fiz"],
                ["<strong>1. Fonte</strong>",
                 f"Baixei <code>DADOS_ABERTOS_MEDICAMENTOS.csv</code> do portal de dados abertos da ANVISA em {_DT}. São <strong>43.489 linhas</strong>, com princípio ativo, nome do produto, categoria regulatória, empresa e situação do registro"],
                ["<strong>2. Busca</strong>",
                 "Para cada composto, procurei o termo no princípio ativo <em>e</em> no nome do produto, sem acento e sem diferença de caixa, contando só o que está com situação <strong>Ativo</strong>. Registro inativo aparece na base e foi descartado"],
                ["<strong>3. Controle</strong>",
                 "<strong>Esta é a parte que valida o resto.</strong> Antes de acreditar em qualquer zero, testei o método com coisas que obrigatoriamente existem: insulina, dipirona e azul de metileno. As três voltaram positivas. E incluí um grupo de controle inteiro — os itens de tarja —, que voltou com 4 de 5"],
            ])),
        dict(h="O caminho errado, que vale registrar", tipo="p", corpo=[
            "A primeira tentativa foi pelo <strong>bulário eletrônico</strong>, que é a consulta óbvia. Ela devolveu "
            "<strong>zero para quarenta compostos</strong>, e eu quase publiquei isso.",
            "O que salvou foi o controle: rodei <em>insulina</em> no bulário e <strong>também deu zero</strong>. "
            "Insulina, obviamente, é registrada no Brasil. O bulário busca por <strong>nome de produto</strong>, e "
            "insulina se vende como Lantus, Humalog, Tresiba — o nome da substância não casa com nada.",
            "<strong>Quarenta zeros certos pelo motivo errado ainda são um resultado inválido.</strong> Foi só ao "
            "trocar para o dado aberto, que traz o princípio ativo em coluna própria, que os zeros passaram a "
            "significar alguma coisa.",
        ]),
        dict(h="O que 'sem registro' quer dizer, e o que não quer", tipo="li", corpo=[
            "<strong>Quer dizer:</strong> não existe medicamento com aquele princípio ativo aprovado para venda no "
            "Brasil. Sem bula brasileira, sem posologia aprovada, sem fiscalização de lote e sem responsável legal.",
            "<strong>Não quer dizer que a substância seja ilegal de possuir.</strong> Importação pessoal em pequena "
            "quantidade tem regra própria, e não é o assunto desta página.",
            "<strong>Não quer dizer que não exista em outra categoria.</strong> O dado aberto usado aqui lista "
            "medicamentos. Suplemento alimentar, cosmético e produto para saúde têm bases separadas e ficaram de "
            "fora — é por isso que creatina e vitamina D não aparecem, embora sejam legais e comuns.",
            "<strong>Não quer dizer que não funcione.</strong> Registro é decisão regulatória, não veredito "
            "científico. As páginas de evidência deste site respondem a outra pergunta, e às vezes discordam desta.",
        ]),
        dict(h="O que esta varredura não fez", tipo="li", corpo=[
            "<strong>Não conferi as bulas dos que têm registro</strong>, salvo os quatro GLP-1 da auditoria "
            "anterior. Saber que existe registro não é saber o que a bula diz.",
            "<strong>Não busquei sinônimo químico exaustivamente.</strong> Usei o nome corrente, o nome comercial "
            "conhecido e a denominação em português. Se algum composto está registrado sob um sinônimo que não "
            "testei, ele aparece aqui como zero — e seria erro meu.",
            "<strong>Não conferi as bases de suplemento e de produto para saúde</strong>, que são separadas.",
            "<strong>Não olhei situação de importação nem RDC aplicável.</strong> A página responde se existe "
            "registro, e só.",
        ]),
    ],
    nota_refs=('Cada número desta página veio do dado aberto oficial da ANVISA, baixado em 4 de setembro '
              'de 2026, contando apenas registros com situação Ativo. <strong>Esta página não usa o PubMed</strong> — '
              'a pergunta dela é regulatória, não de evidência.'),
    referencias=[
        (f"Dados abertos da ANVISA, arquivo DADOS_ABERTOS_MEDICAMENTOS.csv, baixado em {_DT} com 43.489 registros. É a fonte de toda a contagem desta página.",
         "https://dados.anvisa.gov.br/dados/"),
        ("Bulário eletrônico da ANVISA — a consulta que falhou no controle e foi descartada como método, mas que serve para ler a bula de quem tem registro.",
         "https://consultas.anvisa.gov.br/#/bulario/"),
        ("Consulta a medicamentos registrados da ANVISA, usada para conferir categoria regulatória e vencimento dos registros de semaglutida e tirzepatida.",
         "https://consultas.anvisa.gov.br/#/medicamentos/"),
        ("Auditoria dos GLP-1 contra as bulas da FDA e da ANVISA, que originou esta varredura.",
         "proprio_glp1_bula.html"),
    ],
),
}
