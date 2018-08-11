import csv
import random


def loadDataset(filename, split, trainingset=[], testset=[]):
    with open(filename, 'r') as  csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingset.append(dataset[x])
            else:
                testset.append(dataset[x])

trainingset = []
testset = []
loadDataset('iris.data', 0.7, trainingset, testset)
print("训练集合数："+repr(len(trainingset)))
print("测试集合数："+repr(len(testset)))
