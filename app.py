import pandas as pd

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# Parámetros de la conexión a la base de datos
db_params = {
    'user': 'postgres',
    'password': 'Jmqr3st0',
    'host': 'localhost',
    'port': '5432',
    'database': 'db'
}

conn_str = "postgresql://{user}:{password}@{host}:{port}/{database}".format(**db_params)
engine = create_engine(conn_str)

# Se crea una sesión
Session = sessionmaker(bind=engine)
session = Session()

def importar_csv_a_tabla(ruta_csv, nombre_tabla):
    # Cargar el archivo CSV en un DataFrame de pandas
    data_clap = pd.read_csv(ruta_csv)

    # Cargar el DataFrame en la tabla de la base de datos
    data_clap.to_sql(nombre_tabla, con=engine, if_exists='replace', index=False)

def ejecutar_consulta(consulta):
    # Obtener una conexión a la base de datos
    conn = engine.connect()

    # Ejecutar la consulta y obtener los resultados
    result = conn.execute(text(consulta))
    resultados = result.fetchall()

    # Cerrar la conexión
    conn.close()

    return resultados

if __name__ == "__main__":
    # Importación de CSV a data base Clap
    importar_csv_a_tabla("data/clap.csv", "clap")

    # Agrupar por ID_BANCO, ordenar y seleccionar el último registro en cada grupo
    # Luego filtrar solo las transacciones conciliables (TIPO_TRX == 'PAGADA')
    consulta = '''
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY "ID_BANCO" ORDER BY "FECHA_RECEPCION_BANCO" DESC) AS rn
    FROM clap
) AS ranked
WHERE "TIPO_TRX" = 'PAGADA' AND rn = 1;
                '''
    conciliable_txs_clap = ejecutar_consulta(consulta)

    print(len(conciliable_txs_clap))

    # Importación de CSV a data base Bansur
    importar_csv_a_tabla("data/bansur.csv", "bansur")

    # Agrupar por ID_ADQUIRIENTE, ordenar y seleccionar el último registro en cada grupo
    # Luego filtrar solo las transacciones conciliables (TIPO_TRX == 'PAGO')
    consulta = '''
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY "ID_ADQUIRIENTE" ORDER BY "FECHA_RECEPCION" DESC) AS rn
    FROM bansur
) AS ranked
WHERE "TIPO_TRX" = 'PAGO' AND rn = 1;
                '''
    conciliable_txs_bansur = ejecutar_consulta(consulta)

    print(len(conciliable_txs_bansur))

    # Cierra la conexión
    engine.dispose()
