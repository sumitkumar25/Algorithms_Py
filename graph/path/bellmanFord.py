"""
g, adjacency list graph
d, shortest path from source
p, predecessor
w, edge weights
"""
import sys


class BellmanFord:
    def __init__(self, g, w, e):
        self.g = g
        self.d = {}
        self.p = {}
        self.w = w
        self.e = e

    def relax(self, u, v):
        if self.d[v] > self.d[u]+self.w[u+v]:
            self.d[v] = self.d[u]+self.w[u+v]
            self.p[v] = u

    def initialise(self, s):
        if self.g:
            for v in self.g:
                self.d[v] = sys.maxsize
                self.p[v] = None
            self.d[s] = 0

    def shortestPath(self, s):
        self.initialise(s)
        V = len(list(self.g.keys()))
        for i in range(0, V-1):
            for edge in self.e:
                self.relax(edge[0], edge[1])
        for edge in self.e:
            u = edge[0]
            v = edge[1]
            if self.d[v] > self.d[u]+self.w[u+v]:
                return False
        return True
