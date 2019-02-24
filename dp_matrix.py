p = [30, 35, 15, 5, 10, 20]


def matrxiChainOrder(p):
    n = len(p)
    cost = {}
    parentesis = {}
    # init base case
    for i in range(n-1):
        cost['{0}-{1}'.format(p[i], p[i+1])] = i;



matrxiChainOrder(p)
