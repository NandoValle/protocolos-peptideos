# -*- coding: utf-8 -*-
"""Pagina de tamanho de efeito, montada de fonte primaria.

Complementa build/proprios7.py: aquela pagina conta quantos ensaios existem,
esta abre o que os ensaios acharam. Trinta e quatro metanalises e ensaios
grandes lidos no PubMed em 04/09/2026; todo tamanho de efeito foi transportado
do resumo do proprio estudo, nao calculado nem estimado aqui.
"""

EFEITO = {
"proprio_efeito": dict(
    secoes=[
        dict(h="Como ler esta página", tipo="p", corpo=[
            "A <a href=\"proprio_nootropicos.html\">página de nootrópicos</a> responde <em>quantos ensaios "
            "existem</em>. Ela mesma declara o limite disso: a ordem lá é por quantidade de evidência, não por "
            "quanto funciona. Esta página é a outra metade — <strong>o que os ensaios acharam</strong>.",
            "Cada linha traz o tamanho de efeito como o próprio estudo o publicou: SMD, Hedge's <em>g</em>, "
            "Cohen's <em>d</em> ou diferença média, com intervalo de confiança quando o resumo o traz. "
            "<strong>Nada foi calculado, convertido ou estimado aqui.</strong> Onde o estudo declarou a certeza "
            "GRADE, ela está transcrita.",
            "Para calibrar a leitura: em desfecho cognitivo, SMD de 0,2 é pequeno e 0,5 é moderado. Quase tudo "
            "que sobrevive a uma metanálise nesta área fica <strong>entre 0,2 e 0,4</strong> — não é uma mudança "
            "que se perceba sem teste padronizado, é uma mudança que aparece em média, em grupo.",
            "A ordem das faixas é por <strong>a quem a evidência se aplica</strong>, e não por magnitude. Esse é "
            "o achado principal do levantamento, e está explicado na última seção.",
        ]),
        dict(h="Faixa A — metanálise em pessoa saudável", tipo="p", corpo=[
            "O único grupo em que existe evidência agregada de efeito em quem <strong>não</strong> está doente. "
            "É uma lista curta, e dois dos itens dela são negativos.",
        ], tabela=dict(
            cap="Compostos com metanálise em população saudável ou não demente",
            linhas=[
                ["Composto", "Tamanho de efeito publicado", "Base", "Ressalva"],
                ["Creatina monoidratada", "Memória <strong>SMD 0,31</strong> (IC 0,18–0,44). Certeza GRADE <strong>moderada</strong>",
                 "16 ECRs, 492 pessoas",
                 "<strong>A certeza mais alta desta página inteira.</strong> Sem efeito em função executiva nem em cognição global"],
                ["Creatina — o recorte que importa", "Memória <strong>SMD 0,88</strong> (IC 0,22–1,55) em 66–76 anos contra <strong>0,03, não significativo</strong>, em 11–31 anos",
                 "Metanálise separada, 10 ECRs",
                 "Dose de 2,2 a 20 g/dia e duração de 5 dias a 24 semanas <strong>não mudaram o resultado</strong>. O que muda é a idade"],
                ["Bacopa monnieri", "Memória de trabalho <strong>SMD 2,03</strong> (IC 1,28–2,78) vs. placebo, com SUCRA 100%",
                 "Metanálise em rede, 29 ECRs, n=2107",
                 "É o maior efeito da página, e vale só para dose <strong>≥600 mg/dia</strong>. <strong>Sem</strong> diferença em atenção sustentada, atenção seletiva ou velocidade de processamento"],
                ["Ginkgo biloba", "Não se separou do placebo em memória; perdeu para a Bacopa em dose alta e baixa",
                 "Mesma metanálise em rede",
                 "É comparação direta, não comparação indireta entre estudos diferentes"],
                ["Cafeína + L-teanina", "Troca de atenção <strong>SMD 0,33</strong> (IC 0,13–0,54); vigilância <strong>SMD 0,20</strong> (IC 0,02–0,38), na 2ª hora. Teanina isolada: tempo de reação <strong>SMD −0,35</strong>",
                 "50 ECRs revisados, 15 na metanálise",
                 "Os autores registram que os intervalos de confiança <em>frequentemente destacam a incerteza</em>. <strong>Dois coautores são da Lipton e da Unilever</strong>"],
                ["Nicotina (fora do cigarro)", "Efeito positivo em <strong>6 de 9 domínios</strong>, tamanho <strong>0,16 a 0,44</strong>",
                 "41 estudos duplo-cegos controlados por placebo",
                 "Em não fumantes ou fumantes não privados — ou seja, <strong>não é alívio de abstinência</strong>. Os autores tratam o achado como parte da explicação de por que a dependência se mantém"],
                ["Modafinila · metilfenidato · d-anfetamina", "Modafinila <strong>SMD 0,12</strong> global. Metilfenidato <strong>SMD 0,21</strong>. <strong>D-anfetamina: nenhum efeito</strong>",
                 "47 estudos ao todo, em três metanálises",
                 "Conclusão literal dos autores: existe percepção de usuário de que essas drogas funcionam, e a evidência não sustenta isso. Medicamentos de prescrição"],
                ["Ômega-3 (EPA/DHA)", "MMSE <strong>MD −0,07</strong> (IC −0,25 a 0,10). <strong>Nada</strong>",
                 "Revisão Cochrane, 3 ECRs de alta qualidade metodológica, n=3536",
                 "Em idosos <strong>cognitivamente saudáveis</strong>. Também sem benefício em aprendizado de palavras, span de dígitos ou fluência verbal"],
                ["Ômega-3 — o sinal que resta", "Cognição global <strong>g 0,02</strong> (IC −0,12 a 0,15). Só memória se salva: <strong>g 0,31</strong> (p=0,003)",
                 "25 ECRs em não dementes; confirmado por revisão de revisões de 2025 com <strong>26.881 participantes</strong> (efeito 0,16; IC 0,01–0,32)",
                 "Sem relação dose-resposta em nenhuma das duas análises. Continua valendo como nutriente — não como nootrópico"],
            ])),
        dict(h="Faixa B — a evidência existe, mas é toda em paciente", tipo="p", corpo=[
            "Aqui está a maior parte do que o mercado vende como nootrópico. A literatura é real, às vezes robusta, "
            "e é <strong>inteiramente em demência, AVC, traumatismo craniano ou esquizofrenia</strong>. Nenhum "
            "destes tem metanálise em pessoa saudável.",
            "Extrapolar da população do estudo para quem quer render mais no trabalho é o erro mais comum do campo "
            "— e é silencioso, porque o número citado está tecnicamente correto.",
        ], tabela=dict(
            cap="Compostos cuja evidência agregada é exclusivamente clínica",
            linhas=[
                ["Composto", "Tamanho de efeito publicado", "População", "Ressalva"],
                ["Huperzina A", "Entre os 5 melhores em MMSE e <strong>o melhor em atividades de vida diária</strong>. Em esquizofrenia: quociente de memória <strong>WMD 10,59</strong> (IC 5,65–15,53) e QI <strong>WMD 3,97–5,66</strong>",
                 "Metanálise em rede de 194 ECRs e 21 fármacos, em demência vascular; e 12 ECRs (n=1117) em esquizofrenia",
                 "<strong>Os 12 ensaios de esquizofrenia foram todos feitos na China.</strong> É inibidor de acetilcolinesterase de verdade — não combinar com donepezila e afins"],
                ["L-oxiracetam", "<strong>+8,97 pontos</strong> no LOTCA vs. placebo (IC 5,69–12,26), <strong>Cohen's d 0,48</strong>; e superior ao oxiracetam comum",
                 "ECR fase 3 multicêntrico duplo-cego, 51 hospitais na China, n=590, em traumatismo cranioencefálico leve a moderado",
                 "É o ensaio positivo mais bem desenhado desta página. Nada nele fala sobre pessoa saudável"],
                ["Citicolina", "<strong>SMD de 0,56</strong> (IC 0,37–0,75) <strong>a 1,57</strong> (IC 0,77–2,37), conforme a análise de sensibilidade",
                 "7 estudos em comprometimento cognitivo leve, Alzheimer ou demência pós-AVC; 6 na metanálise",
                 "<strong>Os próprios autores classificam a qualidade dos estudos como ruim, com risco significativo de viés a favor da intervenção.</strong> O efeito grande e a ressalva vêm no mesmo artigo"],
                ["Alfa-GPC", "Com donepezila: cognição <strong>MD 1,72</strong> (IC 0,20–3,25), função <strong>MD 0,79</strong>, comportamento <strong>MD −7,61</strong>. Isolado: <strong>MD 3,50</strong> (IC 0,36–6,63)",
                 "Metanálise de 7 ECRs + 1 coorte, em disfunção cognitiva ligada a lesão cerebrovascular; replicado em ECR coreano com n=119",
                 "O ganho documentado é <strong>como adjuvante</strong>, não como item isolado de rotina"],
                ["Oxiracetam", "<strong>Sem diferença.</strong> MMSE p=0,49; CDR-SB p=0,38",
                 "ECR multicêntrico duplo-cego, n=500, 36 semanas, prevenção de declínio cognitivo pós-AVC",
                 "<strong>Os autores escrevem que o achado apoia a decisão regulatória de suspender o uso na Coreia do Sul.</strong> A página de nootrópicos deste site lista 22 ensaios para ele — este é o desfecho do maior deles"],
                ["Cerebrolisina", "<strong>Falhou</strong> em demonstrar superioridade em mRS e Barthel",
                 "Metanálise de 7 ECRs, n=1779, AVC isquêmico agudo",
                 "Segura, e sem efeito. Conclusão dos autores: o uso rotineiro não é sustentado pela evidência disponível"],
                ["Piracetam", "Consta entre os que <strong>&ldquo;não parecem ser eficazes&rdquo;</strong>",
                 "Revisão sistemática de 44 estudos e 22 estratégias em demência com corpos de Lewy",
                 "Na rede de demência vascular ele aparece bem colocado <strong>apenas em perfil de segurança</strong> — que é uma frase diferente de eficácia, e costuma ser citada como se fosse a mesma"],
                ["Acetil-L-carnitina", "<strong>Nenhum efeito</strong> em tempo de reação, vigilância, memória imediata ou evocação tardia",
                 "Revisão Cochrane dedicada a <em>pessoas sem comprometimento cognitivo</em>: apenas <strong>2 ECRs elegíveis</strong> em toda a literatura mundial",
                 "Evidência de <strong>qualidade muito baixa</strong>; os autores declaram que não foi possível concluir nada. É o retrato do campo em uma linha"],
            ])),
        dict(h="Faixa C — pessoa saudável, mas base fina e com o fabricante dentro", tipo="p", corpo=[
            "Dois compostos têm ensaio em adulto saudável e resultado positivo. Em ambos, o desenho é pequeno ou "
            "o patrocínio é da parte interessada — e nos dois casos isso está declarado no próprio artigo.",
        ], tabela=dict(
            cap="Evidência em saudável com limitação estrutural",
            linhas=[
                ["Composto", "Tamanho de efeito publicado", "Base", "Ressalva"],
                ["Alfa-GPC em pessoa saudável", "Stroop total <strong>d 0,61</strong> com 630 mg e <strong>d 0,48</strong> com 315 mg; tempo de conclusão <strong>d 0,56</strong>",
                 "ECR cruzado duplo-cego, n=20 homens treinados, dose única",
                 "<strong>Sem</strong> diferença em Flanker, N-Back, desempenho físico ou hormônio do crescimento. n=20, dose única, autor único, e o produto testado é de marca"],
                ["Magnésio L-treonato", "Três ensaios positivos: sono e humor (n=80, 21 dias); memória (n=109, 30 dias); cognição total no NIH Toolbox p=0,043 e reação p=0,031 (n=100, 6 semanas)",
                 "Três ECRs em adultos saudáveis, <strong>todos com o ingrediente de marca Magtein</strong>",
                 "<strong>Um é assinado por funcionários da AIDP, fabricante do ingrediente.</strong> Outro testou fórmula combinada com fosfatidilserina e vitaminas C e D, o que impede atribuir o efeito ao magnésio. O terceiro foi conduzido por uma CRO. <strong>Não existe metanálise independente</strong>"],
            ])),
        dict(h="Três ensaios grandes e negativos", tipo="p", corpo=[
            "Vale isolar isto, porque muda o tipo de argumento cabível. Para a maior parte dos compostos deste "
            "site, o problema é <strong>ausência</strong> de evidência — ninguém testou direito. Para estes três, "
            "não é: a evidência existe, é grande, e é contrária.",
            "<strong>Oxiracetam</strong>, n=500, 36 semanas: sem diferença em nenhum dos dois desfechos "
            "coprimários, e os autores ligam o resultado à suspensão do uso na Coreia do Sul. "
            "<strong>Cerebrolisina</strong>, n=1779 em 7 ECRs: falhou nos dois desfechos de eficácia. "
            "<strong>Piracetam</strong>: listado nominalmente entre os ineficazes numa revisão sistemática.",
            "Os três continuam sendo vendidos, e os três aparecem em listas de nootrópico com contagem alta de "
            "ensaios. A contagem está certa. O desfecho é que não é.",
        ]),
        dict(h="Quem paga o estudo aparece no resultado", tipo="li", corpo=[
            "<strong>Cafeína + L-teanina:</strong> a metanálise tem dois coautores com afiliação declarada à "
            "Lipton Teas and Infusions e à Unilever.",
            "<strong>Alfa-GPC em saudável:</strong> o ECR testa um produto de marca identificado no próprio "
            "artigo, com n=20 e dose única.",
            "<strong>Magnésio L-treonato:</strong> as três únicas evidências em adulto saudável são do mesmo "
            "ingrediente patenteado; uma delas tem funcionários do fabricante entre os autores, e outra testa uma "
            "fórmula combinada que não isola o composto.",
            "<strong>Pycnogenol</strong>, já registrado na página de nootrópicos, tem a mesma característica: boa "
            "parte dos ensaios é financiada pelo detentor da marca.",
            "Nenhum destes estudos é inválido por causa disso. Mas nenhum é evidência independente — e a diferença "
            "entre <em>funciona</em> e <em>o fabricante mostrou que funciona</em> é a única coisa que separa este "
            "campo do marketing.",
        ]),
        dict(h="O que este levantamento mostra", tipo="li", corpo=[
            "<strong>A divisão real não é entre funciona e não funciona — é entre paciente e pessoa saudável.</strong> "
            "Citicolina, huperzina A, L-oxiracetam e alfa-GPC têm literatura séria, e ela é toda clínica.",
            "<strong>Onde há efeito, ele é pequeno.</strong> SMD de 0,2 a 0,4 na faixa A. A exceção é a Bacopa em "
            "memória de trabalho, e ela não moveu atenção nem velocidade de processamento.",
            "<strong>O ganho concentra em quem tem déficit.</strong> Creatina: 0,88 em idoso, 0,03 em jovem, com a "
            "mesma dose e a mesma duração.",
            "<strong>A Cochrane da acetil-L-carnitina é o retrato do campo.</strong> Uma revisão dedicada "
            "exatamente a pessoas saudáveis encontrou <strong>dois</strong> ensaios elegíveis no mundo inteiro.",
            "<strong>Percepção de usuário não bateu com a evidência</strong> — conclusão literal da metanálise de "
            "estimulantes, justamente o bloco onde a sensação de efeito é maior.",
        ]),
        dict(h="O que ficou de fora", tipo="li", corpo=[
            "<strong>Li resumos, não artigos completos.</strong> Todo tamanho de efeito desta página foi "
            "transportado do resumo estruturado do próprio estudo, que é onde a metanálise publica seus números.",
            "<strong>Não refiz nenhum cálculo.</strong> Não converti SMD em Hedge's <em>g</em>, não recalculei "
            "intervalo de confiança e não agreguei estudos por conta própria. Onde as unidades diferem entre "
            "linhas, elas diferem porque os estudos as publicaram assim.",
            "<strong>Não conferi a situação regulatória na ANVISA item a item.</strong> A suspensão do oxiracetam "
            "na Coreia do Sul é afirmação dos autores do ensaio, não verificação independente em fonte "
            "regulatória coreana.",
            "<strong>A lista da WADA, essa eu conferi</strong> — na fonte oficial, em 4 de setembro de 2026. "
            "Vale a <em>Lista de Proibições de 2026</em>, em vigor desde 1º de janeiro. Da seção "
            "<strong>S6.A, estimulantes não especificados, proibidos apenas em competição</strong>, constam "
            "nominalmente: <strong>Modafinil</strong>, <strong>Adrafinil</strong>, <strong>Bromantan</strong>, "
            "<strong>Fonturacetam [4-phenylpiracetam (carphedon)]</strong>, <strong>Hydrafinil (fluorenol)</strong>, "
            "<strong>Fladrafinil</strong>, <strong>Flmodafinil</strong> e <strong>Lisdexamfetamine</strong>. O "
            "<strong>meldonium</strong> está em outra seção e é mais restrito: S4.4.3, proibido <strong>em todos "
            "os momentos</strong>, não só em competição — o que confirma o que a página de meldonium deste site já "
            "dizia.",
            "<strong>Compostos sem metanálise não entraram.</strong> Noopept, Semax, Selank, juba-de-leão e os "
            "racetams menores não têm evidência agregada de onde tirar um tamanho de efeito — estão na "
            "<a href=\"proprio_nootropicos.html\">página de nootrópicos</a>, contados, que é o que dá para fazer "
            "com eles hoje.",
            "<strong>Não busquei literatura fora do PubMed.</strong> Registro de ensaio em andamento, literatura "
            "cinzenta e bases regionais ficaram de fora.",
        ]),
    ],
    referencias=[
        ("Xu C et al. The effects of creatine supplementation on cognitive function in adults: a systematic review and meta-analysis. Front Nutr. 2024;11:1424972.", "https://doi.org/10.3389/fnut.2024.1424972"),
        ("Prokopidis K et al. Effects of creatine supplementation on memory in healthy individuals: a systematic review and meta-analysis of randomized controlled trials. Nutr Rev. 2023;81(4):416-427.", "https://doi.org/10.1093/nutrit/nuac064"),
        ("Tiemtad P et al. Comparative effects of Bacopa monnieri and Ginkgo biloba on cognitive functions: a systematic review and network meta-analysis. Phytomedicine. 2026;153:157915.", "https://doi.org/10.1016/j.phymed.2026.157915"),
        ("Payne ER et al. Effects of tea or its bioactive compounds l-theanine or l-theanine plus caffeine on cognition, sleep, and mood in healthy participants. Nutr Rev. 2025;83(10):1873-1891.", "https://doi.org/10.1093/nutrit/nuaf054"),
        ("Heishman SJ, Kleykamp BA, Singleton EG. Meta-analysis of the acute effects of nicotine and smoking on human performance. Psychopharmacology. 2010;210(4):453-69.", "https://doi.org/10.1007/s00213-010-1848-1"),
        ("Roberts CA et al. How effective are pharmaceuticals for cognitive enhancement in healthy adults? A series of meta-analyses of modafinil, methylphenidate and D-amphetamine. Eur Neuropsychopharmacol. 2020;38:40-62.", "https://doi.org/10.1016/j.euroneuro.2020.07.002"),
        ("Battleday RM, Brem AK. Modafinil for cognitive neuroenhancement in healthy non-sleep-deprived subjects: a systematic review. Eur Neuropsychopharmacol. 2015;25(11):1865-81.", "https://doi.org/10.1016/j.euroneuro.2015.07.028"),
        ("Sydenham E, Dangour AD, Lim WS. Omega 3 fatty acid for the prevention of cognitive decline and dementia. Cochrane Database Syst Rev. 2012;(6):CD005379.", "https://doi.org/10.1002/14651858.CD005379.pub3"),
        ("Alex A et al. Long-chain omega-3 polyunsaturated fatty acids and cognitive decline in non-demented adults: a systematic review and meta-analysis. Nutr Rev. 2020;78(7):563-578.", "https://doi.org/10.1093/nutrit/nuz073"),
        ("Barros MI et al. Omega-3 polyunsaturated fatty acids and cognitive decline in adults with non-dementia or mild cognitive impairment: an overview of systematic reviews. Nutrients. 2025;17(18):3002.", "https://doi.org/10.3390/nu17183002"),
        ("Dang C et al. Pharmacological treatments for vascular dementia: a systematic review and Bayesian network meta-analysis. Front Pharmacol. 2024;15:1451032.", "https://doi.org/10.3389/fphar.2024.1451032"),
        ("Zheng W et al. Adjunctive huperzine A for cognitive deficits in schizophrenia: a systematic review and meta-analysis. Hum Psychopharmacol. 2016;31(4):286-95.", "https://doi.org/10.1002/hup.2537"),
        ("Liu T et al. Efficacy and safety of L-oxiracetam on cognitive function in patients with traumatic brain injury: a multicentre, randomised, double-blind, phase 3 clinical trial. Signal Transduct Target Ther. 2025;10(1):401.", "https://doi.org/10.1038/s41392-025-02492-5"),
        ("Bonvicini M et al. Is citicoline effective in preventing and slowing down dementia? A systematic review and a meta-analysis. Nutrients. 2023;15(2):386.", "https://doi.org/10.3390/nu15020386"),
        ("Sagaro GG, Traini E, Amenta F. Activity of choline alphoscerate on adult-onset cognitive dysfunctions: a systematic review and meta-analysis. J Alzheimers Dis. 2023;92(1):59-70.", "https://doi.org/10.3233/JAD-221189"),
        ("Lee W, Kim M. Comparative study of choline alfoscerate as a combination therapy with donepezil. Medicine (Baltimore). 2024;103(24):e38067.", "https://doi.org/10.1097/MD.0000000000038067"),
        ("Lim JS et al. Oxiracetam and physical activity in preventing cognitive decline after stroke: a multicenter, randomized controlled trial. Eur Stroke J. 2026;11(1).", "https://doi.org/10.1093/esj/23969873251350141"),
        ("Zhang D et al. Efficacy and safety of cerebrolysin for acute ischemic stroke: a meta-analysis of randomized controlled trials. Biomed Res Int. 2017;2017:4191670.", "https://doi.org/10.1155/2017/4191670"),
        ("Stinton C et al. Pharmacological management of Lewy body dementia: a systematic review and meta-analysis. Am J Psychiatry. 2015;172(8):731-42.", "https://doi.org/10.1176/appi.ajp.2015.14121582"),
        ("Chen N et al. L-carnitine for cognitive enhancement in people without cognitive impairment. Cochrane Database Syst Rev. 2017;3(3):CD009374.", "https://doi.org/10.1002/14651858.CD009374.pub3"),
        ("Kerksick CM. Acute alpha-glycerylphosphorylcholine supplementation enhances cognitive performance in healthy men. Nutrients. 2024;16(23):4240.", "https://doi.org/10.3390/nu16234240"),
        ("Hausenblas HA et al. Magnesium-L-threonate improves sleep quality and daytime functioning in adults with self-reported sleep problems: a randomized controlled trial. Sleep Med X. 2024;8:100121.", "https://doi.org/10.1016/j.sleepx.2024.100121"),
        ("Zhang C et al. A Magtein, magnesium L-threonate, based formula improves brain cognitive functions in healthy Chinese adults. Nutrients. 2022;14(24):5235.", "https://doi.org/10.3390/nu14245235"),
        ("Lopresti AL, Smith SJ. The effects of magnesium L-threonate (Magtein) on cognitive performance and sleep quality in adults: a randomised, double-blind, placebo-controlled trial. Front Nutr. 2026;12:1729164.", "https://doi.org/10.3389/fnut.2025.1729164"),
        ("Todas as buscas e leituras foram feitas no PubMed em 4 de setembro de 2026.", "https://pubmed.ncbi.nlm.nih.gov/"),
        ("Agência Mundial Antidopagem, Lista de Proibições de 2026, em vigor desde 1º de janeiro de 2026. Seção S6.A conferida nominalmente na fonte oficial em 4 de setembro de 2026.", "https://www.wada-ama.org/en/prohibited-list"),
    ],
),
}
