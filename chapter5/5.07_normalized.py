import numpy as np

# 构建一个矩阵
a = np.array([6, 2, 14, -6, 10])
# 求最大值，最小值
a_min, a_max = a.min(), a.max()
print(a_min, a_max)
# 求归一化矩阵
a_normal = (a - a_min) / (a_max - a_min)
print(a_normal)
