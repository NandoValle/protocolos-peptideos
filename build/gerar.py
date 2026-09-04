# -*- coding: utf-8 -*-
"""Gerador do site estatico.

Le  : build/src/*.json  (dados extraidos da fonte)
      build/compostos.py, build/fatos.py  (conteudo PT-BR autoral)
Grava: ./index.html, ./p/*.html, ./seguranca.html, ./sobre.html

Regra: uma tabela so e publicada se passar no portao de traducao.
Tabela que nao passa e descartada e contabilizada no relatorio.
"""
import json, glob, os, re, sys, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dicionario as D
from compostos import COMPOSTOS, CATEGORIAS
from fatos import FATOS
from proprios import PROPRIOS
from evidencia import CORPO as CORPO_EVIDENCIA
from anvisa import ANVISA

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTE = "https://www.peptidedosingprotocols.com/"

# ---------------------------------------------------------------------------
# DATAS. As duas abaixo sao FATOS HISTORICOS, nao a data de hoje.
#
# NUNCA derivar nenhuma delas do relogio (datetime.now, date.today e afins).
# O gerador roda de novo a cada edicao de texto; se a data vier do relogio, o
# site passa a afirmar, a cada rebuild, que foi conferido hoje -- sem que
# ninguem tenha conferido nada. Data velha e correta e melhor que data fresca
# e falsa.
#
# Trocar DATA_FONTE so ao raspar a fonte secundaria de novo.
# Trocar DATA_APURACAO so ao refazer a apuracao em fonte primaria.
# ---------------------------------------------------------------------------
DATA_FONTE = "3 de setembro de 2026"      # acesso a peptidedosingprotocols.com
DATA_APURACAO = "4 de setembro de 2026"   # PubMed, ClinicalTrials.gov, ANVISA, WADA

HOJE = DATA_FONTE  # compatibilidade: o nome enganava, era a data da fonte

# tabelas que interessam
CORE = re.compile(r'(dosing|dosage|reconstitution|cycle|titration|protocol format|schedule|half-life|dose|comparison|timeline|\bvs\b)', re.I)
# deteta ingles remanescente
PALAVRAS_EN = set("""
the and with from that this which these those means then study studies research water store
approved only per about every week weeks day days daily weekly units target tolerance start starting
dosing schedule cycle vial syringe amount context evidence level type reported common commonly used
use blood light room clear color available established not none controlled human humans benefit
safety trial trials cells animals found direct intervals half life longer
shorter than more less most least higher lower when where what how why effect effects change changes
increase decrease response range based between during after before first second third early late
weight loss gain muscle fat skin sleep pain injury repair growth hormone pathway signal
signaling supply planning protocol protocols guide chart table see also may can should would does is
are was were of in at by it its their there here who whom while until unless into onto over
under above below out up down again once both each few other such own same too very
just now ever never always often sometimes usually rarely
""".split())

# tokeniza com letras acentuadas: senao "ate" vira o ingles "at"
_TOKEN = re.compile("[^\\W\\d_]+", re.UNICODE)


ACENTOS = set("áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ")

# funcionais do portugues: se aparece uma destas, o texto passou pela traducao
PALAVRAS_PT = set("""
de da do das dos e ou em no na nos nas um uma uns umas para por com sem sobre
que se ao aos as os a o mais menos entre depois antes cada como quando onde
qual quais isso este esta esse essa aquele aquela ser sao foi era tem tem
apenas ate nao sim pela pelo pelas pelos num numa dele dela seu sua
seus suas nesta neste nessa nesse desta deste dessa desse toda todo todas todos
dose doses dia dias semana semanas mes meses hora horas minuto minutos
frasco frascos unidade unidades seringa agulha injecao aplicacao via vias
aprovado aprovada nao-aprovado estudada estudado estudo estudos ensaio ensaios
pesquisa dados evidencia humano humana humanos humanas animal animais
maior menor alto alta baixo baixa faixa nivel media pico total parcial
inicial inicio fim meia-vida ciclo ciclos pausa manutencao ataque desmame
titulacao reconstituicao concentracao volume peso perda ganho gordura magra
comum comuns relatado relatada tipico tipica padrao esquema protocolo
monoterapia combinacao comunidade clinica clinico nenhum nenhuma forte fraca
agonista receptor receptores peptideo peptideos precursores camundongo
camundongos rato ratos rim figado sangue exame exames sepse grave
manter subir pular checar observar acompanhar reavaliar
""".split())


def _tem_ingles(txt):
    """Heuristica invertida: procura sinal de portugues, nao lista de ingles.

    Passa quando o texto tem acento, tem funcional do PT, tem uma palavra
    conhecida da lista EN traduzida, ou e curto demais para julgar
    (rotulo, numero, nome proprio).
    """
    limpo = txt.replace('in vivo', '').replace('in vitro', '')
    if any(c in ACENTOS for c in limpo):
        return False
    palavras = [w.lower() for w in _TOKEN.findall(limpo)]
    if not palavras:
        return False
    if any(w in PALAVRAS_PT for w in palavras):
        return False
    if any(w in PALAVRAS_EN for w in palavras):
        return True
    # lista de compostos ligada por '+' nao e frase: nao ha o que traduzir
    if '+' in limpo or '/' in limpo:
        return False
    # sem acento, sem funcional PT nem EN: so acusa se for frase longa
    return len(palavras) > 4


# palavras PT que colidem com a regex acima
PERMITIDO = re.compile(r'^(dose|doses|volume|total|nasal|oral|via|status|fase|semanal|diário|não|sim|—|n/d)', re.I)


def esc(s):
    return html.escape(str(s), quote=True)


# separador de milhar da fonte (EN) -> ponto do PT-BR.
# "5,000 mcg" e cinco mil, nao cinco. So dispara com digito inicial 1-9,
# para nunca tocar em decimal do tipo "0,075 mL".
_MILHAR = re.compile(r'\b([1-9]\d{0,2}),(\d{3})\b')


def normaliza_milhar(t):
    anterior = None
    while anterior != t:
        anterior = t
        t = _MILHAR.sub(r'\1.\2', t)
    return t


