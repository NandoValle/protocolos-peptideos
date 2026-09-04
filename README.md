# Protocolos — peptídeos, nootrópicos e correlatos

Referência em português sobre peptídeos, nootrópicos, SARMs e compostos correlatos: dose, titulação, reconstituição, estrutura de ciclo e status regulatório, com o limite da evidência marcado em cada página.

O repositório e a URL guardam o nome antigo, `protocolos-peptideos` — renomear quebraria todo link já publicado. O site cobre mais que peptídeos desde setembro de 2026.

**70 compostos e combinações · 362 tabelas de dose · 73 páginas estáticas.**

Contagens da última execução do gerador, em 4 de setembro de 2026. Ele as imprime a cada rodada — se divergirem daqui, o gerador é que está certo.

### ▶ [protocolos-peptideos.github.io](https://protocolos-peptideos.github.io/)

Publicado por GitHub Pages a partir deste repositório.

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

- **Fontes primárias, nas páginas importadas.** Nas páginas de protocolo vindas da fonte secundária, nenhum artigo do PubMed, registro de ensaio ou bula foi aberto: a checagem foi contra a fonte, e só. Continua sendo a limitação principal delas.
- **A exceção são as páginas de evidência verificada**, hoje 13, onde cada número foi levantado no PubMed, no ClinicalTrials.gov, no dado aberto da ANVISA, na bula ou na lista da WADA, com a consulta declarada na própria página.
- **Calculadoras interativas**, para não dar aparência de precisão a uma conta que depende de conferir o frasco na mão.
- **Fornecedores e preços**, deliberadamente.

---

## Estrutura

```
index.html            grade dos compostos, com busca e filtro por categoria
seguranca.html        riscos que não aparecem na tabela de dose
sobre.html            fonte, método e limites
p/<slug>.html         uma página por composto
assets/estilo.css     sistema visual (escuro, acento de cobre)
assets/app.js         busca e filtro, sem dependências
build/gerar.py        gerador estático
build/compostos.py    metadados PT-BR de cada composto (autoral)
build/fatos.py        faixa de referência rápida por composto (autoral)
build/dicionario*.py  dicionário EN→PT-BR das células de tabela
build/datas.py        as duas datas do site, num lugar só
build/trava_datas.py  trava que impede data cravada ou tirada do relógio
hooks/pre-commit      roda a trava antes de deixar commitar
```

## As duas datas, e por que existe uma trava para elas

O site afirma duas datas sobre si mesmo: **3 de setembro de 2026**, quando a fonte secundária foi raspada, e **4 de setembro de 2026**, quando a apuração em fonte primária foi feita. As duas vivem em `build/datas.py` e em nenhum outro lugar.

A tentação óbvia é trocá-las por `datetime.now()`. **Não pode.** O gerador roda de novo a cada edição de texto; com data de relógio, o site passaria a afirmar, a cada rebuild, que foi conferido hoje — sem que ninguém tenha conferido nada. Data velha e correta vale mais que data fresca e falsa.

`build/trava_datas.py` transforma isso em garantia. Checa o AST, não o texto, para não acusar comentário que apenas mencione o problema. Duas regras: nenhum módulo deriva data do relógio, e nenhum módulo além do `datas.py` escreve à mão as datas do próprio site. Data que é **conteúdo** — quando um ensaio começou, quando a FDA revisou uma bula — fica onde está: é fato reportado, não afirmação do site sobre si.

A trava roda no início do `gerar.py`, que aborta sem escrever nada, e no hook de pre-commit. **Num clone novo o hook precisa ser ligado uma vez:**

```bash
git config core.hooksPath hooks
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
