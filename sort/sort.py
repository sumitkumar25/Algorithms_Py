import math


class Sort:
    def insertionSort(self, arr, asc=True):
        l = len(arr)
        if l > 0:
            for i in range(1, l):
                for j in range(0, i):
                    if asc and a[j] > a[i]:
                        self.swap(a, i, j)
                    elif not asc and a[j] < a[i]:
                        self.swap(a, i, j)
        return

    def bubbleSort(self, arr, asc=True):
        l = len(arr)
        if l > 0:
            for i in range(0, l-1):
                for j in range(i+1, l):
                    if not asc and a[j] > a[i]:
                        self.swap(a, i, j)
                    elif asc and a[j] < a[i]:
                        self.swap(a, i, j)

    def mergeSort(self, arr):
        l = len(arr)
        if l > 1:
            # print(arr)
            m = int(math.floor(l/2))
            a1 = self.mergeSort(arr[0:m])
            a2 = self.mergeSort(arr[m:l])
            print('rs', arr, a1, a2)
            rs = self.merge(a1, a2)
            return rs
        else:
            # print('return ', arr)
            return arr

    def merge(self, a1, a2):
        l1 = len(a1)
        l2 = len(a2)
        res = []
        i = j = 0
        while i < l1 and j < l2:
            if a1[i] < a2[j]:
                res.append(a1[i])
                i = i+1
            elif a1[i] > a2[j]:
                res.append(a2[j])
                j = j+1
            elif a1[i] == a2[j]:
                res.append(a2[j])
                res.append(a1[i])
                i = i+1
                j = j+1
        if i == l1:
            res.extend(a2[j:l2])
        elif j == l2:
            res.extend(a1[i:l1])
        return res

    def swap(self, a, i, j):
        t = a[i]
        a[i] = a[j]
        a[j] = t

