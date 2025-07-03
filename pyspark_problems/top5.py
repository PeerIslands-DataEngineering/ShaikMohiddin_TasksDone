from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, avg

spark = SparkSession.builder.appName("top5").getOrCreate()
df = spark.read.option("header", True).option("inferSchema", True).csv("D:/Downloads/passengers.csv")
df_filtered = df.filter(col("survived") == 1)
result = df_filtered.select("name","pclass","sex", "fare", "cabin").orderBy(col("fare").desc()).limit(5)
result.show()