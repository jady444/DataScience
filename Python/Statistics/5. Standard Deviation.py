from math import sqrt
data2 = [13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12]


def mean(data):
    mean = sum(data) / len(data)
    return mean


def variance(data):
    mu = mean(data)
    return mean([(x - mu)**2 for x in data])


def stddev(data):
    return sqrt(variance(data2))


print(stddev(data2))