def celula_ok(txt):
    t = normaliza_milhar(D.celula(txt))
    if not t or PERMITIDO.match(t.strip()):
        return t, True
    return t, not _tem_ingles(t)


def traduz_tabela(t):
    """Devolve (linhas_traduzidas, aprovada)."""
    linhas, ruins, total = [], 0, 0
    for r in t['rows']:
        nova = []
        for c in r:
            v, ok = celula_ok(c)
            total += 1
            if not ok:
                ruins += 1
            nova.append(v)
        linhas.append(nova)
    aprovada = total > 0 and (ruins / total) <= 0.02
    return linhas, aprovada


# ----------------------------------------------------------------- blocos
def cabecalho(titulo, descricao, prefixo="", atual=""):
    def cls(n):
        return ' aria-current="page"' if atual == n else ''
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(descricao)}">
<meta name="robots" content="noindex, nofollow">
<meta name="color-scheme" content="dark">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(descricao)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{prefixo}assets/estilo.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='22' fill='%23D08A4A'/><text y='72' x='50' text-anchor='middle' font-size='60' font-family='serif' font-weight='700' fill='%2316100A'>P</text></svg>">
</head>
<body>
<a class="pular" href="#principal">Pular para o conteúdo</a>
<header class="cabecalho">
  <div class="cabecalho-in">
    <a class="marca" href="{prefixo}index.html">
      <span class="marca-icone" aria-hidden="true">P</span>
      <span>Protocolos de Peptídeos</span>
    </a>
    <nav class="nav" aria-label="Principal">
      <a href="{prefixo}index.html"{cls('inicio')}>Compostos</a>
      <a href="{prefixo}evidencia.html"{cls('evidencia')}>Evidência</a>
      <a href="{prefixo}seguranca.html"{cls('seguranca')}>Segurança</a>
      <a href="{prefixo}sobre.html"{cls('sobre')}>Sobre</a>
    </nav>
  </div>
</header>
<div class="env">
"""


AVISO = """<div class="aviso" role="note">
  <div class="aviso-icone" aria-hidden="true">!</div>
  <div>
    <h2>Material experimental. Leia antes de usar qualquer coisa daqui.</h2>
    <p><strong>Nada nesta página é recomendação médica, prescrição ou plano de tratamento.</strong> É uma tradução organizada de protocolos que circulam em comunidades de pesquisa e, quando existe, do que ensaios publicados testaram. As duas coisas estão marcadas de forma diferente — e não são equivalentes.</p>
    <p>A maior parte dos compostos aqui <strong>não tem aprovação da ANVISA nem da FDA para uso humano</strong>. Vários são vendidos com rótulo de "uso exclusivo em pesquisa", o que significa que não passaram por controle de pureza, esterilidade ou dosagem para consumo por pessoas. Dose descrita por comunidade não é dose validada: é o que alguém relatou ter feito.</p>
    <p>Converse com um profissional de saúde habilitado antes de considerar qualquer um destes compostos. Se você já usa algum e sentir algo fora do previsto, procure atendimento — não espere o próximo exame de rotina.</p>
  </div>
</div>"""


def rodape(prefixo=""):
    return f"""</div>
<footer class="rodape">
  <div class="rodape-in">
    <div>
      <h4>Protocolos de Peptídeos</h4>
      <p>Referência em português sobre protocolos de peptídeos e compostos correlatos. Material educacional e experimental — não substitui avaliação médica.</p>
      <p style="margin-top:14px">Compilado em {HOJE}.</p>
    </div>
    <div>
      <h4>Navegar</h4>
      <ul>
        <li><a href="{prefixo}index.html">Todos os compostos</a></li>
        <li><a href="{prefixo}seguranca.html">Segurança e limites</a></li>
        <li><a href="{prefixo}sobre.html">Sobre, fonte e método</a></li>
      </ul>
    </div>
    <div>
      <h4>Aviso</h4>
      <ul>
        <li>Não é aconselhamento médico</li>
        <li>Sem registro na ANVISA</li>
        <li>Uso experimental</li>
        <li>Dose de comunidade ≠ dose validada</li>
      </ul>
    </div>
  </div>
