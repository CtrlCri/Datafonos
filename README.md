# Proyecto de Conciliación de Transacciones CLAP-BANSUR

Este proyecto tiene como objetivo realizar la comparación de transacciones entre las bases de datos de CLAP y BANSUR, dos entidades involucradas en el procesamiento de pagos a través de datáfonos. Se busca verificar la coherencia entre las transacciones registradas en ambas bases y analizar los resultados obtenidos.

## Descripción

El proyecto se enfoca en los siguientes pasos:

1. Carga de datos: Cargar los datos de las bases de datos CLAP y BANSUR en DataFrames de pandas.
2. Filtrado y limpieza: Aplicar filtros para considerar únicamente las transacciones relevantes (PAGADAS) y realizar cualquier limpieza necesaria en los datos.
3. Conciliación: Comparar los campos únicos entre las dos entidades y establecer condiciones para considerar transacciones como conciliables.
4. Análisis: Calcular montos totales, cantidades y porcentajes de transacciones conciliables y no conciliables.
5. Visualización: Crear gráficos para representar los resultados de manera visual.

## Requisitos

- Python 3.x
- Jupyter Notebook u otro entorno de programación similar
- Bibliotecas de Python: pandas, matplotlib, seaborn
- PostgreSQL
- pgAdmin (opcional, para interfaz gráfica de PostgreSQL)

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.
2. Abre el archivo Jupyter Notebook `script.ipynb` en tu entorno de programación.
3. Sigue los pasos descritos en el Notebook para cargar los datos, realizar la conciliación y analizar los resultados.
4. Utiliza los gráficos generados para visualizar los porcentajes de transacciones cruzadas y no cruzadas.
5. Por otro lado, en app.py tienes la conexion a la base de datos y las consultas; puedes ajecutar el mismo desde la terminal.

## Resultados

Los resultados del proyecto se presentan en el Notebook y se resumen en gráficos que ayudan a visualizar cómo se comparan las transacciones entre CLAP y BANSUR en términos de conciliación y cruces.

## Contacto

Si tienes preguntas o comentarios sobre este proyecto, no dudes en contactarme en [CtrlCri](mailto:aramayoreyes@gmail.com).
