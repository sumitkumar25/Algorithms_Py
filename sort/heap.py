import heapq
import math


class Heap:
    def __init__(self):
        pass

    def max_heapify(self, arr, index):
        heapSize = len(arr)-1
        left = 2 * index
        right = (2 * index)+1
        elem = arr[index]
        largest = index
        if(left < heapSize and arr[left] > elem):
            largest = right
        if(right < heapSize and arr[right] > elem):
            largest = right
        if largest != index:
            self.swap(arr, largest, index)
            self.max_heapify(arr, largest)

    def min_heapify(self, node):
        pass

    def createMaxHeap(self, arr):
        for i in range(int(math.floor(len(arr)/2))):
            print(i)
            self.max_heapify(arr, i)
            print(a)

        pass

    def createMinHeap(self, arr):
        pass

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def mpqGetMaximum(self, S):
        return S[0]

    def mpqExtractMax(self, S, hs):
        if hs < 0:
            print('heap underflow')
            return None
        else:
            max = S[0]
            S[0] = S[hs]
            hs = hs-1
            self.max_heapify(S, 0)


a = [0, 1, 2, 3, 4, 5, 6, 7]
b = [0, 1, 2, 3, 4, 5, 6, 7]
test = Heap()
test.createMaxHeap(a)
print(a)
heapq._heapify_max(b)
print(b)
