from graph.graphConstruct import GraphConstruct
from graph.graph import Graph


class Executer:

    def graphTest(self):
        graphConstruct = GraphConstruct()
        adjList = graphConstruct.getAdjacencyList([
            [0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]
        ])
        graph = Graph(adjList)
        graph.bfs(2)

    def executeOption(self, identifier):
        if identifier == 'graph':
            self.graphTest()


if __name__ == "__main__":
    execute = Executer()
    execute.executeOption('graph')
