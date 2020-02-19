from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from random import random

conf = SparkConf().setAppName("pi")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)

def sample(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

NUM_SAMPLES = 100000		#數值越大結果越準確
count = sc.parallelize(range(NUM_SAMPLES))
count = count.map(sample).reduce(lambda a, b: a + b)
print('='*30)
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
print('='*30)
