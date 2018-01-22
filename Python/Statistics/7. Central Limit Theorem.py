from plotting import *
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


def sample(N):
    return [mean(flip(N)) for x in range(N)]


N = 1000
outcome = sample(N)
# print(outcome)
histplot(outcome, nbins=30)
