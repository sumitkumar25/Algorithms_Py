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
            for i in range(math.floor(len(arr))+1, -1, -1):
                self.max_heapify(arr, i, l-1)
            print('max heap', arr)
        else:
            print('array of length 0')

    def createMinHeap(self, arr):
        l = len(arr)
        if l:
            for i in range(math.floor(len(arr))+1, -1, -1):
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


a = [21, 5, 1, 15, 2, 667, 3, 22, 77]
test = Heap()
test.heapSortDes(a)
print(a)
