# -*- coding: utf-8 -*-
"""Pagina de doenca renal: o que mudou entre 2021 e 2026.

Entra aqui pelo mesmo motivo da pagina de CRISPR: e um caso onde a promessa
virou medicamento aprovado, e ver o preco disso em evidencia calibra a leitura
do resto do site. A diferenca e que aqui ha seis medicamentos, nao um -- e a
pergunta que os separa (proteinuria ou funcao renal?) e exatamente a pergunta
que este site faz a cada tabela de dose.

Todos os numeros foram levantados em fonte primaria: PubMed, ClinicalTrials.gov,
paginas de aprovacao da FDA e o dado aberto de medicamentos da ANVISA.
"""

from datas import DATA_APURACAO as _DT

RIM = {

"proprio_rim": dict(
    titulo="Doença renal — desfecho substituto e desfecho real",
    nota_refs=(
        "Os números de literatura vêm do PubMed e do ClinicalTrials.gov; as datas e o tipo de cada "
        "aprovação vêm das páginas da própria FDA e dos comunicados das fabricantes, citados um a um; "
        f"o registro brasileiro vem do dado aberto de medicamentos da ANVISA, baixado em {_DT} "
        "(43.491 registros). Nada aqui foi lido em fonte secundária."
    ),
    secoes=[

# ------------------------------------------------------------------ 0. porque
dict(h="Por que esta página existe num site de peptídeos", tipo="p", corpo=[
    "Porque a nefrologia acabou de fazer, em quatro anos e meio, o que este site passa o tempo inteiro "
    "cobrando: sair de nenhum medicamento aprovado para <strong>seis</strong>, com ensaio de fase 3, "
    "registro em agência e bula. É o oposto exato da situação da maior parte dos compostos catalogados "
    "aqui — e por isso serve de régua.",
    "Mas a régua tem duas marcas, não uma. Cinco dessas seis aprovações se apoiaram, no começo, num "
    "número que <em>não</em> é o que interessa ao paciente: a quantidade de proteína na urina. Só "
    "depois — e não em todos os casos ainda — apareceu a prova de que o rim de fato para de piorar. "
    "A distância entre essas duas coisas é o assunto desta página, e é a mesma distância que separa "
    "\"o marcador melhorou\" de \"a pessoa melhorou\" em qualquer tabela deste site.",
    "E há um achado que fecha o circuito. Consultei o ClinicalTrials.gov procurando ensaios que "
    "usassem os peptídeos desta referência — BPC-157, Epitalon, Thymalin, GHK-Cu, Ipamorelina, MOTS-c, "
    "Humanina — em doença renal. A busca devolveu <strong>dois registros, e nenhum dos dois testa o "
    "peptídeo como tratamento</strong>: num, Humanina e MOTS-c são medidos como marcadores num estudo "
    "de anestesia em transplante renal; no outro, Humanina é dosada no plasma como possível marcador "
    "de lesão renal aguda. Zero ensaios de intervenção. É o contraste inteiro numa linha.",
]),

# ------------------------------------------------------------- 1. de zero a 6
dict(h="De zero a seis, em quatro anos e meio", tipo="p", corpo=[
    "A doença é a <strong>nefropatia por IgA</strong> — glomerulopatia primária mais comum do mundo, "
    "conhecida também como doença de Berger. Até dezembro de 2021 não havia um único medicamento "
    "aprovado especificamente para ela em lugar nenhum: tratava-se com bloqueio do sistema "
    "renina-angiotensina e, na crise, corticoide sistêmico.",
    "Hoje são seis, todos aprovados pela FDA. A coluna que importa é a última.",
], tabela=dict(
    cap="Os seis medicamentos aprovados para nefropatia por IgA",
    linhas=[
        ["Medicamento", "Princípio ativo", "Mecanismo", "1ª aprovação FDA", "Sobre que desfecho"],
        ["Tarpeyo", "budesonida de liberação retardada",
         "corticoide de ação local nas placas de Peyer, onde a IgA anômala é produzida",
         "dezembro de 2021 — <strong>acelerada</strong>", "proteinúria"],
        ["Filspari", "sparsentana",
         "antagonista duplo: receptor de endotelina A e receptor AT<sub>1</sub> de angiotensina II",
         "17 de fevereiro de 2023 — <strong>acelerada</strong>", "proteinúria"],
        ["Fabhalta", "iptacopana",
         "inibidor oral do fator B — via alternativa do complemento",
         "agosto de 2024 — <strong>acelerada</strong>", "proteinúria"],
        ["Vanrafia", "atrasentana",
         "antagonista seletivo do receptor de endotelina A",
         "2 de abril de 2025 — <strong>acelerada</strong>", "proteinúria em 36 semanas"],
        ["Voyxact", "sibeprenlimabe",
         "anticorpo monoclonal anti-APRIL",
         "25 de novembro de 2025 — <strong>acelerada</strong>", "proteinúria em 9 meses"],
        ["Trutakna", "atacicepte",
         "proteína de fusão que bloqueia BAFF e APRIL ao mesmo tempo — primeiro da classe",
         "7 de julho de 2026 — <strong>acelerada</strong>", "proteinúria em 9 meses"],
    ])),

# --------------------------------------------------- 2. o que e aprov acelerada
dict(h="O que \"aprovação acelerada\" quer dizer, na prática", tipo="p", corpo=[
    "É um caminho em que a agência aceita um <strong>desfecho substituto</strong> — um número que se "
    "acredita prever o benefício real — em troca do compromisso de provar o benefício real depois, num "
    "ensaio confirmatório. Se a confirmação não vier, o registro pode ser retirado.",
    "Na nefropatia por IgA o substituto é a proteinúria. O desfecho real é a <strong>taxa de filtração "
    "glomerular estimada (TFGe)</strong> — quanto o rim ainda filtra, e com que velocidade isso cai. "
    "Ninguém morre de proteinúria; morre-se de rim que parou.",
    "Não estou inventando essa ressalva: ela está escrita pela própria FDA, no anúncio de cada "
    "aprovação. Sobre o Voyxact, a agência registra que <em>não foi estabelecido se o medicamento "
    "retarda o declínio da função renal a longo prazo</em>, e que a manutenção do registro depende do "
    "ensaio confirmatório. Sobre o Trutakna, a mesma frase, com as mesmas palavras.",
]),

# ---------------------------------------------------- 3. quem ja provou de fato
dict(h="Quem já saiu do substituto — e quem ainda não saiu", tipo="p", corpo=[
    "Esta é a tabela que separa manchete de resultado. Três dos seis já converteram a aprovação "
    "acelerada em aprovação plena, apresentando efeito sobre a função renal. Três ainda não.",
], tabela=dict(
    cap="Situação de cada um quanto ao desfecho real",
    linhas=[
        ["Medicamento", "Situação hoje", "O que mostrou sobre função renal", "Ensaio confirmatório"],
        ["Fabhalta (iptacopana)",
         "<strong>Aprovação tradicional em 17 de julho de 2026</strong>",
         "APPLAUSE-IgAN, 2 anos: queda anualizada de TFGe de <strong>−3,0</strong> mL/min/1,73 m²/ano "
         "contra <strong>−5,7</strong> no placebo — 48% menos declínio",
         "NCT04578834, concluído em 19/09/2025"],
        ["Filspari (sparsentana)",
         "<strong>Aprovação plena para IgAN em setembro de 2024</strong>",
         "PROTECT, 2 anos: preservação de função renal superior à da irbesartana — único fase 3 "
         "cabeça a cabeça feito na doença",
         "NCT03762850, conclusão primária em 07/08/2023"],
        ["Tarpeyo (budesonida DR)",
         "<strong>Aprovação plena em 20 de dezembro de 2023</strong>",
         "NefIgArd: benefício de cerca de <strong>5 mL/min/1,73 m²</strong> na média ponderada no "
         "tempo da TFGe em 2 anos, contra placebo",
         "NefIgArd, concluído"],
        ["Trutakna (atacicepte)",
         "Acelerada — proteinúria apenas",
         "Redução média de 46% na proteinúria contra placebo em 9 meses. Efeito sobre função renal "
         "<strong>não estabelecido</strong>",
         "ORIGIN 3 — NCT04716231, conclusão primária em 15/05/2025"],
        ["Voyxact (sibeprenlimabe)",
         "Acelerada — proteinúria apenas",
         "Redução de 50% na proteinúria contra aumento de 2% no placebo, em 9 meses. Função renal "
         "<strong>não estabelecida</strong>",
         "VISIONARY — NCT05248646, conclusão primária em 13/05/2026"],
        ["Vanrafia (atrasentana)",
         "Acelerada — proteinúria apenas",
         "Redução percentual de proteína na urina em 36 semanas, em 270 pacientes analisados. Função "
         "renal <strong>não estabelecida</strong>",
         "ALIGN — NCT04573478, conclusão primária prevista para <strong>14/04/2028</strong>"],
    ])),

dict(h="Três coisas que essa tabela ensina, e que valem para o site inteiro", tipo="li", corpo=[
    "<strong>O substituto pode se confirmar — e se confirmou três vezes.</strong> Quem trata "
    "proteinúria como número inútil erra na direção oposta. O ponto não é que o marcador não vale "
    "nada; é que ele vale como <em>aposta</em> até que alguém pague para verificar.",
    "<strong>A verificação demora anos.</strong> A atrasentana foi aprovada em abril de 2025 e o "
    "ensaio que vai dizer se ela preserva rim só fecha a coleta em abril de 2028. São três anos de "
    "prescrição legal apoiada numa hipótese — com registro, bula e reembolso.",
    "<strong>Isso tudo acontece no melhor cenário possível.</strong> Fase 3 multicêntrica, "
    "randomizada, com placebo, centenas de pacientes, agência exigindo confirmação. Se aqui a "
    "distância entre marcador e desfecho ainda leva anos para ser vencida, uma tabela de dose "
    "montada em fórum não está a uma nota de rodapé de distância da evidência — está fora da escala.",
]),

# ------------------------------------------------------------- 4. levantamento
dict(h="O levantamento de literatura", tipo="p", corpo=[
    f"Consultas feitas por mim no PubMed e no ClinicalTrials.gov em {_DT}. A consulta está escrita "
    "para que qualquer pessoa possa repetir e conferir o número.",
], tabela=dict(
    cap="Contagens em fonte primária",
    linhas=[
        ["Base", "Consulta", "Resultado"],
        ["PubMed", "<code>IgA nephropathy</code>", "13.624 artigos"],
        ["PubMed", "<code>atrasentan</code>", "521 artigos"],
        ["PubMed", "<code>iptacopan</code>", "178 artigos"],
        ["PubMed", "<code>sparsentan</code>", "133 artigos"],
        ["PubMed", "<code>sibeprenlimab</code>", "28 artigos"],
        ["PubMed", "<code>atacicept AND IgA nephropathy</code>", "16 artigos"],
        ["ClinicalTrials.gov", "condição <code>IgA nephropathy</code>", "<strong>279 estudos registrados</strong>"],
        ["ClinicalTrials.gov", "fase 3, condição IgAN, com um dos cinco fármacos como intervenção", "10 registros"],
        ["ClinicalTrials.gov",
         "peptídeos desta referência (BPC-157, Epitalon, Thymalin, GHK-Cu, Ipamorelina, MOTS-c, "
         "Humanina) em doença renal",
         "<strong>2 registros, nenhum de intervenção</strong>"],
    ])),

dict(h="O contraste, em números", tipo="p", corpo=[
    "Uma única doença renal tem <strong>279 ensaios registrados</strong>. A família inteira dos "
    "bioreguladores curtos — onze compostos — tem <strong>zero</strong>. O Thymalin, o mais estudado "
    "de toda aquela escola, tem 293 artigos no PubMed e nenhum ensaio registrado; a atrasentana "
    "sozinha tem 521 artigos e um fase 3 com data marcada para responder à pergunta que importa.",
    "Não se trata de dizer que um é bom e o outro é ruim. Trata-se de mostrar o que uma base de "
    "evidência parece quando ela existe — para que a ausência dela, nas outras páginas, tenha com o "
    "que ser comparada.",
]),

# ------------------------------------------------------------------- 5. Brasil
dict(h="O que disso chegou ao Brasil", tipo="p", corpo=[
    f"Varri o dado aberto de medicamentos da ANVISA — 43.491 registros, baixado em {_DT} — "
    "procurando cada um dos seis princípios ativos e cada nome comercial. O resultado:",
], tabela=dict(
    cap="Registro na ANVISA, um a um",
    linhas=[
        ["Princípio ativo", "Produto", "Registro", "Empresa", "Situação"],
        ["cloridrato de atrasentana", "<strong>VANRAFIA</strong>", "100681190 · processo finalizado em 31/08/2026",
         "Novartis Biociências S.A. (56.994.502/0001-30)", "<strong>Ativo</strong>"],
        ["cloridrato de iptacopana monoidratado", "<strong>FABHALTA</strong>", "100681187 · finalizado em 27/01/2025",
         "Novartis Biociências S.A.", "<strong>Ativo</strong>"],
        ["sparsentana", "—", "nenhum registro localizado", "—", "—"],
        ["sibeprenlimabe", "—", "nenhum registro localizado", "—", "—"],
        ["atacicepte", "—", "nenhum registro localizado", "—", "—"],
        ["budesonida de liberação retardada para IgAN", "—",
         "nenhum registro localizado sob os nomes Tarpeyo ou Kinpeygo", "—", "—"],
    ])),

dict(h="Duas ressalvas sobre essa tabela, que não podem ser omitidas", tipo="li", corpo=[
    "<strong>O dado aberto da ANVISA não traz a indicação aprovada.</strong> Ele diz que o FABHALTA "
    "tem registro ativo no Brasil desde janeiro de 2025 — não diz para qual doença. A iptacopana "
    "também é aprovada para hemoglobinúria paroxística noturna e para glomerulopatia por C3, e o "
    "registro brasileiro pode ser de qualquer uma delas. Afirmar que o Brasil tem iptacopana "
    "aprovada <em>para nefropatia por IgA</em> seria dedução, não dado. Não farei isso.",
    "<strong>A ausência no dado aberto não é prova de ausência no país.</strong> Significa que não "
    "há registro de medicamento com aquele nome ou princípio ativo na base — o que é forte, mas não "
    "cobre importação individual, uso compassivo ou petição em análise.",
]),

dict(h="A notícia brasileira de 31 de agosto de 2026", tipo="p", corpo=[
    "A ANVISA aprovou o registro da <strong>Vanrafia (cloridrato de atrasentana)</strong> para "
    "adultos com nefropatia primária por imunoglobulina A em risco de progressão, pela Resolução "
    "RE nº 3.416/2026, publicada no Diário Oficial da União. É o mais novo dos dois — e é, "
    "justamente, um dos três que ainda não provaram efeito sobre a função renal. O ensaio que vai "
    "responder isso fecha em 2028.",
    "Registro isso sem ironia: aprovar sobre desfecho substituto é uma decisão regulatória "
    "defensável quando a doença progride e não há alternativa. O que não é defensável é a notícia "
    "chegar ao paciente sem essa metade da frase.",
]),

# -------------------------------------------------------- 6. fora da glomerulo
dict(h="Fora da glomerulopatia: o que mudou na doença renal crônica comum", tipo="p", corpo=[
    "A maior parte da doença renal do mundo não é nefropatia por IgA — é consequência de diabetes e "
    "hipertensão. Aí o que se consolidou foi uma combinação, não uma molécula: bloqueio do sistema "
    "renina-angiotensina, <strong>inibidor de SGLT2</strong>, <strong>finerenona</strong> e, agora, "
    "<strong>agonista de GLP-1</strong>.",
    "No Brasil, a ANVISA aprovou em 2 de fevereiro de 2026 nova indicação para a "
    "<strong>semaglutida</strong>: diabetes tipo 2 <em>com</em> doença renal crônica, como adjuvante "
    "à terapia padrão, com redução de progressão da insuficiência renal e de mortes por eventos "
    "cardiovasculares graves. A própria ANVISA contextualiza com o dado da Sociedade Brasileira de "
    "Nefrologia de 2024: 29% dos pacientes em diálise no país têm diabetes.",
    "A <strong>finerenona</strong> — antagonista não esteroidal do receptor mineralocorticoide — tem "
    "registro ativo no Brasil como <strong>FIRIALTA</strong> (Bayer S.A., registro 170560129, "
    "processo finalizado em 16/01/2023), conforme o mesmo dado aberto.",
    "A semaglutida já tem página própria nesta referência, montada a partir da bula. A diferença "
    "entre o que a bula autoriza e o que circula como protocolo está lá, não aqui.",
]),

dict(h="E o que falhou — que importa tanto quanto o que deu certo", tipo="p", corpo=[
    "O ensaio <strong>ZEUS</strong>, fase 3 com <strong>ziltivekimabe</strong> — anticorpo anti-IL-6 "
    "— em mais de 6.300 pessoas com aterosclerose, doença renal crônica e inflamação, "
    "<strong>não reduziu eventos cardiovasculares maiores</strong>: razão de risco de "
    "<strong>0,99</strong> (IC 95% 0,88–1,11). O medicamento fez exatamente o que se esperava na "
    "biologia — baixou a IL-6 livre e a PCR ultrassensível — e isso não se traduziu em desfecho. "
    "Mortalidade total inalterada, e infecções graves mais frequentes no grupo tratado.",
    "É o mesmo erro desta página, invertido: um marcador se moveu na direção certa e o paciente não "
    "foi junto. Vale registrar aqui porque a hipótese anti-inflamatória é exatamente o tipo de "
    "raciocínio mecanicista que sustenta metade das alegações de peptídeo — <em>reduz inflamação, "
    "logo protege</em>. Num ensaio de 6.300 pessoas, não protegeu.",
]),

# ---------------------------------------------------------- 7. falencia renal
dict(h="Falência renal: o que é notícia e o que é tratamento", tipo="p", corpo=[
    "Em janeiro de 2026, Tim Andrews recebeu um rim humano de doador falecido depois de viver "
    "<strong>271 dias sem diálise</strong> com um rim de porco geneticamente editado, implantado em "
    "janeiro de 2025. É a maior sobrevida sem diálise já documentada após xenotransplante renal em "
    "pessoa viva, e a primeira transição bem-sucedida de xenotransplante para transplante humano — "
    "a ideia de usar o órgão animal como <em>ponte</em> até o órgão humano aparecer. Publicado no "
    "<em>The Lancet</em> em setembro de 2026.",
    "O mesmo artigo relata o que a manchete não carrega: houve rejeição mediada por células T no "
    "período inicial, que respondeu ao tratamento, e lesão microvascular progressiva com inflamação "
    "depois que a imunossupressão foi reduzida durante uma infecção.",
    "O programa clínico regulado é o <strong>EXPAND</strong> (NCT06878560), da United Therapeutics, "
    "com um rim suíno de dez edições gênicas, em pacientes com doença renal terminal sem perspectiva "
    "de rim humano em cinco anos. O primeiro xenotransplante do protocolo foi feito no NYU Langone "
    "em 3 de novembro de 2025.",
    "Um caso e um ensaio que começou. Não é tratamento disponível, e ninguém deveria lê-lo como tal.",
]),

# ------------------------------------------------------------------ 8. limites
dict(h="O que esta página não autoriza", tipo="li", corpo=[
    "<strong>Nada aqui é aplicável por conta própria.</strong> Todos os seis medicamentos são de "
    "prescrição, vários com programa de acompanhamento obrigatório por hepatotoxicidade ou "
    "imunossupressão. O Filspari é distribuído nos EUA sob programa restrito, com certificação "
    "exigida de quem prescreve e de quem dispensa.",
    "<strong>Não existe peptídeo desta referência com ensaio de intervenção em doença renal.</strong> "
    "Dois registros no ClinicalTrials.gov, ambos usando o peptídeo como <em>marcador medido</em>, não "
    "como tratamento aplicado. Qualquer alegação de \"proteção renal\" por peptídeo vendido como "
    "material de pesquisa não tem, hoje, um ensaio registrado atrás dela.",
    "<strong>Função renal reduzida muda o risco de tudo o mais neste site.</strong> Compostos "
    "eliminados por via renal se acumulam quando o rim filtra menos. Esta página não traz ajuste de "
    "dose para insuficiência renal — e a ausência é deliberada: esse ajuste é decisão clínica com "
    "exame na mão, não tabela de referência.",
]),
    ],
    referencias=[
        ("FDA. FDA approves new treatment for primary immunoglobulin A nephropathy (Voyxact/sibeprenlimabe, aprovação acelerada de 25/11/2025)",
         "https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-new-treatment-primary-immunoglobulin-nephropathy"),
        ("FDA. FDA Approves New Treatment to Reduce Proteinuria in Adults with Primary Immunoglobulin A Nephropathy (Trutakna/atacicepte, aprovação acelerada de 07/07/2026)",
         "https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-new-treatment-reduce-proteinuria-adults-primary-immunoglobulin-nephropathy"),
        ("FDA. Drug Trials Snapshot: VANRAFIA (atrasentana, aprovação acelerada de 02/04/2025, ensaio ALIGN)",
         "https://www.fda.gov/drugs/drug-trials-snapshots/drug-trials-snapshot-vanrafia"),
        ("FDA. First FDA-Approved Treatment for Patients with Focal Segmental Glomerulosclerosis (Filspari, aprovação plena para GESF, 16/04/2026)",
         "https://www.fda.gov/drugs/drug-alerts-and-statements/first-fda-approved-treatment-patients-focal-segmental-glomerulosclerosis-rare-kidney-condition"),
        ("Novartis. Fabhalta (iptacopana) receives FDA traditional approval as first and only complement inhibitor to significantly slow kidney function decline in primary IgAN — 17/07/2026, dados de TFGe do APPLAUSE-IgAN",
         "https://www.novartis.com/news/media-releases/novartis-fabhalta-iptacopan-receives-fda-traditional-approval-first-and-only-complement-inhibitor-significantly-slow-kidney-function-decline-primary-igan"),
        ("Travere Therapeutics. Full FDA Approval of FILSPARI (sparsentana) in IgA Nephropathy — conversão para aprovação plena, estudo PROTECT",
         "https://travere.com/news/travere-therapeutics-announces-full-fda-approval-of-filspari-sparsentan-the-only-non-immunosuppressive-treatment-that-significantly-slows-kidney-function-decline-in-iga-nephropathy/"),
        ("ClinicalTrials.gov. PROTECT — sparsentana em nefropatia por IgA (NCT03762850)",
         "https://clinicaltrials.gov/study/NCT03762850"),
        ("ClinicalTrials.gov. APPLAUSE-IgAN — iptacopana (NCT04578834)",
         "https://clinicaltrials.gov/study/NCT04578834"),
        ("ClinicalTrials.gov. ALIGN — atrasentana, conclusão primária prevista para 14/04/2028 (NCT04573478)",
         "https://clinicaltrials.gov/study/NCT04573478"),
        ("ClinicalTrials.gov. VISIONARY — sibeprenlimabe (NCT05248646)",
         "https://clinicaltrials.gov/study/NCT05248646"),
        ("ClinicalTrials.gov. ORIGIN 3 — atacicepte (NCT04716231)",
         "https://clinicaltrials.gov/study/NCT04716231"),
        ("ANVISA. Novo medicamento para nefropatia primária por imunoglobulina A é aprovado pela Anvisa — Vanrafia, RE nº 3.416/2026, 31/08/2026",
         "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/novo-medicamento-para-nefropatia-primaria-por-imunoglobulina-a-e-aprovado-pela-anvisa"),
        ("ANVISA. Anvisa aprova novas indicações para semaglutida e tezepelumabe — semaglutida em diabetes tipo 2 com doença renal crônica, 02/02/2026",
         "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/anvisa-aprova-novas-indicacoes-para-semaglutida-e-tezepelumabe"),
        ("ANVISA. Dados abertos de medicamentos registrados (DADOS_ABERTOS_MEDICAMENTOS.csv) — base usada para a varredura de registro brasileiro",
         "https://dados.anvisa.gov.br/dados/"),
        ("TCTMD. ZEUS Trial: Ziltivekimab Fails to Reduce MACE in ASCVD Patients — razão de risco 0,99 (IC 95% 0,88–1,11)",
         "https://www.tctmd.com/news/zeus-trial-ziltivekimab-fails-reduce-mace-ascvd-patients"),
        ("Mass General Brigham / The Lancet. Xenotransplante renal como ponte para transplante humano — 271 dias sem diálise, setembro de 2026 (DOI 10.1016/S0140-6736(26)01295-X)",
         "https://doi.org/10.1016/S0140-6736(26)01295-X"),
        ("NYU Langone Health. First Gene-Edited Pig Kidney Transplant Clinical Trial Begins — estudo EXPAND (NCT06878560), primeiro procedimento em 03/11/2025",
         "https://nyulangone.org/news/first-gene-edited-pig-kidney-transplant-clinical-trial-begins-nyu-langone-health"),
        ("National Kidney Foundation. A New Era for IgA Nephropathy: Six New Treatments Bring New Hope",
         "https://www.kidney.org/news-stories/new-era-iga-nephropathy-six-new-treatments-bring-new-hope"),
    ],
),
}
