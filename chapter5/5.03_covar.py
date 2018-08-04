dataSet = [[1.2, 1.1], [2.4, 3.5], [4.1, 3.2], [3.4, 2.8], [5, 5.4]]
x = [row[0] for row in dataSet]
y = [row[1] for row in dataSet]


def mean(values):
    return sum(values) / float(len(values))


def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar


mean_x, mean_y = mean(x), mean(y)
covar = covariance(x, mean_x, y, mean_y)
print("协方差：%.3f" % (covar))
