# -*- coding: utf-8 -*-
"""Dicionario EN->PT-BR para celulas e legendas de tabela.

Regra de seguranca: numeros nunca sao reescritos por traducao livre.
Apenas a virgula decimal e aplicada, e a unidade e traduzida por regex.
"""
import re
from dicionario2 import FRASES as _FRASES
from dicionario2 import LEGENDAS_FIXAS as _LEG_FIXAS

# ---------------------------------------------------------------- exatos
EXATO = {
    # cabecalhos de coluna
    "Phase": "Fase", "Dose": "Dose", "Frequency": "Frequência",
    "Duration": "Duração", "Notes": "Observações", "Timing": "Horário",
    "Route": "Via", "Week": "Semana", "Weeks": "Semanas",
    "Marker": "Marcador", "Why it matters": "Por que importa",
    "State": "Estado", "Storage": "Armazenamento", "Concentration": "Concentração",
    "Vial Size": "Frasco", "Vial size": "Frasco", "Volume": "Volume",
    "Feature": "Item", "Compound": "Composto", "Approach": "Abordagem",
    "Off Period": "Intervalo", "Off period": "Intervalo",
    "Best For": "Indicado para", "Best for": "Indicado para",
    "Daily dose": "Dose diária", "Daily Dose": "Dose diária",
    "Appearance": "Aspecto", "FDA status": "Status FDA",
    "Window": "Janela", "BAC Water": "Água bacteriostática",
    "BAC water": "Água bacteriostática", "BAC water added": "Água bacteriostática",
    "Draw volume": "Volume a aspirar", "Draw Volume": "Volume a aspirar",
    "Total blend delivered": "Total da blend entregue",
    "Component": "Componente", "Amount": "Quantidade",
    "Protocol": "Protocolo", "Schedule": "Esquema", "Cycle": "Ciclo",
    "Target": "Alvo", "Result": "Resultado", "Effect": "Efeito",
    "Evidence": "Evidência", "Status": "Status", "Source": "Fonte",
    "Type": "Tipo", "Level": "Nível", "Range": "Faixa", "Value": "Valor",
    "Test": "Exame", "When": "Quando", "What": "O quê", "Why": "Por quê",
    "Step": "Passo", "Action": "Ação", "Format": "Formato",
    "Half-life": "Meia-vida", "Half life": "Meia-vida",
    "Mechanism": "Mecanismo", "Onset": "Início de efeito",
    "Units": "Unidades", "Unit": "Unidade", "Syringe": "Seringa",
    "Injection": "Injeção", "Total": "Total", "Ratio": "Proporção",
    # estados / valores
    "Baseline": "Basal", "Follow-up": "Reavaliação", "Follow up": "Reavaliação",
    "Optional": "Opcional", "Yes": "Sim", "No": "Não", "None": "Nenhum",
    "Standard": "Padrão", "Extended": "Estendido", "Maintenance": "Manutenção",
    "Conservative": "Conservador", "Aggressive": "Agressivo",
    "Low": "Baixo", "Moderate": "Moderado", "High": "Alto",
    "Strong": "Forte", "Weak": "Fraco", "Limited": "Limitada",
    "Mixed": "Misto", "Unknown": "Desconhecido", "Varies": "Variável",
    "Not approved": "Não aprovado", "Not FDA-approved": "Não aprovado pela FDA",
    "Approved": "Aprovado", "Research only": "Apenas pesquisa",
    "Lyophilized (powder)": "Liofilizado (pó)", "Lyophilized": "Liofilizado",
    "Reconstituted (liquid)": "Reconstituído (líquido)",
    "Reconstituted": "Reconstituído", "Powder": "Pó", "Liquid": "Líquido",
    "Refrigerated": "Refrigerado", "Frozen": "Congelado",
    "Room temperature": "Temperatura ambiente",
    "Subcutaneous": "Subcutânea", "SubQ": "Subcutânea", "Subq": "Subcutânea",
    "Intranasal": "Intranasal", "Nasal": "Nasal", "Oral": "Oral",
    "Intramuscular": "Intramuscular", "Topical": "Tópico",
    "Sublingual": "Sublingual", "Injectable": "Injetável",
    "Morning": "Manhã", "Evening": "Noite", "Night": "Noite",
    "Bedtime": "Antes de dormir", "Pre-workout": "Pré-treino",
    "Post-workout": "Pós-treino", "Fasted": "Em jejum",
    "With food": "Com alimento", "Empty stomach": "Estômago vazio",
    "Once daily": "1×/dia", "Twice daily": "2×/dia",
    "Three times daily": "3×/dia", "Once weekly": "1×/semana",
    "Twice weekly": "2×/semana", "Daily": "Diário", "Weekly": "Semanal",
    "Every other day": "Dias alternados", "As needed": "Conforme necessário",
    "Continuous": "Contínuo", "Cycled": "Em ciclos",
    # exames de sangue
    "Comprehensive metabolic panel (CMP)": "Painel metabólico completo (CMP)",
    "Complete blood count (CBC)": "Hemograma completo",
    "CBC with differential": "Hemograma completo com diferencial",
    "Lipid panel": "Perfil lipídico", "Fasting glucose": "Glicemia de jejum",
    "A1c": "Hemoglobina glicada (HbA1c)", "HbA1c": "Hemoglobina glicada (HbA1c)",
    "TSH and free T4": "TSH e T4 livre", "TSH": "TSH",
    "CRP": "PCR (proteína C reativa)",
    "hs-CRP": "PCR ultrassensível", "IGF-1": "IGF-1",
    "Liver enzymes (ALT/AST)": "Enzimas hepáticas (ALT/AST)",
    "Kidney function (eGFR)": "Função renal (TFGe)",
    "Blood pressure and resting heart rate": "Pressão arterial e frequência cardíaca de repouso",
    "Blood pressure": "Pressão arterial", "Serum copper": "Cobre sérico",
    "Ceruloplasmin": "Ceruloplasmina", "Ferritin": "Ferritina",
    "Testosterone": "Testosterona", "Estradiol": "Estradiol",
    "Prolactin": "Prolactina", "Cortisol": "Cortisol",
    "Amylase and lipase": "Amilase e lipase", "Vitamin B12": "Vitamina B12",
    "Electrolytes": "Eletrólitos", "Uric acid": "Ácido úrico",
    "Weight and waist circumference": "Peso e circunferência abdominal",
    "Longer term": "Longo prazo", "Long term": "Longo prazo",
    "Every 8-12 weeks": "A cada 8–12 semanas",
    "Every 12 weeks": "A cada 12 semanas",
    "Before starting": "Antes de iniciar",
    "—": "—", "-": "—", "N/A": "n/d", "TBD": "a definir",
}