</footer>
</body>
</html>"""



# paginas de protocolo que ganharam companheira de fonte primaria
COMPANHEIRA = {
    'stacks_klow-stack': ('proprio_klow_evidencia', 'KLOW'),
    'protocol_semax': ('proprio_semax_evidencia', 'Semax'),
}

# paginas de GLP-1: a tarja preta da FDA entra antes de qualquer tabela de dose.
# Auditoria em proprio_glp1_bula, contra as bulas lidas em 04/09/2026.
TARJA_GLP1 = {
    'protocol_semaglutide':            'semaglutida',
    'protocol_tirzepatide':            'tirzepatida',
    'protocol_retatrutide':            None,
    'protocol_cagrilintide':           None,
    'protocol_survodutide':            None,
    'stacks_cagrisema':                'semaglutida',
    'stacks_cagrilintide-tirzepatide': 'tirzepatida',
    'stacks_cagrilintide-retatrutide': None,
    'stacks_retatrutide-mots-c':       None,
}

_RODAPE_TARJA = (
    f'<p>Esta advertência não estava nesta página até {DATA_APURACAO}, e a falha era deste site, não da '
    'fonte. A auditoria das tabelas de dose contra as bulas da FDA e da ANVISA está em '
    '<a href="proprio_glp1_bula.html">Os GLP-1 contra a bula</a>.</p>'
    '</div></div>'
)

# a semaglutida e a tirzepatida NAO tem o mesmo tratamento regulatorio no Brasil:
# a bula da ANVISA contraindica a tirzepatida e apenas recomenda cautela na semaglutida.
TARJA_SEMA = (
    '<div class="aviso"><div class="aviso-icone">!</div><div>'
    '<h2>Tarja preta nos EUA, cautela no Brasil — e as duas bulas discordam</h2>'
    '<p><strong>A semaglutida carrega a advertência mais forte que a FDA aplica a um medicamento.</strong> Em '
    'roedores ela causa tumores de células C da tireoide de forma dependente da dose e da duração do tratamento, '
    'em exposições clinicamente relevantes. Não se sabe se causa em humanos.</p>'
    '<p><strong>Nos Estados Unidos isso é contraindicação absoluta</strong> em quem tem história pessoal ou '
    'familiar de carcinoma medular de tireoide (CMT) ou neoplasia endócrina múltipla tipo 2 (NEM 2). '
    '<strong>No Brasil, não é.</strong> As bulas de Ozempic, Wegovy e Rybelsus contraindicam apenas '
    'hipersensibilidade; sobre o CMT, mandam <strong>usar com cautela</strong> e classificam a relevância humana '
    'como considerada baixa. Quem decide, aqui, é o prescritor — não a bula.</p>'
    '<p><strong>Há relato de anafilaxia e angioedema</strong> com semaglutida, e isso é contraindicação nos dois '
    'países.</p>'
    + _RODAPE_TARJA
)

TARJA_TIRZ = (
    '<div class="aviso"><div class="aviso-icone">!</div><div>'
    '<h2>Contraindicação absoluta, no Brasil e nos Estados Unidos</h2>'
    '<p><strong>A tirzepatida carrega tarja preta da FDA</strong> por tumores de células C da tireoide em ratos, '
    'dependentes da dose e da duração do tratamento, em exposições clinicamente relevantes. Não se sabe se causa '
    'em humanos.</p>'
    '<p><strong>É contraindicada</strong> em quem tem história <strong>pessoal ou familiar</strong> de carcinoma '
    'medular de tireoide (CMT) ou neoplasia endócrina múltipla tipo 2 (NEM 2). Diferente da semaglutida, '
    '<strong>a bula brasileira do MOUNJARO traz essa contraindicação na seção 4</strong>, com o mesmo alcance da '
    'americana. Também é contraindicada em quem já teve hipersensibilidade grave: há relato de anafilaxia e '
    'angioedema.</p>'
    + _RODAPE_TARJA
)

TARJA_TEXTO_INVEST = (
    '<div class="aviso"><div class="aviso-icone">!</div><div>'
    '<h2>Sem bula, sem dose aprovada</h2>'
    '<p><strong>Este composto não tem registro na FDA</strong> — conferido na base de rótulos em 4 de setembro '
    'de 2026. Isso não o torna mais seguro que a semaglutida ou a tirzepatida, que têm tarja preta: torna-o '
    'menos conhecido. <strong>Não existe escada de titulação aprovada, não existe dose máxima definida e não '
    'existe lista oficial de contraindicação</strong> para comparar com as tabelas desta página.</p>'
    '<p>Os análogos aparentados que já têm bula carregam advertência de tumor de células C da tireoide — e a '
    'tirzepatida é contraindicada em carcinoma medular de tireoide e NEM 2 nas bulas dos dois países, enquanto '
    'a semaglutida só é nos Estados Unidos. A auditoria completa está em '
    '<a href="proprio_glp1_bula.html">Os GLP-1 contra a bula</a>.</p>'
    '</div></div>'
)


def selo_anvisa(slug):
    """Selo do cartao do indice. So marca o que foi de fato medido."""
    if slug not in ANVISA:
        return '', 'nd'
    reg, nof, _ = ANVISA[slug]
    if reg:
        return (f'<span class="selo selo-anv-sim" title="{reg} medicamento(s) com registro ativo '
                f'na ANVISA">ANVISA</span>'), 'sim'
    if nof:
        return '<span class="selo selo-anv-nof" title="Só produto notificado, sem registro">notificado</span>', 'nof'
    return '<span class="selo selo-anv-nao" title="Nenhum medicamento registrado no Brasil">sem registro</span>', 'nao'


def linha_anvisa(slug):
    """Uma linha por composto: existe medicamento registrado no Brasil?"""
    if slug not in ANVISA:
        return None
    reg, nof, prod = ANVISA[slug]
    if reg:
        lista = ', '.join(prod[:6]) + ('...' if len(prod) >= 6 else '')
        return (f'<div class="nota"><strong>No Brasil: {reg} medicamento(s) com registro ativo na ANVISA.</strong> '
                f'{esc(lista)}. Levantado em {DATA_APURACAO} no dado aberto da agência. '
                f'A varredura dos {len(ANVISA)} compostos está em '
                f'<a href="proprio_anvisa.html">O que existe no Brasil</a>.</div>')
    if nof:
        return (f'<div class="aviso-linha"><strong>No Brasil: nenhum registro, {nof} produto(s) apenas notificado(s).</strong> '
                f'Notificação é a via de baixo risco e não passa pela mesma análise de um registro. '
                f'Ver <a href="proprio_anvisa.html">O que existe no Brasil</a>.</div>')
    return ('<div class="aviso-linha"><strong>No Brasil: nenhum medicamento registrado com este princípio ativo.</strong> '
            f'Conferido em {DATA_APURACAO} no dado aberto da ANVISA, com 43.489 registros. '
            'Não existe bula brasileira, dose aprovada nem lote fiscalizado — o que circula é importação ou manipulação. '
            'A varredura completa está em <a href="proprio_anvisa.html">O que existe no Brasil</a>.</div>')


def selo_aprovacao(v):
    return {
        "nao":     ('selo-nao', 'Não aprovado'),
        "parcial": ('selo-parcial', 'Aprovação parcial'),
        "sim":     ('selo-sim', 'Aprovado'),
    }[v]


# ------------------------------------------------------------- página índice
def gera_index(itens, stats):
    partes = [cabecalho(
        "Protocolos de Peptídeos — referência em português",
        "Referência traduzida de protocolos de peptídeos: dose, reconstituição, ciclo e limites de evidência. Material experimental, não é recomendação médica.",
        "", "inicio")]

    partes.append('<main id="principal" class="env-largo">')
    partes.append(f"""<section class="hero">
  <span class="hero-sobre">Referência experimental</span>
  <h1>Protocolos de peptídeos, <em>em português</em> e com o limite da evidência à mostra.</h1>
  <p class="hero-sub">{stats['n']} compostos e combinações, com dose, reconstituição, estrutura de ciclo e status regulatório. Cada página separa o que um ensaio publicado testou do que é apenas prática relatada por comunidade — porque a diferença entre as duas coisas é o assunto todo.</p>
  <div class="hero-numeros">
    <div class="numero"><b>{stats['n']}</b><span>compostos</span></div>
    <div class="numero"><b>{stats['tabelas']}</b><span>tabelas de dose</span></div>
    <div class="numero"><b>{stats['nao_aprovados']}</b><span>sem aprovação</span></div>
    <div class="numero"><b>{len(CATEGORIAS)}</b><span>categorias</span></div>
  </div>
