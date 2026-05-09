import pandas as pd
import numpy as np

df_vendas = pd.read_csv("vendas_tech.csv", low_memory=False)
df_gerentes = pd.read_excel("gerentes_lojas.xlsx")
