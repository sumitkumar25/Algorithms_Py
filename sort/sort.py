import math


class Sort:
    def insertionSort(self, a, asc=True):
        l = len(a)
        if l > 0:
            for i in range(1, l):
                for j in range(0, i):
                    if asc and a[j] > a[i]:
                        self.swap(a, i, j)
                    elif not asc and a[j] < a[i]:
                        self.swap(a, i, j)
        return

    def bubbleSort(self, a, asc=True):
        l = len(a)
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

    def quick(self, a, i, j):
        if i < j:
            q = self.partition(a, i, j)
            self.quick(a, i, q-1)
            self.quick(a, q+1, j)

    def swap(self, a, i, j):
        t = a[i]
        a[i] = a[j]
        a[j] = t

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

    def partition(self, a, i, j):
        item = a[j]
        q = i-1
        for k in range(i, j):
            if a[k] <= item:
                q = q+1
                self.swap(a, q, k)
        self.swap(a, q+1, j)
        return q+1


a = [21, 5, 1, 15, 2, 667, 3, 22, 77]
test = Sort()
test.quick(a, 0, len(a)-1)
print(a)
