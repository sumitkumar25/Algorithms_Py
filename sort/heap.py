import math


class Heap:
    def __init__(self):
        pass

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def max_heapify(self, arr, i, heapSize):
        if i < heapSize:
            largest = i
            left = 2*i + 1
            right = 2*i + 2
            if left <= heapSize and arr[left] > arr[largest]:
                largest = left
            if right <= heapSize and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                self.swap(arr, i, largest)
                self.max_heapify(arr, largest, heapSize)

    def min_heapify(self, arr, i, heapSize):
        if i < heapSize:
            min = i
            left = 2*i + 1
            right = 2*i + 2
            if left <= heapSize and arr[left] < arr[min]:
                min = left
            if right <= heapSize and arr[right] < arr[min]:
                min = right
            if min != i:
                self.swap(arr, i, min)
                self.min_heapify(arr, min, heapSize)

    def createMaxHeap(self, arr):
        l = len(arr)
        if l:
            for i in range(int(math.floor(len(arr))+1), -1, -1):
                self.max_heapify(arr, i, l-1)
            print('max heap', arr)
        else:
            print('array of length 0')

    def createMinHeap(self, arr):
        l = len(arr)
        if l:
            for i in range(int(math.floor(len(arr))+1), -1, -1):
                self.min_heapify(arr, i, l-1)
            print('min heap', arr)
        else:
            print('array of length 0')

    def heapSort(self, arr):
        heapSize = len(arr)-1
        self.createMaxHeap(arr)
        while heapSize > 0:
            self.swap(arr, 0, heapSize)
            heapSize = heapSize - 1
            self.max_heapify(arr, 0, heapSize)

    def heapSortDes(self, arr):
        heapSize = len(arr)-1
        self.createMinHeap(arr)
        while heapSize > 0:
            self.swap(arr, 0, heapSize)
            heapSize = heapSize - 1
            self.min_heapify(arr, 0, heapSize)

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
            self.max_heapify(S, 0, hs)
            return max

    def mpqInsert(self, S, item):
        S.append(item)
        self.createMaxHeap(S)

    def mpqIncreaseKey(self, S, i, value):
        l = len(S)
        if i < l:
            if(S[i] > value):
                print('value less than current value .exit')
                return
            S[i] = value
            self.createMaxHeap(S)
        else:
            print('index greater than heapsize')


a = [21, 5, 1, 15, 2, 667, 3, 22, 77]
test = Heap()
test.createMaxHeap(a)
test.mpqInsert(a,1000)
print(a)
