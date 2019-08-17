# There are two types of professional wrestlers: "babyfaces" ("good guys") and "heels" ("bad guys").
# Between any pair of professional wrestlers, there may or may not be a rivalry.
# Suppose we have nn professional wrestlers and we have a list of rr pairs of wrestlers for which there are rivalries.
# Give an O(n + r)O(n+r)-time algorithm that determines whether it is possible to designate some of the wrestlers as
#  babyfaces and the remainder as heels such that each rivalry is between a babyface and a heel. If it is possible to perform such a designation,
#  your algorithm should produce it.

from graph.graphConstruct import GraphConstruct


class GraphQuestion:
    proWrestlers = 10
    rivalries = [
        (1, 2),
        (2, 3),
        (1, 4),
        (4, 9),
        (0, 5),
        (7, 0),
        (8, 6)
    ]

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def rivalryGraph(self):
        return GraphConstruct().getAdjacencyList(self.rivalries)
