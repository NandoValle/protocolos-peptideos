# -*- coding: utf-8 -*-
"""Auditoria das tabelas de GLP-1 do site contra as bulas oficiais.

Bulas lidas em 04/09/2026 pela API da openFDA e pelo DailyMed (NLM):
  Wegovy injecao + comprimido  setid ee06186f-2aa3-4990-a760-757579d8f77b, 30/06/2026
  Rybelsus / Ozempic comprimidos  vigencia 30/01/2026
  Mounjaro  vigencia 29/07/2026
  Zepbound  vigencia 28/08/2026
"""

GLP1 = {
"proprio_glp1_bula": dict(
    secoes=[
        dict(h="Por que esta página existe", tipo="p", corpo=[
            "As outras páginas de fonte primária deste site respondem <em>quanta evidência existe</em>. Esta "
            "responde outra coisa, e mais direta: <strong>as tabelas de dose que este site publica estão certas?</strong>",
            "Até aqui, a garantia que eu dava era que os números foram transportados da fonte sem serem "
            "reinterpretados. Isso garante que eu copiei certo. <strong>Não garante que a fonte estava certa</strong>, "
            "e essa distinção nunca tinha sido testada em página nenhuma.",
            "Os GLP-1 são o único grupo do site onde dá para testar, porque são os únicos com <strong>bula "
            "aprovada por agência</strong>. Peguei as bulas oficiais na base da FDA e do DailyMed em 4 de setembro "
            "de 2026 e comparei degrau por degrau. O resultado tem duas metades bem diferentes.",
        ]),
        dict(h="Primeira metade: os números batem", tipo="p", corpo=[
            "Esta é a parte boa, e é a maior. <strong>Nenhuma escada de titulação do site está errada em valor de "
            "dose.</strong> Conferi as cinco, degrau por degrau.",
        ], tabela=dict(
            cap="Escadas de titulação — site contra bula",
            linhas=[
                ["Produto", "O que o site publica", "O que a bula diz", "Veredito"],
                ["Wegovy injetável", "0,25 → 0,5 → 1 → 1,7 → 2,4 mg/semana, degraus de 4 semanas, manutenção na semana 17",
                 "Tabela 1: semanas 1–4 / 5–8 / 9–12 / 13–16 / 17 em diante, exatamente esses valores",
                 "<strong>Idêntico</strong>"],
                ["Wegovy comprimido", "1,5 → 4 → 9 → 25 mg/dia",
                 "Tabela 2: dias 1–30 / 31–60 / 61–90 / 91 em diante, esses mesmos valores",
                 "<strong>Valores corretos</strong>, prazo comprimido em 6 dias"],
                ["Rybelsus", "3 → 7 → 14 mg/dia",
                 "Dias 1–30 / 31–60 / 61 em diante, com 14 mg <strong>só se precisar</strong> de mais controle glicêmico",
                 "<strong>Valores corretos</strong>, prazo comprimido em 6 dias"],
                ["Ozempic comprimido", "1,5 → 4 → 9 mg/dia",
                 "Dias 1–30 / 31–60 / 61 em diante, com 9 mg <strong>só se precisar</strong>",
                 "<strong>Valores corretos</strong>, prazo comprimido em 6 dias"],
                ["Tirzepatida (Mounjaro e Zepbound)", "2,5 → 5 → 7,5 → 10 → 12,5 → 15 mg/semana, degraus de 4 semanas",
                 "Início 2,5 mg por 4 semanas, depois incrementos de 2,5 mg a cada <strong>no mínimo</strong> 4 semanas, máximo 15 mg",
                 "<strong>Idêntico</strong>"],
            ])),
        dict(h="E o site acertou uma coisa difícil", tipo="p", corpo=[
            "A tabela da tirzepatida marca 7,5 mg e 12,5 mg como <em>fase de transição</em>, e 5 mg e 10 mg como "
            "doses de manutenção. Isso está certo e quase ninguém acerta: a bula do Zepbound diz que a manutenção "
            "recomendada é <strong>5, 10 ou 15 mg</strong> — 7,5 e 12,5 existem só para subir a escada, não para "
            "ficar. E diz também que <strong>2,5 mg não é aprovada como manutenção</strong>, o que o site já "
            "escrevia.",
            "A regra de segurar o degrau também está certa nos dois lados: o site manda acrescentar 4 semanas em "
            "qualquer degrau intolerável, e a bula diz literalmente para considerar adiar o escalonamento por 4 "
            "semanas quando o paciente não tolera.",
        ]),
        dict(h="Segunda metade: seis coisas faltando", tipo="p", corpo=[
            "Nenhuma delas é número errado. Todas são <strong>instrução da bula que o site não traz</strong> — e "
            "três mudam decisão.",
        ], tabela=dict(
            cap="O que a bula manda e o site não dizia",
            linhas=[
                ["Falta", "O que a bula diz", "Por que importa"],
                ["<strong>1,7 mg é dose de manutenção, não só degrau</strong>",
                 "A manutenção do Wegovy injetável é <strong>1,7 mg ou 2,4 mg</strong>, com 2,4 recomendada. Vale para redução de peso e para risco cardiovascular",
                 "O site tratava 1,7 como um degrau a caminho de 2,4. Quem não tolera 2,4 tem uma <strong>opção aprovada de parar em 1,7</strong> — e não sabia disso lendo esta página"],
                ["<strong>A instrução de troca de via</strong>",
                 "Quem não tolera os 25 mg do comprimido deve considerar mudar para <strong>Wegovy injetável 1,7 mg por semana</strong>",
                 "É a única saída que a bula oferece a quem não suporta o oral. Não estava em lugar nenhum do site"],
                ["<strong>Apneia do sono só com 10 ou 15 mg</strong>",
                 "Na apneia obstrutiva do sono, o Zepbound tem manutenção de <strong>10 ou 15 mg</strong> — 5 mg não serve para essa indicação",
                 "O site citava a indicação de apneia sem a restrição de dose. Quem parasse em 5 mg estaria tratando obesidade, não apneia"],
                ["<strong>Ozempic também é comprimido</strong>",
                 "Desde a bula de janeiro de 2026, Ozempic é injetável <strong>e</strong> comprimido, com escada própria (1,5 → 4 → 9 mg). A bula avisa que <strong>Rybelsus e Ozempic comprimidos não são intercambiáveis miligrama a miligrama</strong>",
                 "São dois comprimidos de semaglutida, do mesmo fabricante, com escadas diferentes. Trocar um pelo outro pela miligrama é erro que a bula antecipa"],
                ["<strong>Máximo pediátrico da tirzepatida</strong>",
                 "Em criança de 10 anos ou mais, o máximo do Mounjaro é <strong>10 mg</strong> por semana, não 15",
                 "A tabela do site termina em 15 mg sem ressalva de idade"],
                ["<strong>Os degraus orais são de 30 dias</strong>",
                 "Dias 1–30, 31–60, 61–90, 91 em diante — não semanas 1–4, 5–8, 9–12, 13 em diante",
                 "A diferença é de 6 dias na chegada aos 25 mg. Pequena, mas a escada existe justamente para reduzir efeito gastrointestinal: encurtá-la vai na direção contrária"],
            ])),
        dict(h="A falha maior, e não é de dose", tipo="p", corpo=[
            "Procurei nas nove páginas de GLP-1 deste site — semaglutida, tirzepatida, retatrutida, cagrilintida, "
            "survodutida, CagriSema e as três combinações — por <em>tireoide</em>, <em>medular</em>, <em>NEM 2</em>, "
            "<em>pancreatite</em>, <em>vesícula</em>, <em>retinopatia</em>, <em>gastroparesia</em>, "
            "<em>anestesia</em> e <em>gravidez</em>.",
            "<strong>Zero ocorrências. Nenhuma delas, em nenhuma das nove páginas.</strong>",
            "Semaglutida e tirzepatida carregam <strong>tarja preta</strong> — a advertência mais forte que a FDA "
            "aplica a um medicamento. A advertência é de <strong>tumor de células C da tireoide</strong>, "
            "dose-dependente e tempo-dependente em roedor, com relevância humana não determinada. E carregam uma "
            "<strong>contraindicação absoluta</strong>: história pessoal ou familiar de carcinoma medular de "
            "tireoide, ou neoplasia endócrina múltipla tipo 2.",
            "Contraindicação absoluta não é advertência. Não é \"tome cuidado\" nem \"converse com seu médico\". É "
            "<strong>não use</strong>. E este site publicava a escada de titulação completa e a tabela de "
            "reconstituição frasco a frasco, sem uma linha sobre ela.",
            "Não é erro de tradução, nem da fonte secundária: é o que <strong>nenhuma das duas</strong> trouxe, e "
            "eu não conferi antes de publicar. É a falha mais grave que este site já teve, e ela estava no ar.",
        ]),
        dict(h="O que a tarja preta diz, em português", tipo="p", corpo=[
            "Tradução direta do texto das bulas do Wegovy, do Mounjaro, do Zepbound e do Rybelsus/Ozempic "
            "comprimidos, que trazem a mesma advertência com a molécula trocada:",
        ], tabela=dict(
            cap="Tarja preta e contraindicações — semaglutida e tirzepatida",
            linhas=[
                ["Item", "O que a bula estabelece"],
                ["<strong>Tarja preta</strong>",
                 "Em roedores, a substância causa tumores de células C da tireoide de forma dependente da dose e da duração do tratamento, em exposições clinicamente relevantes. <strong>Não se sabe se causa em humanos</strong>, incluindo carcinoma medular de tireoide — a relevância humana dos tumores de roedor não foi determinada"],
                ["<strong>Contraindicação absoluta</strong>",
                 "História <strong>pessoal ou familiar</strong> de carcinoma medular de tireoide, ou neoplasia endócrina múltipla tipo 2 (NEM 2)"],
                ["<strong>Segunda contraindicação</strong>",
                 "Reação de hipersensibilidade grave prévia à substância ou a qualquer excipiente. Já foram relatadas <strong>anafilaxia e angioedema</strong> com semaglutida e com tirzepatida"],
                ["<strong>Quem prescreve deve orientar</strong>",
                 "A bula manda o profissional aconselhar o paciente sobre o risco potencial de carcinoma medular de tireoide e sobre os sintomas de tumor de tireoide"],
            ])),
        dict(h="Os três que não têm bula nenhuma", tipo="p", corpo=[
            "Retatrutida, cagrilintida e survodutida: procurei na base de rótulos da FDA e <strong>nenhum dos três "
            "tem registro</strong>. A afirmação que o site já fazia — investigacional, em fase 3 — está confirmada.",
            "O que isso significa na prática é o contrário do que parece. Não é que sejam mais seguros por não terem "
            "tarja preta. É que <strong>não existe autoridade nenhuma para dizer qual é a dose certa</strong>: não "
            "há escada aprovada, não há máximo definido, não há lista de contraindicação. As tabelas desses três no "
            "site vêm inteiramente da fonte secundária e não têm com o que ser comparadas.",
        ], tabela=dict(
            cap="Situação regulatória e ensaios verificados",
            linhas=[
                ["Composto", "Rótulo na FDA", "O que confirmei no ClinicalTrials.gov"],
                ["Retatrutida", "<strong>Nenhum</strong>",
                 "Fase 3 em curso. TRIUMPH-4 é o NCT05931367, concluído, 445 participantes. Há também um ensaio de desfecho cardiovascular e renal com <strong>10.000</strong> participantes (NCT06383390) e uma comparação direta com tirzepatida (NCT06662383, 800)"],
                ["Cagrilintida (e CagriSema)", "<strong>Nenhum</strong>",
                 "Fase 3 em curso. REDEFINE 3 é o NCT05669755, com <strong>7.101</strong> participantes, e há um ensaio concluído em diabetes tipo 2 com 1.200"],
                ["Survodutida", "<strong>Nenhum</strong>",
                 "Programa clínico ativo, com vários estudos de fase 1 concluídos, inclusive de formulação e de gasto energético"],
            ])),
        dict(h="O que muda no site a partir daqui", tipo="li", corpo=[
            "<strong>As nove páginas de GLP-1 passam a trazer um aviso no topo</strong>, com a tarja preta e a "
            "contraindicação absoluta, e o link para esta página.",
            "<strong>As escadas de dose continuam como estão</strong>, porque estão certas. O que muda é o que vai "
            "junto delas.",
            "<strong>Este método vale para pouca coisa do resto do site.</strong> Dos 65 compostos, quase nenhum tem "
            "bula: é o que torna os GLP-1 auditáveis e o resto, não. Onde não há bula, não há gabarito — e essa é a "
            "situação normal desta referência, não a exceção.",
            "<strong>A lição não é sobre GLP-1.</strong> É que \"o número foi preservado da fonte\" e \"o número "
            "está certo\" são afirmações diferentes, e só a primeira valia para este site até hoje.",
        ]),
        dict(h="O que esta auditoria não fez", tipo="li", corpo=[
            "<strong>Não conferi as tabelas de reconstituição.</strong> Elas são aritmética de diluição, não "
            "posologia de bula — nenhuma bula descreve reconstituir frasco de peptídeo com água bacteriostática, "
            "porque o produto aprovado já vem pronto em caneta.",
            "<strong>Usei a bula da FDA, não a da ANVISA.</strong> As duas não são idênticas, e as indicações "
            "aprovadas no Brasil podem ser menos amplas. Onde houver diferença, <strong>a bula brasileira é a que "
            "vale aqui</strong>.",
            "<strong>Não auditei as seções de interação medicamentosa nem de populações especiais.</strong> Fiquei "
            "na posologia, na tarja preta e nas contraindicações.",
            "<strong>Não li os ensaios citados nas tabelas do site</strong> — STEP 1, SURMOUNT-1, OASIS 4, TRIUMPH-4. "
            "Confirmei que TRIUMPH-4 existe e o número de participantes; os percentuais de perda de peso continuam "
            "vindo da fonte secundária.",
        ]),
    ],
    referencias=[
        ("Bula do Wegovy (injeção e comprimido), Novo Nordisk, publicada em 30 de junho de 2026. Fonte das Tabelas 1 e 2 de titulação e da tarja preta.",
         "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ee06186f-2aa3-4990-a760-757579d8f77b"),
        ("Bula conjunta de Rybelsus e Ozempic comprimidos, vigência de 30 de janeiro de 2026, com a advertência de que os dois não são intercambiáveis miligrama a miligrama.",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=RYBELSUS"),
        ("Bula do Mounjaro (tirzepatida), vigência de 29 de julho de 2026 — origem do máximo pediátrico de 10 mg.",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=MOUNJARO"),
        ("Bula do Zepbound (tirzepatida), vigência de 28 de agosto de 2026 — origem das doses de manutenção de 5, 10 e 15 mg e da restrição a 10 ou 15 mg na apneia do sono.",
         "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=ZEPBOUND"),
        ("API pública de rótulos da FDA, usada para confirmar a ausência de registro de retatrutida, cagrilintida e survodutida.",
         "https://open.fda.gov/apis/drug/label/"),
        ("Registros de ensaio conferidos no ClinicalTrials.gov: NCT05931367 (TRIUMPH-4), NCT06383390, NCT06662383 e NCT05669755 (REDEFINE 3).",
         "https://clinicaltrials.gov/study/NCT05931367"),
        ("Bulário eletrônico da ANVISA — a referência que vale no Brasil, e que não foi usada nesta auditoria.",
         "https://consultas.anvisa.gov.br/#/bulario/"),
    ],
),
}