</section>""")

    partes.append(AVISO)

    partes.append("""<div class="busca-caixa">
  <div class="busca-campo">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
    <label for="busca" class="pular">Buscar composto</label>
    <input type="search" id="busca" placeholder="Buscar por nome, classe ou sigla — KLOW, Semax, GLP-1, reparo…" autocomplete="off">
  </div>
  <div class="filtros" id="filtros" role="group" aria-label="Filtrar por categoria">
    <button class="filtro" data-cat="todos" aria-pressed="true">Todos</button>""")
    for k, (nome, _) in CATEGORIAS.items():
        partes.append(f'    <button class="filtro" data-cat="{k}" aria-pressed="false">{esc(nome)}</button>')
    partes.append('  </div>')
    partes.append("""  <div class="filtros filtros-anvisa" id="filtros-anvisa" role="group" aria-label="Filtrar por registro no Brasil">
    <button class="filtro filtro-anv" data-anv="todos" aria-pressed="true">Registro no Brasil: todos</button>
    <button class="filtro filtro-anv" data-anv="sim" aria-pressed="false">Só o que existe aqui</button>
    <button class="filtro filtro-anv" data-anv="nao" aria-pressed="false">Só o que não existe</button>
  </div>
</div>""")
    partes.append('<p class="nota-filtro">O selo de registro vem da <a href="evidencia.html">varredura do dado aberto '
                  f'da ANVISA</a> feita em {DATA_APURACAO}, e só aparece nos 44 compostos que foram medidos um a '
                  'um. Combinações e páginas de método não têm selo.</p>')
    partes.append('<p id="vazio" hidden style="color:var(--texto-fraco);padding:40px 0">Nenhum composto corresponde à busca.</p>')

    for cat, (nome, desc) in CATEGORIAS.items():
        grupo = [i for i in itens if i['meta']['categoria'] == cat]
        if not grupo:
            continue
        partes.append(f'<section class="secao" data-secao="{cat}">')
        partes.append(f'  <div class="secao-cabeca"><h2>{esc(nome)}</h2><p class="secao-desc">{esc(desc)}</p></div>')
        partes.append('  <div class="grade">')
        for i in sorted(grupo, key=lambda x: x['meta']['nome']):
            m = i['meta']
            cls, rot = selo_aprovacao(m['aprovado'])
            selo_anv, estado_anv = selo_anvisa(i['slug'])
            extra = {'sim': ' anvisa registro brasil registrado',
                     'nao': ' sem registro anvisa importacao manipulado',
                     'nof': ' notificado anvisa baixo risco'}.get(estado_anv, '')
            busca = f"{m['nome']} {m['tagline']} {nome} {i['slug']}{extra}".lower()
            partes.append(f"""    <a class="card" href="p/{i['slug']}.html" data-cat="{cat}" data-anv="{estado_anv}" data-busca="{esc(busca)}">
      <div class="card-topo"><h3>{esc(m['nome'])}</h3><span class="selo {cls}">{rot}</span></div>
      <p>{esc(m['tagline'])}</p>
      <div class="card-rodape"><span class="selo selo-cat">{esc(nome)}</span>{selo_anv}<span>{i['n_tabelas']} tabela(s)</span></div>
    </a>""")
        partes.append('  </div>\n</section>')

    partes.append('</main>')
    partes.append(rodape(""))
    partes.append('<script src="assets/app.js"></script>')
    return '\n'.join(partes)


# ------------------------------------------------------------ página composto
CANONICO_ARMAZENAMENTO = """<h2 id="armazenamento">Armazenamento e manuseio</h2>
<p>As regras abaixo valem para praticamente todo peptídeo liofilizado desta referência. Onde o composto tiver exigência própria, ela aparece na tabela da seção anterior.</p>
<ul>
  <li><strong>Pó liofilizado, fechado:</strong> geladeira, entre 2 e 8 °C, protegido da luz. Muitos toleram temperatura ambiente por períodos curtos de transporte, mas isso é tolerância, não recomendação.</li>
  <li><strong>Depois de reconstituído:</strong> sempre refrigerado, entre 2 e 8 °C. A janela de estabilidade cai para dias ou poucas semanas, conforme o composto.</li>
  <li><strong>Nunca congelar depois de reconstituir.</strong> O ciclo de congelamento e descongelamento degrada o peptídeo.</li>
  <li><strong>Não agitar.</strong> Girar o frasco devagar. Agitar quebra a cadeia peptídica.</li>
  <li><strong>Água bacteriostática pela parede do frasco</strong>, em fio lento, e não jorrada direto sobre o pó.</li>
  <li><strong>Solução turva, com partículas ou mudança de cor:</strong> descartar. Não existe recuperação.</li>
</ul>"""

CANONICO_EXAMES = """<h2 id="exames">Exames e monitoramento</h2>
<p>Esta lista é a que aparece de forma recorrente na fonte, com pequenas variações por composto. Serve como ponto de partida para conversar com um profissional — não como substituto dessa conversa.</p>
<ul>
  <li><strong>Antes de começar:</strong> hemograma completo, painel metabólico completo, perfil lipídico, glicemia de jejum e HbA1c, TSH e T4 livre, pressão arterial e frequência cardíaca de repouso.</li>
  <li><strong>Conforme o composto:</strong> IGF-1 (eixo do GH), lipase e amilase (VIP e os agonistas de incretina), cobre sérico e ceruloplasmina (GHK-Cu e blends que o contenham), PCR.</li>
  <li><strong>Reavaliação:</strong> a maior parte dos protocolos revisa entre a semana 4 e a 8, e depois a cada 8–12 semanas.</li>
  <li><strong>Não esperar o exame de rotina</strong> diante de dor abdominal, alteração visual, mudança em pinta, falta de ar, inchaço assimétrico ou qualquer sintoma novo e persistente. Isso é procura de atendimento, não item de planilha.</li>
