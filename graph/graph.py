from ds_queue.dsqueue import DsQueue
from linkedList.singleLLNode import Node


class Graph:
    def __init__(self, adjList):
        self.adjList = adjList
        self.color = ['white' for i in range(len(self.adjList))]
        self.predecessor = [None for i in range(len(self.adjList))]
        self.distance = [0 for i in range(len(self.adjList))]
        self.dfsStarttime = [0 for i in range(len(self.adjList))]
        self.dfsEndtime = [0 for i in range(len(self.adjList))]
        self.time = 0

    def bfs(self, vertex):
        if not self.adjList:
            print('No Adj list representing Graph found')
        else:
            self.color[vertex] = 'grey'
            self.distance[vertex] = 0
            aux_queue = DsQueue()
            aux_queue.enqueue(vertex)
            while not aux_queue.isEmpty():
                u = aux_queue.dequeue()
                print('deque vertex ', u)
                current = None
                if self.adjList[u]:
                    current = self.adjList[u].head
                while current:
                    if self.color[current.data] == 'white':
                        self.color[current.data] = 'grey'
                        self.distance[current.data] = self.distance[u]+1
                        self.predecessor[current.data] = u
                        aux_queue.enqueue(current.data)
                    current = current.next
                self.color[u] = 'black'

    def dfs(self):
        if not self.adjList:
            print('No Adj list representing Graph found')
            return
        for i in range(len(self.adjList)):
            if i >= 0 and self.adjList[i]:
                u = i  # set the current forest vertex
                if self.color[u] == 'white':
                    self.dfs_visit(u)
        print(self.dfsStarttime, self.dfsEndtime)

    def dfs_visit(self, v):
        self.color[v] = 'grey'
        print('greyd', v)
        self.time = self.time + 1
        self.dfsStarttime[v] = self.time
        ll = self.adjList[v]
        if(ll):
            curr = self.adjList[v].head
            while curr:
                if(self.color[curr.data] == 'white'):
                    self.predecessor[curr.data] = v
                    self.dfs_visit(curr.data)
                curr = curr.next
        self.color[v] = 'black'
        self.time = self.time+1
        self.dfsEndtime[v] = self.time

    def def_iterative(self):
        if not self.adjList:
            print('No Adj list representing Graph found')
            return
        for i in range(len(self.adjList)):
            if i >= 0 and self.adjList[i]:
                u = i  # set the current forest vertex
                if self.color[u] == 'white':
                    self.dfs_visit_iterative(u)
        print(self.dfsStarttime, self.dfsEndtime)

    def dfs_visit_iterative(self, _v):
        s = [_v]
        while len(s):
            v = s.pop()
            if self.color[v] == 'white':
                self.time = self.time + 1
                self.color[v] = 'grey'
                print('greyd', v)
                self.dfsStarttime[v] = self.time
                s.append(v)
                ll = self.adjList[v]
                tempStack = []
                if ll:
                    curr = self.adjList[v].head
                    while curr:
                        if self.color[curr.data] == 'white':
                            tempStack.append(curr.data)
                        curr = curr.next
                    tempStack.reverse()
                    s.extend(tempStack)
            elif self.color[v] == 'grey':
                self.time = self.time + 1
                self.color[v] = 'black'
                self.dfsEndtime[v] = self.time
