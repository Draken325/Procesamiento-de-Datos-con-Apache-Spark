# Procesamiento-de-Datos-con-Apache-Spark
Descripción del Proyecto
  Este repositorio contiene una solución de ingeniería de datos diseñada para procesar el dataset de Casos positivos de COVID-19 en Colombia (Instituto Nacional de Salud). El objetivo  
  es demostrar la eficiencia del procesamiento distribuido frente a herramientas tradicionales cuando se manejan millones de registros.

Características Principales
  Procesamiento en Batch: Uso de PySpark (DataFrames) para la ingesta, limpieza y transformación de datos masivos.
  Análisis Exploratorio (EDA): Generación de indicadores estadísticos y visualizaciones sobre la distribución geográfica y demográfica de los casos.
  Arquitectura de Streaming: Implementación de un ecosistema de mensajería con Apache Kafka para la producción y consumo de datos en tiempo real.
  Ingesta vía API: Conexión directa con el portal de Datos Abiertos de Colombia para asegurar la actualidad de la información.

Tecnologías Utilizadas
  Lenguaje: Python 3.
  Procesamiento: Apache Spark.
  Mensajería: Apache Kafka.
  Análisis de datos: Pandas, Matplotlib.
  Entorno: Linux (VirtualBox).

Resultados
  La aplicación permite identificar las regiones con mayor impacto epidemiológico, optimizando los tiempos de respuesta mediante el particionamiento de datos y el motor de ejecución  
  Catalyst de Spark.