</ul>"""


def gera_composto(item):
    slug = item['slug']
    m = item['meta']
    cat_nome = CATEGORIAS[m['categoria']][0]
    cls, rot = selo_aprovacao(m['aprovado'])
    # pagina autoral nao traz dose: o titulo nao pode prometer uma
    if slug in PROPRIOS:
        titulo = f"{m['nome']} — o que a evidência mostra"
    else:
        titulo = f"{m['nome']} — protocolo, dose e ciclo"

    p = [cabecalho(titulo, m['tagline'], "../")]
    p.append('<div class="pagina">')

    proprio = PROPRIOS.get(slug)

    # trilha lateral
    itens_trilha = [('resumo', 'Resumo')]
    if proprio:
        for k, sec in enumerate(proprio['secoes']):
            itens_trilha.append((f'sec{k}', sec['h']))
        itens_trilha.append(('refs', 'Referências'))
    else:
        if slug in FATOS:
            itens_trilha.append(('rapido', 'Referência rápida'))
        for k, t in enumerate(item['tabelas']):
            itens_trilha.append((f'tab{k}', t['cap']))
        itens_trilha += [('armazenamento', 'Armazenamento'), ('exames', 'Exames'), ('limites', 'Limites da evidência')]

    p.append('<aside class="trilha" aria-label="Nesta página">')
    p.append('  <p class="trilha-titulo">Nesta página</p>\n  <ol>')
    for aid, rotulo in itens_trilha:
        p.append(f'    <li><a href="#{aid}">{esc(rotulo)}</a></li>')
    p.append('  </ol>\n</aside>')

    p.append('<main id="principal" class="conteudo">')
    p.append(f'<div class="migalha"><a href="../index.html">Compostos</a> &rsaquo; {esc(cat_nome)}</div>')
    p.append('<div class="artigo-cabeca">')
    p.append(f'  <h1>{esc(m["nome"])}</h1>')
    p.append(f'  <p class="artigo-sub">{esc(m["tagline"])}</p>')
    p.append(f'  <div class="artigo-selos"><span class="selo {cls}">{rot}</span><span class="selo selo-cat">{esc(cat_nome)}</span></div>')
    p.append('</div>')

    p.append(AVISO)

    _anv = linha_anvisa(slug)
    if _anv:
        p.append(_anv)

    if slug in TARJA_GLP1:
        _mol = TARJA_GLP1[slug]
        p.append(TARJA_SEMA if _mol == 'semaglutida'
                 else TARJA_TIRZ if _mol == 'tirzepatida'
                 else TARJA_TEXTO_INVEST)

    if slug in COMPANHEIRA:
        destino, nome = COMPANHEIRA[slug]
        p.append(f'<div class="nota"><strong>Esta página vem da fonte secundária.</strong> '
                 f'O que a evidência primária diz sobre o {esc(nome)} — contagem no PubMed, ensaios registrados '
                 f'e as doses que os estudos publicados usaram — está em '
                 f'<a href="{destino}.html">{esc(nome)} — a evidência</a>.</div>')

    if m.get('alerta'):
        p.append(f'<div class="aviso-linha"><strong>Atenção específica deste composto:</strong> {esc(m["alerta"])}</div>')

    p.append('<h2 id="resumo">Resumo</h2>')
    p.append(f'<p>{esc(m["resumo"])}</p>')

    # ---- pagina autoral, montada de fonte primaria
    if proprio:
        for k, sec in enumerate(proprio['secoes']):
            p.append(f'<h2 id="sec{k}">{esc(sec["h"])}</h2>')
            if sec.get('tipo') == 'li':
                p.append('<ul>')
                for x in sec['corpo']:
                    p.append(f'  <li>{x}</li>')
                p.append('</ul>')
            else:
                for x in sec['corpo']:
                    p.append(f'<p>{x}</p>')
            tab = sec.get('tabela')
            if tab:
                p.append('<div class="tabela-env"><div class="tabela-rolagem"><table>')
                p.append('  <thead><tr>' + ''.join(f'<th>{c}</th>' for c in tab['linhas'][0]) + '</tr></thead>')
                p.append('  <tbody>')
                for r in tab['linhas'][1:]:
                    p.append('    <tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>')
                p.append('  </tbody></table></div></div>')

        p.append('<h2 id="refs">Referências</h2>')
        # A frase das referencias nao pode afirmar PubMed para toda pagina: a de
        # ANVISA nao usa PubMed, e afirmar isso ali e falso. Default generico,
        # com override por pagina via 'nota_refs'.
        nota_refs = proprio.get('nota_refs',
            f'Cada número foi levantado por mim nas fontes listadas abaixo, em {DATA_APURACAO}, '
            'e a consulta usada está declarada acima.')
        p.append('<div class="nota"><strong>Esta página não veio da fonte secundária.</strong> '
                 f'{nota_refs}</div>')
        p.append('<ol style="color:var(--texto-suave);font-size:14.5px;line-height:1.6">')
        for txt, url in proprio['referencias']:
            p.append(f'  <li style="margin-bottom:10px"><a href="{url}" rel="noopener" target="_blank">{esc(txt)}</a></li>')
        p.append('</ol>')
        p.append('<p><a href="../index.html">&larr; Voltar para todos os compostos</a></p>')
        p.append('</main>\n</div>')
        p.append(rodape("../"))
        return '\n'.join(p)

    if slug in FATOS:
        p.append('<h2 id="rapido">Referência rápida</h2>')
        p.append('<dl class="fatos">')
        for rotulo, valor in FATOS[slug]:
            p.append(f'  <div class="fato"><dt>{esc(rotulo)}</dt><dd>{esc(valor)}</dd></div>')
        p.append('</dl>')

    for k, t in enumerate(item['tabelas']):
        p.append(f'<h2 id="tab{k}">{esc(t["cap"])}</h2>')
        p.append('<div class="tabela-env">')
        p.append(f'  <div class="tabela-titulo">{esc(t["cap"])}</div>')
        p.append('  <div class="tabela-rolagem"><table>')
        cab = t['linhas'][0]
        p.append('    <thead><tr>' + ''.join(f'<th>{esc(c)}</th>' for c in cab) + '</tr></thead>')
        p.append('    <tbody>')
        for r in t['linhas'][1:]:
            tds = []
            for j, c in enumerate(r):
                num = ' class="num"' if j > 0 and re.match(r'^[~≈<>≥≤]?\s*[\d.,]+\s*(mg|mcg|mL|g|UI|°C|h|%|unidade)', c) else ''
                tds.append(f'<td{num}>{esc(c)}</td>')
            p.append('      <tr>' + ''.join(tds) + '</tr>')
        p.append('    </tbody></table></div>')
        p.append('</div>')

    p.append(CANONICO_ARMAZENAMENTO)
    p.append(CANONICO_EXAMES)

    p.append('<h2 id="limites">Limites da evidência</h2>')
    p.append('<div class="nota"><strong>O que estes números são e o que não são.</strong> Os valores acima foram preservados exatamente como aparecem na fonte, sem reinterpretação. O que a fonte descreve como prática de comunidade está marcado assim nas tabelas; o que veio de ensaio publicado também. Uma dose repetida por muita gente não vira dose validada por repetição.</div>')
    p.append(f'<p>Fonte dos dados: <a href="{FONTE}" rel="nofollow noopener" target="_blank">peptidedosingprotocols.com</a>, acesso em {HOJE}. Tradução e organização em português são autorais. Nenhuma fonte primária (PubMed, registro de ensaio, bula) foi conferida na montagem desta página — a checagem foi contra a fonte secundária, e só.</p>')
    p.append(f'<p><a href="../index.html">&larr; Voltar para todos os compostos</a></p>')

    p.append('</main>\n</div>')
    p.append(rodape("../"))
    return '\n'.join(p)


# ------------------------------------------------------------ páginas fixas
def gera_seguranca():
    p = [cabecalho("Segurança e limites — Protocolos de Peptídeos",
                   "O que esta referência é, o que não é, e os riscos que não aparecem nas tabelas de dose.",
                   "", "seguranca")]
    p.append('<main id="principal" class="env-largo" style="max-width:800px;padding-top:52px;padding-bottom:80px">')
    p.append('<h1 style="font-family:var(--display);font-size:clamp(32px,4.6vw,44px);font-weight:600;letter-spacing:-.026em;margin:0 0 22px">Segurança e limites</h1>')
    p.append(AVISO)
    p.append('<div class="conteudo" style="padding:0">')
    p.append("""
