# Apuração eleitoral por bairros — Ponte Nova (MG)

Projeto em Python para organizar os resultados da votação para presidente em Ponte Nova (MG), no segundo turno das eleições de 2026, agrupando os votos por bairro a partir da identificação das seções eleitorais.

## Como funciona

O script `main.py`:

1. Lê a base de boletins de urna (`bu_mg.csv`).
2. Seleciona os registros do município de Ponte Nova.
3. Lê a planilha que relaciona as seções eleitorais aos bairros (`secoes_por_bairros.xlsx`).
4. Cruza as duas bases pelo número da seção eleitoral.
5. Soma os votos por candidatura em cada bairro.
6. Exporta uma planilha Excel com o resultado.

## Organização dos arquivos

```text
apuracao-eleitoral-ponte-nova/
├── main.py
├── dados/
│   ├── bu_mg.csv
│   └── secoes_por_bairros.xlsx
├── resultados/
├── README.md
├── requirements.txt
└── .gitignore
```

Coloque os dois arquivos de entrada na pasta `dados/`. O arquivo gerado será salvo em `resultados/`.

## Como executar

É necessário ter Python instalado. No terminal, instale as dependências:

```bash
pip install -r requirements.txt
```

Depois, execute:

```bash
python main.py
```

## Dependências

- pandas
- openpyxl

## Observação metodológica

O agrupamento por bairro é feito a partir da correspondência entre seções eleitorais e bairros fornecida na planilha `secoes_por_bairros.xlsx`. Portanto, os totais representam os votos registrados nas seções associadas a cada bairro. Eles não identificam necessariamente o bairro de residência dos eleitores.

## Dados de entrada

A base de boletins de urna e a planilha de correspondência entre seções e bairros devem ser obtidas e incluídas localmente na pasta `dados/`. Verifique as condições de uso e redistribuição dos arquivos originais antes de publicá-los no repositório.
