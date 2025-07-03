from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, avg

spark = SparkSession.builder.appName("survival").getOrCreate()
df = spark.read.option("header", True).option("inferSchema", True).csv("D:/Downloads/passengers.csv")
df_filtered = df.filter(col("fare").isNotNull())
df_group = df_filtered.groupBy("embarked").agg(round(avg("age"),2).alias("avg_age"), round(avg("fare"),2).alias("avg_fare"))
df_ordered = df_group.orderBy(col("avg_fare").desc())
df_ordered.show()