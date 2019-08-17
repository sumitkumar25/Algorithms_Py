from graph.graphConstruct import GraphConstruct
from graph.graph import Graph
from graph.questions import GraphQuestion
from sort.sort import Sort
from heap.heap import Ds_Heap
import math


class Executer:

    def graphTest(self):
        graphConstruct = GraphConstruct()
        adjList = graphConstruct.getAdjacencyList([
            [0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]
        ])
        graph = Graph(adjList)
        graph.dfs()

    def graphQuestion(self):
        questions = GraphQuestion()
        rGraph = questions.rivalryGraph()
        for i in range(len(rGraph)):
            if i:
                ll = rGraph[i]
                if(ll):
                    curr = ll.head
                    while(curr):
                        print(i, curr.data)
                        curr = curr.next

    def insertionSort(self):
        test = [23, 2, 1, 4213, 43, 1, 21, 4, 1,
                213, 43, 23423, 53, 21, 221, 342312123]
        sortObj = Sort()
        sortObj.insertionSort_While(test)
        print(test)

    def mergeSort(self):
        test = [23, 2, 1, 4213, 43, 1, 21, 4, 1,
                213, 43, 23423, 53, 21, 221, 342312123]
        sortObj = Sort()
        sortObj.mergeSort2(test, 0, len(test)-1, 'main')
        print(test)

    def testHeap(self):
        test = Ds_Heap()
        arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        test.heapSort(arr)
        print(test.heap)

    def executeOption(self, identifier):
        if identifier == 'graph':
            self.graphTest()
        elif identifier == 'graphQuestion':
            self.graphQuestion()
        elif identifier == 'i-sort':
            self.insertionSort()
        elif identifier == 'm-sort':
            self.mergeSort()
        elif identifier == 'heap':
            self.testHeap()


if __name__ == "__main__":
    execute = Executer()
    execute.executeOption('heap')