<h2>O risco que não aparece na tabela de dose</h2>
<p>Toda tabela desta referência responde à pergunta "quanto". Nenhuma responde às três que costumam machucar antes:</p>
<h3>1. O que tem dentro do frasco</h3>
<p>Produto com rótulo de "uso exclusivo em pesquisa" não passou por controle de identidade, pureza, esterilidade ou endotoxina para uso humano. O rótulo diz 10 mg; ninguém garantiu que sejam 10 mg, nem que seja o composto certo, nem que esteja estéril. Um laudo de análise (COA) do fornecedor é melhor que nada, mas é um documento emitido por quem está vendendo.</p>
<h3>2. A dose que a comunidade repete</h3>
<p>Boa parte dos números aqui vem de relato de comunidade. Uma dose citada por mil pessoas continua sendo um relato repetido mil vezes — não vira evidência por acúmulo. Onde existe ensaio publicado, a página diz. Onde não existe, também diz.</p>
<h3>3. A interação com o que você já toma</h3>
<p>Vários compostos desta lista mexem em glicose, pressão, coagulação ou sinalização serotonérgica. O azul de metileno com um antidepressivo ISRS é o exemplo mais direto: é risco de síndrome serotoninérgica, não incômodo. Um profissional que veja sua lista inteira de medicamentos é a única forma séria de resolver isso.</p>

<h2>Situações que pedem parar e procurar atendimento</h2>
<ul>
  <li>Dor abdominal persistente, sobretudo com náusea ou vômito — atenção redobrada com agonistas de incretina e com VIP.</li>
  <li>Qualquer alteração em pinta: cor, borda, tamanho ou sangramento. Vale para Melanotan II em particular.</li>
  <li>Falta de ar, inchaço assimétrico de perna, dor no peito.</li>
  <li>Alteração visual, dor de cabeça nova e persistente, confusão.</li>
  <li>Reação no local da injeção que espalha, esquenta ou vem com febre.</li>
  <li>Hipoglicemia — tremor, suor frio, confusão. Preocupa especialmente com IGF-1 LR3.</li>
</ul>

<h2>Grupos em que o risco é outro</h2>
<p>Gravidez, amamentação, câncer ativo ou histórico oncológico, doença renal ou hepática, uso de anticoagulante, transtorno psiquiátrico em tratamento e menores de idade. Nenhum dos compostos desta referência tem dado de segurança que sustente uso nesses contextos, e vários têm razão mecanística para preocupar — sinal de crescimento sistêmico é o exemplo mais claro.</p>

<h2>Situação regulatória no Brasil</h2>
<p>Nenhum dos compostos marcados como "não aprovado" nesta referência tem registro na ANVISA para as finalidades descritas. Semaglutida, tirzepatida e tesamorelina têm registro para indicações específicas e exigem prescrição. Importar produto de uso em pesquisa para consumo pessoal não os transforma em medicamento — muda apenas quem carrega o risco.</p>

