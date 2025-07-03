import os
import findspark

# Set JAVA_HOME and initialize Spark
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21"
findspark.init()

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("CSV to DataFrame").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Read CSV
df = spark.read.csv(r"C:\Users\HP\Downloads\sample_companies_100.csv", header=True, inferSchema=True)

# Show data
df.show()

