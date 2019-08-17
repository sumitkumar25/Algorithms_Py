from common.util import Util
import math


class Ds_Heap:
    def __init__(self):
        self.heap_size = 0
        self.heap = []

    def max_heapify(self, i):
        # arr check, heapsizecheck
        if len(self.heap) and i < self.heap_size:
            largest = i
            left = 2*i+1
            right = 2*i+2
            if left < self.heap_size and self.heap[largest] < self.heap[left]:
                largest = left
            if right < self.heap_size and self.heap[largest] < self.heap[right]:
                largest = right
            if largest != i:
                Util.swap(self.heap, i, largest)
                self.max_heapify(largest)

    def build_max_heap(self, arr):
        if arr == None and len(arr) == 0:
            print("Input error")
        else:
            self.heap = arr
            self.heap_size = len(arr)
            n = math.floor(len(arr)/2)
            for i in range(n-1, -1, -1):
                print('index', i)
                self.max_heapify(i)

    def heapSort(self, arr):
        if arr == None and len(arr) == 0:
            print("Input error")
        else:
            self.heap = arr
            self.heap_size = len(arr)
            self.build_max_heap(arr)
            while(self.heap_size > 0):
                self.max_heapify(0)
                Util.swap(arr, 0, self.heap_size-1)
                self.heap_size = self.heap_size - 1
