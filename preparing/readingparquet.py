from pyspark.sql import SparkSession

# Step 1: Create SparkSession
spark = SparkSession.builder \
    .appName("ReadParquetExample") \
    .master("local[*]") \
    .getOrCreate()

# Step 2: Read Parquet file
# Replace 'your_file_path.parquet' with your actual Parquet file path
df = spark.read.parquet("C:/Users/HP/Downloads/titanic.parquet")

# Step 3: Show the content in the console
df.show()

# Optional: Print schema
df.printSchema()

# Stop the Spark session
spark.stop()
