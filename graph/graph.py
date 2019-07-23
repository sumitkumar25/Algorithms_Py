from ds_queue.dsqueue import DsQueue


class Graph:
    def __init__(self, adjList):
        self.adjList = adjList
        self.color = ['white' for i in range(len(self.adjList))]
        self.predecessor = [None for i in range(len(self.adjList))]
        self.distance = [0 for i in range(len(self.adjList))]

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
