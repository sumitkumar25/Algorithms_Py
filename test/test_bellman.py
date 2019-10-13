from graph.path.bellmanFord import BellmanFord


class TestBellman:
    def __init__(self):
        w = {
            "tx": 5,
            "ty": 8,
            "tz": -4,
            "xt": -2,
            "yx": -3,
            "yz": 9,
            "zx": 7,
            "zs": 2,
            "st": 7,
            "sy": 7,
        }
        g = {
            's': ['y', 't'],
            't': ['x', 'y', 'z'],
            'y': ['z', 'x'],
            'z': ['x', 's'],
            'x': 't'
        }
        test = BellmanFord(g, w, [list(e) for e in list(w.keys())])
        isShortestPath = test.shortestPath('s')
        print('isShortestPath defined', isShortestPath)
        print(test.d,test.p)
