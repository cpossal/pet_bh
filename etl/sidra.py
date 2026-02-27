import sidrapy

def consultar_sidra(tabela: str):
    df = sidrapy.get_table(table_code=tabela)
    return df