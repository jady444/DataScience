data2 = [13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12]


def mean(data):
    mean = sum(data) / len(data)
    return mean


# The below mentioned coding for variance is bit lengthy
def variance(data):
    mu = mean(data2)
    ndata = []
    for i in range(len(data)):
        ndata.append((data[i] - mu)**2)
    sigma = mean(ndata)
    return sigma


# Below mentioned coding for variance is easy and is in 2 steps
def variance1(data):
    mu1 = mean(data)
    return mean([(x - mu1)**2 for x in data])


print(variance(data2))
print(variance1(data2))
