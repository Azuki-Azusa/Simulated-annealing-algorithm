import Map
import math
import random
import matplotlib.pyplot as plt
import copy
import numpy


class SA:
    def __init__(self, map, T, cool):
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
        self.T = T
        self.cool = cool
        self.times = 0
        self.sameTimes = 0
        self.distance = self.path.distance()
        self.best = self.path.distance()
        if self.path.size() < 30:
            coolingEnhancer = 0.5
        elif self.path.size() < 150:
            coolingEnhancer = 0.05
        elif self.path.size() < 750:
            coolingEnhancer = 0.005
        else:
            coolingEnhancer = 0.0005
        self.coolingEnhancer = coolingEnhancer

        plt.clf()
        plt.plot(self.path.path[0], self.path.path[1])
        plt.scatter(self.path.path[0],
                    self.path.path[1])
        plt.show()
        self.Tl = []
        self.timsl = []
        self.dl = []

    def run(self):
        print("BEGIN Distance: ", self.path.distance())
        while self.T >= 1:
            self.timsl.append(self.times)
            self.Tl.append(self.T)
            self.dl.append(self.path.distance())
            self.judge()

            if self.path.distance() == self.distance:
                self.sameTimes += 1
                '''
                if self.sameTimes == 2000:
                    self.T *= 200
                    self.sameTimes = 0
                '''
            else:
                self.sameTimes = 0
                self.distance = self.path.distance()

        plt.clf()
        plt.plot(self.path.path[0], self.path.path[1])
        plt.scatter(self.path.path[0], self.path.path[1])
        plt.show()
        plt.clf()
        plt.rcParams['figure.figsize'] = (10, 6)
        plt.plot(self.timsl, self.Tl)
        #plt.scatter(self.timsl, self.Tl)
        plt.show()
        plt.clf()
        plt.rcParams['figure.figsize'] = (10, 6)
        plt.plot(self.timsl, self.dl)
        #plt.scatter(self.timsl, self.dl)
        plt.show()

        print("END Distance:", self.path.distance())
        print("Times:", self.times)
        print("Excess:", '%.2f%%' % ((self.path.distance() - 629) / 629 * 100))

    def move(self):
        a = 0
        b = 0
        while a == b:
            a = random.randint(1, self.path.size() - 1)
            b = random.randint(1, self.path.size() - 1)
        return a, b

    def neighbor(self):
        a = b = 0
        while a == b:
            a = random.randint(1, self.path.size() - 1)
            b = random.randint(1, self.path.size() - 1)
        t = copy.deepcopy(self.path)
        t.exchange(a, b)
        temp = t
        d = temp.distance()
        '''
        for i in range(10):
            a = b = 0
            while a == b:
                a = random.randint(1, self.path.size() - 1)
                b = random.randint(1, self.path.size() - 1)
            t = copy.deepcopy(self.path)
            t.exchange(a, b)
            if t.distance() < d:
                temp = t
                d = t.distance()

        for i in range(10):
            a = b = c = 0
            while a == b or b == c or a == c:
                a = random.randint(1, self.path.size() - 1)
                b = random.randint(1, self.path.size() - 1)
                c = random.randint(1, self.path.size() - 1)
            t = copy.deepcopy(self.path)
            t.exchange(a, b)
            t.exchange(b, c)
            if t.distance() < d:
                temp = t
                d = t.distance()
        '''

        for i in range(5):
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
            t = Map.Map()
            t.path[0] = tempx
            t.path[1] = tempy
            if t.distance() < d:
                temp = t
                d = t.distance()
        return temp

    def judge(self):
        # distance0 = self.path.distance()
        # a, b = self.move()
        # self.path.exchange(a, b)
        # distance1 = self.path.distance()

        temp = self.neighbor()
        if self.isSelected(self.probability(self.path.distance(), temp.distance())):
            self.path = temp
        if self.best > temp.distance():
            self.best = temp.distance()

        # if not self.isSelected(self.probability(distance0, distance1)):
        #     self.path.exchange(a, b)

        dT = self.T * self.coolingEnhancer * self.cool
        self.T -= dT
        '''
        plt.clf()
        plt.plot(self.path.path[0], self.path.path[1])
        plt.scatter(self.path.path[0], self.path.path[1])
        '''
        self.times += 1

        if self.times % 5000 == 0:
            print(self.T, self.times, self.path.distance())
            plt.clf()
            plt.plot(self.path.path[0], self.path.path[1])
            plt.scatter(self.path.path[0],
                        self.path.path[1])
            plt.show()

        '''
        if self.times % 10000 == 0:
            plt.clf()
            plt.plot(self.path.path[0], self.path.path[1])
            plt.scatter(self.path.path[0] + self.path.path[0][self.path.size() - 1: self.path.size()],
                        self.path.path[1] + self.path.path[1][self.path.size() - 1: self.path.size()])
            plt.show()
        '''

    def probability(self, distance0, distance1):
        E = distance1 - distance0
        if E <= 0:
            return 1

        else:
            E2 = self.best - distance1
            e1 = (- E) / self.T
            e2 = (-E2) / self.T
            return math.exp(e1-e2)

    def isSelected(self, p):
        # print(p)
        R = random.random()
        if R < p:
            return True
        else:
            return False

    '''
    def select(self, nb):
        temp = nb[0]
        for path in nb:
            if path.distance() < temp.distance():
                temp = path
        return temp
    '''
