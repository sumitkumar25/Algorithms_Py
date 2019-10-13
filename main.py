from graph.graphConstruct import GraphConstruct
from graph.graph import Graph
from graph.questions import GraphQuestion
from sort.sort import Sort
from heap.heap import Ds_Heap
from trees.bst import BinarySearchTree
from test.test_bellman import TestBellman
from test.test_graphs import GraphTest
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

    def testBst(self):
        test = BinarySearchTree()
        for i in [47, 2, 40, 20, 38, 30, 14, 28, 10, 16, 19, 44, 39, 27, 7, 9, 31, 12, 43, 21, 5, 41, 34, 49, 13, 33, 3, 4, 25, 22, 29, 15, 32, 35, 6, 24, 23, 26, 1, 11, 42, 36, 37, 17, 18, 8, 45, 48, 50, 46]:
            #
            # for i in [4, 2, 10, 3, 1, 6,7, 5,18,19]:
            test.insert(test.root, i)
        test.verticalOrderTraversal(test.root, 0)

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
        elif identifier == 'bst':
            self.testBst()
        elif identifier == 'path':
            pathalgo = input('bellman?')
            if pathalgo == 'bellman':
                d = TestBellman()
        d = None


if __name__ == "__main__":
    inputMsg = """
    Please input data structure choice
    1.bst
    """
    # dataStructure = input(inputMsg)
    # if dataStructure:
    #     execute = Executer()
    #     execute.executeOption(dataStructure)
    test = GraphTest()
