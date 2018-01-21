data1 = [49, 66, 64, 15, 75, -51, 64, 75, 85, 21, -44, -33, -75, 12, 96]


# To find the mean of the data set below is the function for the same
def mean(data):
    mean = sum(data) / len(data)
    return mean


print(mean(data1))

# To find the median of the data set below is the function for the same


def median(data):
    sdata = sorted(data)
    index = int((len(data) - 1) / 2)    # Used int function as the output is in float
    return sdata[index]


print(median(data1))

# To find the mode of the data set below is the function for the same


def mode(data):
    modecnt = 0
    for i in range(len(data)):
        icount = data.count(data[i])
        if icount > modecnt:
            mode = data[i]
            modecnt = icount
    return mode


print(mode(data1))
