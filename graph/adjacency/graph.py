from graph.graphConstruct import GraphConstruct
from ds_queue.dsqueue import DsQueue


class Graph:
    def __init__(self):
        self.construct = GraphConstruct()
        self.color = {}
        self.predecessor = {}
        self.distance = {}
        self.startTime = {}
        self.endTime = {}
        self.time = 0

    def setGraphMatrix(self, rows, columns, edges, isWeighted=False, directed=False):
        self.adjMat = self.construct.getAdjacency(rows, columns, None)

        # 1 at index [i,j] edge represented edge i --> j
        #  for weighted graph use object instead on 1,0
        for E in edges:
            self.adjMat[int(list(E)[0])][int(list(E)[1])] = 1
            if directed:
                self.adjMat[int(list(E)[1])][int(list(E)[0])] = 1

    def dfs_matrix(self, s=0):
        if self.adjMat:
            self.setTraversalAttrs()
            print('\n DFS of adj Matrix \n')
            q = DsQueue()
            q.enqueue(s)
            # self.color[s] = 'grey'
            # self.distance[s] = 0
            # self.startTime[s] = 0
            while not q.isEmpty():
                curr = q.dequeue()
                if self.color[curr] == 'white':
                    self.time += 1
                    self.startTime[curr] = self.time
                    self.color[curr] = 'grey'
                    print('greyed ', curr)
                    for i in range(len(self.adjMat[curr])):
                        if self.adjMat[curr][i]:
                            self.predecessor[i] = curr
                            self.distance[i] = self.distance[curr]+1
                            q.enqueue(i)
                self.color[curr] = 'black'
                self.time += 1
                self.endTime[curr] = self.time

    #  helpers
    #  not optimised for nodes

    def setTraversalAttrs(self):
        if self.adjMat:
            for i in range(len(self.adjMat)):
                self.color[i] = 'white'
                self.predecessor[i] = None
                self.distance[i] = 0
                self.startTime[i] = 0
                self.endTime[i] = 0

    def printGrapt_adjMat(self):
        for i in range(len(self.adjMat)):
            print(*self.adjMat[i])

    def printEdgesFromVertx_adjMat(self, s):
        for j in range(len(self.adjMat[s])):
            if self.adjMat[s][j]:
                print(s, '--->', j)
