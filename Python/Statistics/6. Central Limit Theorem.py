import random
from math import sqrt


def mean(data):
    return float(sum(data) / len(data))


def variance(data):
    mu = mean(data)
    return sum([(float(x) - mu)**2 for x in data]) / len(data)


def stddev(data):
    return sqrt(variance(data))


def flip(N):
    return [random.random() > 0.5 for x in range(N)]


N = 1000
f = flip(N)

# print(f)
print(mean(f))
print(stddev(f))
