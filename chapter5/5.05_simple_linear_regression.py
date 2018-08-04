from math import sqrt

dataSet = [[1.2, 1.1], [2.4, 3.5], [4.1, 3.2], [3.4, 2.8], [5, 5.4]]


# 定义求均值的函数
def mean(values):
    return sum(values) / float(len(values))


# 定义x与y协方差函数
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar


# 计算方差的函数
def variance(values, mean):
    return sum([(x - mean) ** 2 for x in values])


# 计算回归系数的函数
def coefficients(dataSet):
    x = [row[0] for row in dataSet]
    y = [row[1] for row in dataSet]
    x_mean, y_mean = mean(x), mean(y)
    w1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    w0 = y_mean - w1 * x_mean
    return w0, w1


# 计算根方误差RMSE
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
        mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)


# 构建简单线性回归
def simple_linear_regression(train, test):
    predictions = list()
    w0, w1 = coefficients(train)
    for row in test:
        y_model = w1 * row[0] + w0
        predictions.append(y_model)
    return predictions


# 评估算法数据准备及协调
def evaluate_algorithm(dataSet, algorithm):
    test_set = list()
    for row in dataSet:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)

    predicted = algorithm(dataSet, test_set)
    for val in predicted:
        print("%.3f\t" % (val))

    actual = [row[-1] for row in dataSet]
    rmse = rmse_metric(actual, predicted)
    return rmse


rmse = evaluate_algorithm(dataSet, simple_linear_regression)
print("RMSE:%.3f"%(rmse))
