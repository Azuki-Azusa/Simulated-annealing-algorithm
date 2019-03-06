import Map
import math
import random
import numpy
import copy
import matplotlib.pyplot as plt

class LS:
    def __init__(self, map, state):
        self.path = map
        l = []
        self.min = self.path
        for i in range(self.path.size()):
            l.append(i)
        for i in range(10):
            temp = Map.Map()
            l = numpy.random.permutation(l)
            for num in l:
                temp.add(self.path.path[0][num], self.path.path[1][num])
            if self.min.distance() > temp.distance():
                self.min = temp
        self.path = self.min
        self.times = 0
        self.state = state
        '''
        plt.plot(self.path.path[0], self.path.path[1])
        plt.scatter(self.path.path[0], self.path.path[1])
        plt.show()
        '''

    def run(self):
        while True:
            self.times += 1
            if self.state == 0:
                flag = self.select(self.neighbor())
            elif self.state == 1:
                flag = self.select(self.neighbor2())
            else:
                flag = self.select(self.neighbor3())
            if not flag:
                plt.plot(self.path.path[0], self.path.path[1])
                plt.scatter(self.path.path[0], self.path.path[1])
                plt.show()
                print(self.path.distance())
                break

    def neighbor(self):
        nb = []
        nb.append(self.path)
        for i in range(10 * self.path.size()):
            a = b = 0
            while a == b:
                a = random.randint(1, self.path.size() - 1)
                b = random.randint(1, self.path.size() - 1)
            temp = copy.deepcopy(self.path)
            temp.exchange(a, b)
            nb.append(temp)
        return nb

    def neighbor2(self):
        nb = []
        nb.append(self.path)
        for i in range(10 * self.path.size()):
            a = b = c = 0
            while a == b or b == c or a == c:
                a = random.randint(1, self.path.size() - 1)
                b = random.randint(1, self.path.size() - 1)
                c = random.randint(1, self.path.size() - 1)
            temp = copy.deepcopy(self.path)
            temp.exchange(a, b)
            temp.exchange(b, c)
            nb.append(temp)
        return nb

    def neighbor3(self):
        nb = []
        nb.append(self.path)
        for i in range(10 * self.path.size()):
            a = b = 0
            while a == b:
                a = random.randint(1, self.path.size() - 1)
                b = random.randint(1, self.path.size() - 1)
            a, b = min(a, b), max(a, b)
            tempx = self.path.path[0][a:b]
            tempy = self.path.path[1][a:b]
            tempx.reverse()
            tempy.reverse()
            tempx = self.path.path[0][:a] + tempx + self.path.path[0][b:]
            tempy = self.path.path[1][:a] + tempy + self.path.path[1][b:]
            temp = Map.Map()
            temp.path[0] = tempx
            temp.path[1] = tempy
            nb.append(temp)
        return nb

    def select(self, nb):
        temp = nb[0]
        change = False
        for path in nb:
            if path.distance() < temp.distance():
                change = True
                temp = path
        self.path = temp
        return change
