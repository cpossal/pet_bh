import pandas as pd
from dbfread import DBF

def load_arqv(caminho_arquivo):
    if caminho_arquivo.endswith(".csv"):
        return pd.read_csv(caminho_arquivo)
    elif caminho_arquivo.endswith(".xlsx"):
        return pd.read_excel(caminho_arquivo)
    elif caminho_arquivo.endswith(".dbf"):
        table = DBF(caminho_arquivo, encoding='utf-8')
        return pd.DataFrame(iter(table))
    else:
        raise ValueError("Formato de arquivo não suportado")