from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, avg

spark = SparkSession.builder.appName("survival").getOrCreate()
df = spark.read.option("header", True).option("inferSchema", True).csv("D:/Downloads/passengers.csv")
df_group = df.groupBy("pclass", "sex").agg(round(avg("survived"), 2).alias("surviving_rate"))
df_ordered = df_group.orderBy(col("pclass"), col("surviving_rate").desc())

df_ordered.show()
