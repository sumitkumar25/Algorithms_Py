import math


class Search:
    # binarySearch if element exists
    def exists(self, arr, n):
        l = len(arr)
        if l == 0:
            return -1
        elif l == 1:
            return arr[0] == n
        else:
            m = int(math.floor(l/2))
            mid = arr[m]
            if mid < n:
                return self.exists(arr[m:l], n)
            elif mid > n:
                return self.exists(arr[0: m], n)
            else:
                return mid == n

    # binarySearch if element exists return index
    def findIndex(self, arr, n, start=0, end=0):
        if(end < start):
            return -1
        else:
            m = start + (end - start)//2
            mid = arr[m]
            if mid == n:
                return m
            elif mid < n:
                return self.findIndex(arr, n, m+1, end)
            elif mid > n:
                return self.findIndex(arr, n, start, m-1)
            else:
                return -1


s = Search()
a = [1, 2, 3, 4, 5, 6, 67, 8, 85]
n = 44444
result = s.findIndex(a, n, 0, len(a)-1)
print(result)
