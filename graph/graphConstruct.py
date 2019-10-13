from linkedList.singleLL import LinkedList
import math


class GraphConstruct:
    def getAdjacencyList(self, edges):
        adjDic = {}
        for edge in edges:
            ll = adjDic.get(edge[0])
            if ll:
                ll.insert(edge[1])
            else:
                ll = LinkedList()
                adjDic[edge[0]] = ll
                ll.insert(edge[1])
        adjList = [None for i in range(max(adjDic.keys())+1)]
        for i in adjDic.keys():
            adjList[i] = adjDic[i]
        return adjList

    def getAdjacency(self, rows, columns,type):
        if rows and columns:
            val = 0
            if type == 'color':
                val = 'white'
            if type == 'predecessor':
                val = None
            return [[val for j in range(columns)] for i in range(rows)]
        else:
            print('rows and colums not valid')
