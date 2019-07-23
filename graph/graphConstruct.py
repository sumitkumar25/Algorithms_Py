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
