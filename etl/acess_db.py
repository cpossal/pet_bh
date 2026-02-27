import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def conectar_postgres():
    load_dotenv()

    usuario = os.getenv("PG_USER")
    senha = os.getenv("PG_PASSWORD")
    host = os.getenv("PG_HOST")
    porta = os.getenv("PG_PORT")
    database = os.getenv("PG_DATABASE")

    if not all([usuario, senha, host, porta, database]):
        raise ValueError("❌ Variáveis de ambiente do banco não configuradas corretamente.")

    engine = create_engine(
        f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{database}"
    )

    return engine


def salvar_df_bd(df, nome_tabela, schema="public", if_exists="replace"):
    try:
        engine = conectar_postgres()

        df.to_sql(
            name=nome_tabela,
            con=engine,
            schema=schema,
            if_exists=if_exists,
            index=False
        )

        print(f"\n✅ Tabela '{nome_tabela}' criada com {len(df)} registros.")

    except Exception as e:
        print(f"\n❌ Erro ao salvar no banco: {e}")