# --------------------------------------------------------------- regras
REGRAS = [
    # semanas / dias / meses
    (r'^Weeks?\s+(\d+)\s*[-–]\s*(\d+)(.*)$', lambda m: 'Semanas %s–%s%s' % (m.group(1), m.group(2), m.group(3))),
    (r'^Weeks?\s+(\d+)\+(.*)$', lambda m: 'Semana %s em diante%s' % (m.group(1), m.group(2))),
    (r'^Weeks?\s+(\d+)(.*)$', lambda m: 'Semana %s%s' % (m.group(1), m.group(2))),
    (r'^Days?\s+(\d+)\s*[-–]\s*(\d+)$', lambda m: 'Dias %s–%s' % (m.group(1), m.group(2))),
    (r'^Months?\s+(\d+)\s*[-–]\s*(\d+)$', lambda m: 'Meses %s–%s' % (m.group(1), m.group(2))),
    (r'^Month\s+(\d+)$', lambda m: 'Mês %s' % m.group(1)),
    (r'\b(\d+)\s*[-–]\s*(\d+)\s+weeks\b', lambda m: '%s–%s semanas' % (m.group(1), m.group(2))),
    (r'\b(\d+)\s+weeks\b', lambda m: '%s semanas' % m.group(1)),
    (r'\b(\d+)\s+week\b', lambda m: '%s semana' % m.group(1)),
    (r'\b(\d+)\s*[-–]\s*(\d+)\s+days\b', lambda m: '%s–%s dias' % (m.group(1), m.group(2))),
    (r'\b(\d+)\s+days\b', lambda m: '%s dias' % m.group(1)),
    (r'\b(\d+)\s*[-–]\s*(\d+)\s+months\b', lambda m: '%s–%s meses' % (m.group(1), m.group(2))),
    (r'\b(\d+)\s+months\b', lambda m: '%s meses' % m.group(1)),
    (r'\b(\d+)\s+hours?\b', lambda m: '%s h' % m.group(1)),
    (r'\b(\d+)\s+minutes?\b', lambda m: '%s min' % m.group(1)),
    # temperatura: descarta Fahrenheit, mantem Celsius
    (r'\b[\d.]+\s*[-–]\s*[\d.]+\s*F\s*\(\s*([\d]+)\s*[-–]\s*([\d]+)\s*C\s*\)', lambda m: '%s–%s °C' % (m.group(1), m.group(2))),
    (r'\b([\d.]+)\s*F\s*\(\s*([\d.]+)\s*C\s*\)', lambda m: '%s °C' % m.group(2)),
    # unidades de seringa
    (r'\((\d+(?:[.,]\d+)?)\s*units?\)', lambda m: '(%s unidades)' % m.group(1)),
    (r'\b(\d+(?:[.,]\d+)?)\s*units\b', lambda m: '%s unidades' % m.group(1)),
    (r'\b(\d+(?:[.,]\d+)?)\s*unit\b', lambda m: '%s unidade' % m.group(1)),
    # frequencia
    (r'\bonce\s+daily\b', lambda m: '1×/dia'),
    (r'\btwice\s+daily\b', lambda m: '2×/dia'),
    (r'\bthree\s+times\s+daily\b', lambda m: '3×/dia'),
    (r'\bonce\s+weekly\b', lambda m: '1×/semana'),
    (r'\btwice\s+weekly\b', lambda m: '2×/semana'),
    (r'\b(\d+)x\s*/?\s*(?:per\s+)?day\b', lambda m: '%s×/dia' % m.group(1)),
    (r'\b(\d+)x\s*/?\s*(?:per\s+)?week\b', lambda m: '%s×/semana' % m.group(1)),
    (r'\bper\s+day\b', lambda m: 'por dia'),
    (r'\bper\s+week\b', lambda m: 'por semana'),
    (r'\bdaily\b', lambda m: 'diário'),
    (r'\bweekly\b', lambda m: 'semanal'),
    # vocabulario solto frequente
    (r'\btotal blend\b', lambda m: 'da blend total'),
    (r'\bvial\b', lambda m: 'frasco'),
    (r'\bsyringe\b', lambda m: 'seringa'),
    (r'\bnasal spray\b', lambda m: 'spray nasal'),
    (r'\binjection\b', lambda m: 'injeção'),
    (r'\bcapsule[s]?\b', lambda m: 'cápsulas'),
    (r'\btablet[s]?\b', lambda m: 'comprimidos'),
    (r'\bpowder\b', lambda m: 'pó'),
    (r'\bsplit\b', lambda m: 'dividida'),
    (r'\btaper\b', lambda m: 'desmame'),
    (r'\btitration\b', lambda m: 'titulação'),
    (r'\bloading\b', lambda m: 'ataque'),
    (r'\bmaintenance\b', lambda m: 'manutenção'),
    (r'\bwashout\b', lambda m: 'washout'),
    (r'\bcycle\b', lambda m: 'ciclo'),
    (r'\bon\b(?=\s*/\s*)', lambda m: 'on'),
    (r'\bmonitor\b', lambda m: 'monitorar'),
    (r'\bbaseline\b', lambda m: 'basal'),
    (r'\bstore\b', lambda m: 'armazenar'),
    (r'\bprotect from light\b', lambda m: 'proteger da luz'),
    (r'\bdiscard\b', lambda m: 'descartar'),
    (r'\brefrigerate[d]?\b', lambda m: 'refrigerado'),
    (r'\broom temp(?:erature)?\b', lambda m: 'temperatura ambiente'),
    # taxas por dia/semana/mes coladas na unidade
    (r'/\s*day\b', lambda m: '/dia'),
    (r'/\s*week\b', lambda m: '/semana'),
    (r'/\s*month\b', lambda m: '/mês'),
    (r'/\s*dose\b', lambda m: '/dose'),
    (r'^Days$', lambda m: 'Dias'),
    (r'^Weeks?$', lambda m: 'Semanas'),
    (r'\b(\d+)\+\s*weeks\b', lambda m: '%s+ semanas' % m.group(1)),
    (r'\b(\d+)\+\s*days\b', lambda m: '%s+ dias' % m.group(1)),
    (r'^(\d[\d.,]*\s*(?:mg|mcg|g|mL))\s+Dose$', lambda m: 'Dose de %s' % m.group(1)),
    (r'\bweek\s+(\d+)\b', lambda m: 'semana %s' % m.group(1)),
    (r'\bweeks\s+(\d+)\s*[-–]\s*(\d+)\b', lambda m: 'semanas %s–%s' % (m.group(1), m.group(2))),
    (r'\bweeks\s+(\d+)\s+e\s+(\d+)\b', lambda m: 'semanas %s e %s' % (m.group(1), m.group(2))),
    (r'\b(\d+)-week\b', lambda m: 'de %s semanas' % m.group(1)),
    (r'\b(\d+)-day\b', lambda m: 'de %s dias' % m.group(1)),
    (r'\badditional weeks\b', lambda m: 'semanas adicionais'),
    (r'^Days on$', lambda m: 'Dias ativos'),
    (r'^Pulsed week$', lambda m: 'Semana pulsada'),
    (r'^Draw \(units\)$', lambda m: 'Aspirar (unidades)'),
    (r'^Units \(U-100 seringa\)$', lambda m: 'Unidades (seringa U-100)'),
    (r'\bU-100\s+(?:seringa\s+)?units\b', lambda m: 'unidades na seringa U-100'),
    (r'\bInsulin units\b', lambda m: 'unidades de insulina'),
    (r'\bUnits on U-100 seringa\b', lambda m: 'Unidades na seringa U-100'),
    (r'\bapprox\.?\b', lambda m: 'aprox.'),
    (r'\bup to\b', lambda m: 'até'),
    (r'\bor\b', lambda m: 'ou'),
    (r'\band\b', lambda m: 'e'),
]

