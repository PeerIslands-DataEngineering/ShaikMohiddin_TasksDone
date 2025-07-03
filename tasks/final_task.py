
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, avg, count, round as spark_round
from pyspark.sql.types import DoubleType
import pandas as pd

spark = SparkSession.builder.appName("HiddenGemsAnalysis").getOrCreate()

def parse_money(val):
    if val is None:
        return None
    val = val.replace('$', '').strip().upper()
    try:
        if val.endswith('K'):
            return float(val[:-1]) * 1e3
        elif val.endswith('M'):
            return float(val[:-1]) * 1e6
        elif val.endswith('B'):
            return float(val[:-1]) * 1e9
        elif val.endswith('T'):
            return float(val[:-1]) * 1e12
        else:
            return float(val)
    except:
        return None

parse_money_udf = udf(parse_money, DoubleType())


df = spark.read.option("header", True).csv("C:/Users/HP/Downloads/startups_100_rows.csv")
df = df.withColumn("ARR", parse_money_udf(col("ARR")))
df = df.withColumn("Valuation", parse_money_udf(col("Valuation")))
df = df.withColumn("G2 Rating", col("G2 Rating").cast("double"))
df = df.withColumn("Founded Year", col("Founded Year").cast("int"))


filtered = df.filter(
    (col("ARR") > 100_000_000) &
    (col("Valuation") < 500_000_000) &
    (col("G2 Rating") >= 4.0) &
    (col("Founded Year") >= 2015)
)

result = (
    filtered.groupBy("Industry")
    .agg(
        count("*").alias("NumCompanies"),
        spark_round(avg("ARR"), 2).alias("AvgARR"),
        spark_round(avg("Valuation"), 2).alias("AvgValuation")
    )
    .filter(col("NumCompanies") >= 2)
    .orderBy(col("AvgARR").desc())
)


result.show(truncate=False)
