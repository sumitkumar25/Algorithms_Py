import math


class Sort:
    def insertionSort_While(self, a):
        for i in range(1, len(a)):
            curr = a[i]
            j = i-1
            while j >= 0 and a[j] > curr:
                a[j+1] = a[j]
                j = j-1
            a[j+1] = curr

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

    def mergeSort2(self, arr, start, end, call):
        if start < end:
            m = math.floor((start + end) / 2)
            print('mergeSort2', start, m, end, call)
            self.mergeSort2(arr, start, m, 'first')
            self.mergeSort2(arr, m+1, end, 'second')
            self.merge2(arr, start, m, end)

    def merge2(self, arr, start, m, end):
        l1 = m-start + 1
        l2 = end - m
        a1 = [None]*l1
        a2 = [None]*l2
        for i in range(l1):
            a1[i] = arr[start+i]
        for j in range(l2):
            a2[j] = arr[m+1+j]
        #  merge the arrays into arr
        i = 0
        j = 0
        k = start
        while i < l1 and j < l2:
            if a1[i] <= a2[j]:
                arr[k] = a1[i]
                i = i+1
            else:
                arr[k] = a2[j]
                j = j+1
            k = k+1
        # copy remaining
        while i < l1:
            arr[k] = a1[i]
            i = i+1
            k = k+1
        while j < l2:
            arr[k] = a2[j]
            j = j+1
            k = k+1

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
