from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

# 1. Inicializar sesión de Spark
spark = SparkSession.builder \
    .appName("AnalisisCovidColombiaAPI") \
    .getOrCreate()

# 2. Cargar datos desde la API
url = "https://www.datos.gov.co/resource/gt2j-8ykr.csv?$limit=100000"
print("Cargando datos desde la API... por favor espera.")

try:
    response = requests.get(url)
    data = StringIO(response.text)
    pdf = pd.read_csv(data)
    df_covid = spark.createDataFrame(pdf)

    # 3. Limpieza y Transformación
    df_limpio = df_covid.select(
        col("departamento_nom").alias("departamento"),
        col("edad"),
        col("sexo"),
        col("estado")
    ).filter(col("departamento").isNotNull())

    # Análisis: Cantidad de casos por departamento
    df_analisis = df_limpio.groupBy("departamento") \
        .agg(count("*").alias("total_casos")) \
        .orderBy(desc("total_casos"))

    # Mostrar resultados en consola
    print("\n--- RESULTADOS DEL PROCESAMIENTO EN BATCH ---")
    df_analisis.show(10)

    # 4. Visualización
    top_10 = df_analisis.limit(10).toPandas()
    plt.figure(figsize=(12,6))
    plt.bar(top_10['departamento'], top_10['total_casos'], color='#2E86C1')
    plt.title('Distribución de Casos por Departamento')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    print("\nMostrando gráfica... Cierra la ventana de la imagen para continuar.")
    plt.show()

except Exception as e:
    print(f"Ocurrió un error: {e}")

# --- Input para cierre ---
print("\n" + "="*40)
input("PROCESO FINALIZADO. Presiona [ENTER] para cerrar la sesión de Spark...")
print("Cerrando... ¡Adiós!")
# --------------------------------

spark.stop()
