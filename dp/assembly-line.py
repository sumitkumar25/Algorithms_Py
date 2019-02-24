import random


class AssemblyLine:
    def __init__(self, a, t, e, x, n, nLines):
        self.a = a
        self.t = t
        self.e = e
        self.x = x
        self.n = n
        self.nLines = nLines
        self.f0 = [None] * self.n
        self.f1 = [None] * self.n
        self.l0 = [None] * self.n
        self.l1 = [None] * self.n
        self.ff = None
        self.ll = None
        self.fastestWay()
        self.printStation()

    def fastestWay(self):
        self.f0[0] = self.e[0] + self.a[0][0]
        self.f1[0] = self.e[1] + self.a[1][0]
        for i in range(1, self.n):
            sameLineCost0 = self.f0[i - 1] + self.a[0][i]
            switchLineCost0 = self.f1[i - 1] + self.a[0][i] + t[1][i - 1]
            sameLineCost1 = self.f1[i - 1] + self.a[1][i]
            switchLineCost1 = self.f0[i - 1] + self.a[1][i] + t[0][i - 1]
            if sameLineCost0 < switchLineCost0:
                self.f0[i] = sameLineCost0
                self.l0[i] = 0
            else:
                self.f0[i] = switchLineCost0
                self.l0[i] = 1

            if sameLineCost1 < switchLineCost1:
                self.f1[i] = sameLineCost1
                self.l1[i] = 1
            else:
                self.f1[i] = switchLineCost1
                self.l1[i] = 0
        if self.f0[self.n-1] + self.x[0] < self.f1[self.n-1] + self.x[1]:
            self.ff = self.f0[self.n-1] + self.x[0]
            self.ll = 0
        else:
            self.ff = self.f1[self.n-1] + self.x[1]
            self.ll = 1
    
    def printStation(self):
        print('line {0} , station {1}'.format(self.ll,self.n))
        k = self.ll
        for i in range(n-1,0,-1):
            if k == 1:
                print('line {0} , station {1}'.format(self.l1[i], i))
                k = self.l1[i]
            else:
                print('line {0} , station {1}'.format(self.l0[i], i))
                k = self.l0[i]


# time required at each station a[i,j]
# a
# time required at switch station t[i,j]
# t
# entry time
# e
# exit time x[]
# x
# no of stations
# n


n = 6
a = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
t = [[2,3,1,3,4], [2,1,2,2,1]]
e = [2, 4]
x = [3, 2]
lines = 2
test = AssemblyLine(a, t, e, x, n, lines)

