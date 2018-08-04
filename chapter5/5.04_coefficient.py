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


# 定义求方差的函数
def variance(values, means):
    return sum([(x - means) ** 2 for x in values])


# 计算回归系数的函数
def coefficients():
    x_mean, y_mean = mean(x), mean(y)
    w1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    w0 = y_mean - w1 * x_mean
    return w0, w1


w0, w1 = coefficients()
print("回归系数分别为：w0 = %.3f,w1=%.3f" % (w0, w1))