# legendas de tabela
LEGENDAS = [
    (r'Storage & Handling', 'Armazenamento e manuseio'),
    (r'Blood Tests & Monitoring', 'Exames de sangue e monitoramento'),
    (r'Reconstitution Guide', 'Guia de reconstituição'),
    (r'Reconstitution Math', 'Cálculo de reconstituição'),
    (r'Reconstitution Format', 'Formato de reconstituição'),
    (r'Reconstitution by Vial Format', 'Reconstituição por formato de frasco'),
    (r'Reconstitution by Format', 'Reconstituição por formato'),
    (r'Reconstitution', 'Reconstituição'),
    (r'Timeline & What to Monitor', 'Linha do tempo e o que monitorar'),
    (r'Cycle Guidelines', 'Diretrizes de ciclo'),
    (r'Cycle structure', 'Estrutura do ciclo'),
    (r'Protocol Formats', 'Formatos de protocolo'),
    (r'protocol formats', 'formatos de protocolo'),
    (r'Dosing Protocol & Schedule', 'Protocolo e esquema de dose'),
    (r'Dosing Guide by Route', 'Guia de dose por via'),
    (r'Dosing by Formulation', 'Dose por formulação'),
    (r'Dosing Patterns', 'Padrões de dose'),
    (r'Dosing Protocol', 'Protocolo de dose'),
    (r'Dosing Guide', 'Guia de dose'),
    (r'Dosage Chart', 'Tabela de doses'),
    (r'Dosage Per Day', 'Dose por dia'),
    (r'Dosage and Research Evidence', 'Dose e evidência'),
    (r'Evidence boundary', 'Limite da evidência'),
    (r'Current evidence', 'Evidência atual'),
    (r'Full Staggered Titration Schedule', 'Esquema completo de titulação escalonada'),
    (r'Community SubQ titration pattern', 'Padrão de titulação subcutânea (comunidade)'),
    (r'Oral Tablet Titration', 'Titulação em comprimido oral'),
    (r'Oral Capsules vs Injection', 'Cápsula oral vs. injeção'),
    (r'Half-Life and Dosing Frequency', 'Meia-vida e frequência de dose'),
    (r'Benefits and Results: What the Evidence Shows', 'Efeitos e resultados: o que a evidência mostra'),
    (r'Benefits: Claims vs Evidence', 'Efeitos: alegação vs. evidência'),
    (r'What Is the Difference\?', 'qual é a diferença?'),
    (r'which format\?', 'qual formato?'),
    (r'\bvs\b', 'vs.'),
    (r'\bSchedule\b', 'Esquema'),
    (r'\bCalculator\b', 'Calculadora'),
]


def _decimal_ptbr(texto):
    """1.5 mL -> 1,5 mL   (nao toca em 1.5.2 nem em datas)"""
    return re.sub(r'(?<=\d)\.(?=\d)', ',', texto)


def celula(txt):
    if not txt:
        return txt
    s = txt.strip()
    if s in EXATO:
        return EXATO[s]
    for pat, rep in REGRAS:
        s = re.sub(pat, rep, s, flags=re.I)
    s = _decimal_ptbr(s)
    # segunda passada: frases inteiras que sobraram hibridas
    return _FRASES.get(s, s)


def legenda(txt):
    s = txt.strip()
    for pat, rep in LEGENDAS:
        s = re.sub(pat, rep, s)
    s = s.replace('vs..', 'vs.').replace('vs. .', 'vs.')
    return _LEG_FIXAS.get(s, s)
