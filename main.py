import pandas as pd
from pathlib import Path

pasta = Path(__file__).parent
dados_dir = pasta / "dados"
resultados_dir = pasta /"resultados"

resultados_dir.mkdir(exist_ok=True)

df = pd.read_csv(dados_dir / "bu_mg.csv", sep=';', encoding='latin1')

df_pn = df[df["NM_MUNICIPIO"]=="PONTE NOVA"] #variável que recebe a tabela para PN

bairros = pd.read_excel(dados_dir / "secoes_por_bairros.xlsx") #seções por bairros em PN

df_cruzado = df_pn.merge(
    bairros, 
    left_on="NR_SECAO",
    right_on="SECOES",
    how="left"
)

votos_bairro = df_cruzado.pivot_table(
    index="BAIRROS",
    columns="NM_VOTAVEL",
    values="QT_VOTOS",
    aggfunc="sum",
    fill_value=0
).reset_index()

votos_bairro.to_excel( resultados_dir /
    "resultao_da_apuração_bairros_PN.xlsx",
    index=False
)

print("concluido")