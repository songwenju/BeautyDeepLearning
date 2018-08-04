import matplotlib.pyplot as plt

dataSet = [[1.2, 1.1], [2.4, 3.5], [4.1, 3.2], [3.4, 2.8], [5, 5.4]]

x = [row[0] for row in dataSet]
y = [row[1] for row in dataSet]
plt.axis([0, 6, 0, 6])  # 横坐标从0到6，纵坐标从0到6
plt.plot(x, y, 'b')  # 分别以x和y列表为坐标点，画出方快散点图。“bs”为blue squares，
plt.grid()
plt.show()
plt.savefig("scatter.png")
