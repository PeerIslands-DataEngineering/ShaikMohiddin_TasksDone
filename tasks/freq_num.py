from pyspark import SparkContext

sc = SparkContext.getOrCreate()

numbers = [5, 3, 4, 5, 2, 3, 5, 3, 4]

rdd = sc.parallelize(numbers)

freq_sorted = (
    rdd.map(lambda x: (x, 1))
       .reduceByKey(lambda a, b: a + b)
       .map(lambda x: (x[1], x[0]))
       .sortByKey(ascending=False)
)

print(freq_sorted.take(3))