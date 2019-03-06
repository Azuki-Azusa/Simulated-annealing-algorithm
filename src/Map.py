import math

class Map:
    def __init__(self):
        self.path = [[], []]


    def add(self, x, y):
        self.path[0].append(x)
        self.path[1].append(y)

    def size(self):
        return len(self.path[0])

    def NBHDdistance(self, i, j):
        a = self.path[0][i] - self.path[0][j]
        b = self.path[1][i] - self.path[1][j]
        return math.sqrt(a ** 2 + b ** 2)

    def distance(self):
        distance = 0
        for i in range(self.size() - 1):
            distance += self.NBHDdistance(i, i + 1)
        distance += self.NBHDdistance(0, self.size() - 1)
        return distance

    def exchange(self, a, b):
        self.path[0][a], self.path[0][b] = self.path[0][b], self.path[0][a]
        self.path[1][a], self.path[1][b] = self.path[1][b], self.path[1][a]