<h2>O que esta referência não faz</h2>
<ul>
  <li>Não indica fornecedor, loja ou marca. A fonte original tem links comerciais; eles foram removidos.</li>
  <li>Não recomenda dose, ciclo ou combinação para ninguém.</li>
  <li>Não verificou nenhuma fonte primária. A conferência foi contra a fonte secundária.</li>
  <li>Não substitui consulta, exame ou receita.</li>
</ul>
""")
    p.append('</div>\n</main>')
    p.append(rodape(""))
    return '\n'.join(p)


def gera_evidencia():
    p = [cabecalho("Verificado em fonte primária — Protocolos de Peptídeos",
                   "As sete páginas montadas direto do PubMed e do ClinicalTrials.gov, com a consulta declarada. 105 compostos.",
                   "", "evidencia")]
    p.append('<main id="principal" class="env-largo" style="max-width:860px;padding-top:52px;padding-bottom:80px">')
    p.append('<h1 style="font-family:var(--display);font-size:clamp(32px,4.6vw,44px);font-weight:600;'
             'letter-spacing:-.026em;margin:0 0 14px">Verificado em fonte primária</h1>')
    p.append('<p class="artigo-sub" style="margin-bottom:30px">Sete páginas, 105 compostos, cada número '
             'levantado no PubMed e no ClinicalTrials.gov com a consulta declarada.</p>')
    p.append('<div class="conteudo" style="padding:0">')
    p.append(CORPO_EVIDENCIA)
    p.append('</div>')
    p.append('</main>')
    p.append(rodape(""))
    return chr(10).join(p)


def gera_sobre(stats):
    p = [cabecalho("Sobre, fonte e método — Protocolos de Peptídeos",
                   "De onde vieram os dados, como foram traduzidos e o que ficou de fora.",
                   "", "sobre")]
    p.append('<main id="principal" class="env-largo" style="max-width:800px;padding-top:52px;padding-bottom:80px">')
    p.append('<h1 style="font-family:var(--display);font-size:clamp(32px,4.6vw,44px);font-weight:600;letter-spacing:-.026em;margin:0 0 22px">Sobre, fonte e método</h1>')
    p.append('<div class="conteudo" style="padding:0">')
    p.append(f"""
<h2>O que é isto</h2>
<p>Uma referência pessoal, em português, sobre protocolos de peptídeos e compostos correlatos. Foi montada porque o material sério sobre o assunto está quase todo em inglês e quase sempre misturado com página de venda.</p>

<h2>Fonte</h2>
<p>Os dados de protocolo — dose, titulação, reconstituição, estrutura de ciclo, status regulatório — foram compilados de <a href="{FONTE}" rel="nofollow noopener" target="_blank">peptidedosingprotocols.com</a>, acesso em {HOJE}. É uma fonte secundária de caráter comercial, não uma publicação revisada por pares. Isso está dito em cada página, e não é detalhe: significa que a confiabilidade de tudo aqui está limitada pela confiabilidade dela.</p>

<h2>Como foi traduzido</h2>
<ul>
  <li><strong>Os números não foram retipados.</strong> Todo valor de dose, volume, concentração e duração foi transportado por script, célula a célula. O que mudou foi o separador decimal (ponto para vírgula) e a unidade escrita por extenso. Isso é deliberado: retipar dose à mão é como se erra dose.</li>
  <li><strong>Os textos em português são autorais.</strong> Resumos, alertas e as seções de segurança foram escritos do zero a partir da leitura da fonte, e não traduzidos linha a linha. São mais curtos que o original.</li>
  <li><strong>Tabela que não passou no portão de tradução foi descartada</strong>, não publicada pela metade. Das {stats['tabelas_total']} tabelas extraídas, {stats['tabelas']} foram publicadas e {stats['tabelas_total'] - stats['tabelas']} foram descartadas por não atingirem o critério.</li>
  <li><strong>Todo conteúdo comercial foi removido:</strong> links de fornecedor, cupons, seções de "onde comprar" e recomendações de loja.</li>
</ul>

<h2>O que ficou de fora, e por quê</h2>
<ul>
  <li><strong>Fontes primárias, nas páginas importadas.</strong> Nas páginas de protocolo que vêm da fonte secundária, nenhum artigo do PubMed, registro de ensaio ou bula foi aberto para conferir os números: a checagem foi contra a fonte, e só. Isso continua sendo a limitação principal desta referência.<br><strong>As páginas de <a href="evidencia.html">evidência verificada</a> são a exceção, e existem justamente para corrigir isso</strong> — nelas cada número foi levantado por mim no PubMed, no ClinicalTrials.gov, na bula da ANVISA ou na lista da WADA, com a consulta declarada na própria página. As duas coisas não têm o mesmo peso, e estão marcadas de forma diferente em todo o site.</li>
  <li><strong>Seções de calculadora interativa.</strong> A fonte tem widgets de cálculo de dose; eles não foram reproduzidos, para não dar aparência de precisão a uma conta que depende de conferir o frasco na mão.</li>
  <li><strong>Fornecedores e preços.</strong> Deliberadamente fora.</li>
</ul>

<h2>Direitos</h2>
<p>Valores numéricos de protocolo são fatos e não são objeto de direito autoral. A organização, os textos em português e o projeto visual desta referência são autorais. A fonte está creditada com link em todas as páginas. Este é um site pessoal, sem publicidade, sem afiliação e sem finalidade comercial. Havendo pedido justificado do detentor dos direitos da fonte, o material sai do ar.</p>

