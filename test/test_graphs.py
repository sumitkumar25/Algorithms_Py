from graph.adjacency.graph import Graph


class GraphTest:
    def __init__(self):
        self.G = Graph()
        graphFormat = input(
            "type 'list' for adjacency list or \n 'matrix' for ajacency matrix \n\n")
        if graphFormat == 'list':
            pass
        elif graphFormat == 'matrix':
            self.testGraph_adjMat()
        else:
            print('invalid choice')

    def testGraph_adjMat(self):
        edges = [
            '01', '02', '21', '23', '24', '14', '43', '34', '30'
        ]
        vertices = 5
        self.G.setGraphMatrix(vertices, vertices, edges, False,True)
        self.G.printGrapt_adjMat()
        for v in range(vertices):
            self.G.printEdgesFromVertx_adjMat(v)
            print('edges from ',v,' ends')
