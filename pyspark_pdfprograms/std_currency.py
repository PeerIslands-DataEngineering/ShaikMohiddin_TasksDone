from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType
df = SparkSession.builder.appName("std_currency").getOrCreate().read.csv("D:\Downloads\saas_companies_50rows_clean.csv", header = True)

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

df = df.withColumn("arr", parse_money_udf(col("ARR")))
df = df.withColumn("valuation", parse_money_udf(col("Valuation")))
df = df.withColumn("total funding", parse_money_udf(col("Total Funding")))
df.show()


