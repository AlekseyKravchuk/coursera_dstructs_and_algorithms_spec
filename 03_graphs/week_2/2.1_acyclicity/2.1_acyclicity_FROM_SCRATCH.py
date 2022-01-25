from collections import defaultdict
from copy import deepcopy


class Graph:
    def __init__(self, n):
        self.vertices = defaultdict(set, {key: set() for key in range(1, n + 1)})

        self.not_visited = set(self.vertices.keys())
        self.visited = set()
        self.processed = set()

    def add_edge(self, src, dest):
        self.vertices[src].add(dest)

    def print_graph(self):
        for vertex, neighbors in self.vertices.items():
            print('{}: {}'.format(vertex, *neighbors))

    def mark_as_visited(self, current):
        self.not_visited.remove(current)
        self.visited.add(current)

    def mark_as_processed(self, current):
        self.visited.remove(current)
        self.processed.add(current)

    # modified dfs to check acyclicity in graph
    def dfs_m(self, current):
        if current in self.visited:  # that is given graph has a cycle
            return 1
        if current in self.processed:  # that is current vertex has been processed previously
            return 0

        self.mark_as_visited(current)

        for neighbor in self.vertices[current]:
            if self.dfs_m(neighbor):
                return 1

        self.mark_as_processed(current)
        return 0

    def has_cycle(self):
        # handle each of the connected component of the given graph
        while self.not_visited:
            current = next(iter(self.not_visited))
            if self.dfs_m(current):
                return 1
        # if no connected component of the given graph contains a cycle return 0
        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))
    # G.print_graph()

    print(G.has_cycle())