<h2>Estado desta compilação</h2>
<p>Compilado em {HOJE}, cobrindo {stats['n']} compostos e combinações. Protocolo de peptídeo muda rápido, e o status regulatório muda mais rápido ainda — várias datas de Categoria 2 da FDA citadas aqui têm revisão marcada para 2026. Confira antes de tratar qualquer status como atual.</p>
""")
    p.append('</div>\n</main>')
    p.append(rodape(""))
    return '\n'.join(p)


APP_JS = """(function () {
  var busca = document.getElementById('busca');
  var filtros = document.getElementById('filtros');
  var filtrosAnv = document.getElementById('filtros-anvisa');
  var vazio = document.getElementById('vazio');
  if (!busca || !filtros) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card[data-busca]'));
  var secoes = Array.prototype.slice.call(document.querySelectorAll('[data-secao]'));
  var cat = 'todos';
  var anv = 'todos';

  function normaliza(s) {
    return s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  }

  function aplicar() {
    var termo = normaliza(busca.value.trim());
    var achou = 0;
    cards.forEach(function (c) {
      var okCat = cat === 'todos' || c.dataset.cat === cat;
      // 'nao' inclui o notificado: nenhum dos dois tem registro
      var estado = c.dataset.anv || 'nd';
      var okAnv = anv === 'todos'
        || (anv === 'sim' && estado === 'sim')
        || (anv === 'nao' && (estado === 'nao' || estado === 'nof'));
      var okTermo = !termo || normaliza(c.dataset.busca).indexOf(termo) !== -1;
      var mostra = okCat && okAnv && okTermo;
      c.hidden = !mostra;
      if (mostra) achou++;
    });
    secoes.forEach(function (s) {
      var visiveis = s.querySelectorAll('.card:not([hidden])').length;
      s.hidden = visiveis === 0;
    });
    if (vazio) vazio.hidden = achou !== 0;
  }

  function grupo(el, campo, aplicaValor) {
    if (!el) return;
    el.addEventListener('click', function (e) {
      var b = e.target.closest('.filtro');
      if (!b) return;
      aplicaValor(b.dataset[campo]);
      el.querySelectorAll('.filtro').forEach(function (x) {
        x.setAttribute('aria-pressed', String(x === b));
      });
      aplicar();
    });
  }

  busca.addEventListener('input', aplicar);
  grupo(filtros, 'cat', function (v) { cat = v; });
  grupo(filtrosAnv, 'anv', function (v) { anv = v; });
})();
"""


# ------------------------------------------------------------------- main
# paginas de duracao de ciclo: nao sao compostos proprios, entram na pagina do pai
CICLO_PAI = {
    'peptide-cycles_5-amino-1mq':                  'protocol_5-amino-1mq',
    'peptide-cycles_aod-9604-cycle-length':        'protocol_aod-9604',
    'peptide-cycles_cartalax-cycle':               'protocol_cartalax',
    'peptide-cycles_ipamorelin':                   'protocol_ipamorelin',
    'peptide-cycles_klow-peptide-cycle-length':    'stacks_klow-stack',
    'peptide-cycles_kpv-cycle-length':             'protocol_kpv',
    'peptide-cycles_nad-plus':                     'protocol_nad-plus',
    'peptide-cycles_retatrutide':                  'protocol_retatrutide',
    'peptide-cycles_selank':                       'protocol_selank',
    'peptide-cycles_wolverine-stack-cycle-length': 'stacks_wolverine-stack',
}


def carrega_ciclos():
    """Tabelas das paginas de ciclo, agrupadas pelo composto pai."""
    extra = {}
    for caminho in sorted(glob.glob(os.path.join(RAIZ, 'build', 'src', 'peptide-cycles_*.json'))):
        d = json.load(open(caminho, encoding='utf-8'))
        pai = CICLO_PAI.get(d['slug'])
        if pai:
            extra.setdefault(pai, []).extend(d['tables'])
    return extra


def main():
    itens, n_tab_total, n_tab_ok = [], 0, 0
    ciclos = carrega_ciclos()

    for caminho in sorted(glob.glob(os.path.join(RAIZ, 'build', 'src', '*.json'))):
        d = json.load(open(caminho, encoding='utf-8'))
        slug = d['slug']
        if slug not in COMPOSTOS:
            continue
        tabelas = []
        for t in d['tables'] + ciclos.get(slug, []):
            if not CORE.search(t['cap']):
                continue
            n_tab_total += 1
            linhas, ok = traduz_tabela(t)
            if not ok or len(linhas) < 2:
                continue
            largura = max(len(r) for r in linhas)
            if largura < 2:
                continue
            linhas = [r + [''] * (largura - len(r)) for r in linhas]
            n_tab_ok += 1
            tabelas.append({'cap': D.legenda(t['cap']), 'linhas': linhas})
        itens.append({'slug': slug, 'meta': COMPOSTOS[slug],
                      'tabelas': tabelas, 'n_tabelas': len(tabelas)})

    # paginas autorais: nao tem JSON de origem, o conteudo esta em proprios.py
    for slug, conteudo in PROPRIOS.items():
        n = sum(1 for s in conteudo['secoes'] if s.get('tabela'))
        n_tab_total += n
        n_tab_ok += n
        itens.append({'slug': slug, 'meta': COMPOSTOS[slug],
                      'tabelas': [], 'n_tabelas': n})

    stats = {
        'n': len(itens),
        'tabelas': n_tab_ok,
        'tabelas_total': n_tab_total,
        'nao_aprovados': sum(1 for i in itens if i['meta']['aprovado'] == 'nao'),
    }

    os.makedirs(os.path.join(RAIZ, 'p'), exist_ok=True)
    os.makedirs(os.path.join(RAIZ, 'assets'), exist_ok=True)

    def grava(rel, txt):
        with open(os.path.join(RAIZ, rel), 'w', encoding='utf-8', newline='\n') as f:
            f.write(txt)

    grava('index.html', gera_index(itens, stats))
    grava('evidencia.html', gera_evidencia())
    grava('seguranca.html', gera_seguranca())
    grava('sobre.html', gera_sobre(stats))
    grava(os.path.join('assets', 'app.js'), APP_JS)
    for i in itens:
        grava(os.path.join('p', i['slug'] + '.html'), gera_composto(i))

    print('compostos      :', stats['n'])
    print('tabelas core   :', n_tab_total)
    print('  publicadas   :', n_tab_ok)
    print('  descartadas  :', n_tab_total - n_tab_ok)
    print('paginas geradas:', stats['n'] + 3)
    semtab = [i['slug'] for i in itens if i['n_tabelas'] == 0]
    if semtab:
        print('sem tabela     :', ', '.join(semtab))


if __name__ == '__main__':
    main()
