
from pyspark import SparkContext

sc = SparkContext("local", "WordCountFiltering")

sentences = [
    "This is a simple sentence",
    "The word count program is written in PySpark",
    "PySpark is a powerful tool",
    "This tool is used for big data processing"
]

rdd = sc.parallelize(sentences)

stopwords = {"is", "the", "a", "an", "in", "for", "this"}

word_counts = (
    rdd.flatMap(lambda line: line.lower().split())
       .filter(lambda word: word not in stopwords)
       .map(lambda word: (word, 1))
       .reduceByKey(lambda x, y: x + y)
)

result = word_counts.collect()

for word, count in result:
    print(f"{word}: {count}")
