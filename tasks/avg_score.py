from pyspark import SparkContext

sc = SparkContext.getOrCreate()

data = [("Alice", 80), ("Bob", 90), ("Alice", 70), ("Bob", 85), ("Charlie", 60)]

rdd = sc.parallelize(data)

avg_scores = (
    rdd.map(lambda x: (x[0], (x[1], 1)))
       .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
       .map(lambda x: (x[0], x[1][0] / x[1][1]))
)

print(avg_scores.collect())
