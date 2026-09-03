# Protocolos de Peptídeos

Referência em português sobre protocolos de peptídeos e compostos correlatos: dose, titulação, reconstituição, estrutura de ciclo e status regulatório, com o limite da evidência marcado em cada página.

**55 compostos e combinações · 266 tabelas de dose · 58 páginas estáticas.**

---

## ⚠️ Aviso

Material **educacional e experimental**. Nada aqui é recomendação médica, prescrição ou plano de tratamento.

A maior parte dos compostos não tem aprovação da ANVISA nem da FDA para uso humano. Vários são vendidos com rótulo de "uso exclusivo em pesquisa", o que significa que não passaram por controle de pureza, esterilidade ou dosagem para consumo por pessoas. **Dose descrita por comunidade não é dose validada.**

---

## Fonte e método

Os dados de protocolo foram compilados de [peptidedosingprotocols.com](https://www.peptidedosingprotocols.com/), acesso em 3 de setembro de 2026. É uma fonte secundária de caráter comercial, não uma publicação revisada por pares — e isso limita a confiabilidade de tudo que está aqui.

Três decisões de método:

1. **Nenhum número foi retipado à mão.** Todo valor de dose, volume, concentração e duração foi transportado por script, célula a célula. O que mudou foi o separador decimal (ponto → vírgula) e o separador de milhar (vírgula → ponto), porque `5,000 mcg` em inglês é cinco mil, e em português seria cinco. Retipar dose à mão é como se erra dose.

2. **Os textos em português são autorais.** Resumos, alertas e as seções de segurança foram escritos a partir da leitura da fonte, não traduzidos linha a linha. São mais curtos que o original.

3. **Portão de tradução.** Uma tabela só é publicada se passar num teste automático de sinal linguístico. Tabela que não passa é descartada, não publicada pela metade. O gerador reporta a contagem a cada execução.

Todo conteúdo comercial da fonte foi removido: links de fornecedor, cupons, seções de "onde comprar" e recomendação de loja.

### O que ficou de fora

- **Fontes primárias.** Nenhum artigo do PubMed, registro de ensaio clínico ou bula foi aberto para conferir os números. A checagem foi contra a fonte secundária, e só. É a limitação principal deste material.
- **Calculadoras interativas**, para não dar aparência de precisão a uma conta que depende de conferir o frasco na mão.
- **Fornecedores e preços**, deliberadamente.

---

## Estrutura

```
index.html            grade dos 55 compostos, com busca e filtro por categoria
seguranca.html        riscos que não aparecem na tabela de dose
sobre.html            fonte, método e limites
p/<slug>.html         uma página por composto
assets/estilo.css     sistema visual (escuro, acento de cobre)
assets/app.js         busca e filtro, sem dependências
build/gerar.py        gerador estático
build/compostos.py    metadados PT-BR de cada composto (autoral)
build/fatos.py        faixa de referência rápida por composto (autoral)
build/dicionario*.py  dicionário EN→PT-BR das células de tabela
```

## Regenerar

```bash
python build/gerar.py
```

O gerador depende de `build/src/*.json`, a extração da fonte — que **não está versionada** (ver `.gitignore`). O repositório guarda o material autoral e a ferramenta, não uma cópia do site de origem. Para reconstruir do zero é preciso refazer a extração localmente.

## Rodar

```bash
python -m http.server 8231
```

Sem build, sem dependências, sem JavaScript de terceiros. As fontes vêm do Google Fonts; o resto é local.

---

## Direitos

Valores numéricos de protocolo são fatos e não são objeto de direito autoral. A organização, os textos em português e o projeto visual são autorais. A fonte está creditada com link em todas as páginas.

Site pessoal, sem publicidade, sem afiliação e sem finalidade comercial. Havendo pedido justificado do detentor dos direitos da fonte, o material sai do ar.
