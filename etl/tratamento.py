import pandas as pd

def tratar_dados(df: pd.DataFrame):
    # Exemplo: remover duplicados e preencher nulos
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df