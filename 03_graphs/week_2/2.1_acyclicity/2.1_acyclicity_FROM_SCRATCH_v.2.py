from collections import defaultdict
from copy import deepcopy


class Graph:
    def __init__(self, n):
        self.vertices = defaultdict(set, {key: set() for key in range(1, n+1)})

        self.not_visited = deepcopy(set(self.vertices.keys()))
        self.visited = set()
        self.processed = set()

    def add_edge(self, start, end):
        self.vertices[start].add(end)

    def mark_as_visited(self, vertex):
        self.not_visited.remove(vertex)
        self.visited.add()

    def has_cycle(self):
        pass



if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))
    # G.print_graph()

    print(G.has_cycle())
