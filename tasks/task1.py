from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Problem1_CurrencyStandardization") \
    .getOrCreate()

# Sample data (replace with your actual data loading)
data = [
    ("Company A", "$1.2B", "$3.5B", "$200B"),
    ("Company B", "$300M", "$1.8B", "$50B"),
    ("Company C", "$500M", "$900M", "$30B")
]
df = spark.createDataFrame(data, ["Company Name", "Total Funding", "ARR", "Valuation"])

# Define the UDF to convert currency strings to numeric values
def convert_currency(value):
    if not value or value == '':
        return None
    value = value.strip('$')
    if 'B' in value:
        return float(value.replace('B', '')) * 1_000_000_000
    elif 'M' in value:
        return float(value.replace('M', '')) * 1_000_000
    else:
        return float(value)

convert_currency_udf = udf(convert_currency, DoubleType())

# Apply the UDF to create new numeric columns
df = df.withColumn('Valuation_Num', convert_currency_udf(df['Valuation'])) \
       .withColumn('ARR_Num', convert_currency_udf(df['ARR'])) \
       .withColumn('Funding_Num', convert_currency_udf(df['Total Funding']))

# Show results
print("Problem 1 Results: Currency Standardization")
df.select("Company Name", "Total Funding", "Funding_Num", "ARR", "ARR_Num", "Valuation", "Valuation_Num").show()

# Stop Spark session
spark.stop()