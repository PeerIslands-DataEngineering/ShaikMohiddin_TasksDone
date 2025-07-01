import os
import findspark

# Set JAVA_HOME and initialize Spark
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-11"
findspark.init()

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("CSV to DataFrame").getOrCreate()

# Read CSV
df = spark.read.csv(r"C:/Users/HP/Desktop/data.csv", header=True, inferSchema=True)

# Show data
df.show()

