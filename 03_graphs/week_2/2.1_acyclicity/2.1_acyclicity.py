from collections import defaultdict
from copy import deepcopy


class Graph:
    def __init__(self, n: int):
        self.vertices = defaultdict(set, {k: set() for k in range(1, n + 1)})

        self.non_visited = deepcopy(set(self.vertices.keys()))  # WHITE set, vertices that aren't visited at all
        self.visited = set()    # GREY set, vertices that are in recursion stack currently
        self.processed = set()  # BLACK set, vertices that already visited and whose all neighbors are visited too

    def add_edge(self, start: int, end: int):
        self.vertices[start].add(end)

    def print_graph(self):
        for vertex, neighbors in self.vertices.items():
            print('{}: {}'.format(vertex, ', '.join(map(str, neighbors))))
    
    def mark_as_visited(self, vertex):
        self.non_visited.remove(vertex)
        self.visited.add(vertex)

    def mark_as_processed(self, vertex):
        self.visited.remove(vertex)
        self.processed.add(vertex)

    def dfs(self, current):
        self.mark_as_visited(current)

        for neighbor in self.vertices[current]:
            if neighbor in self.processed:  # neighbor is already processed, so continue
                continue
            if neighbor in self.visited:    # neighbor is already visited, then cycle is found
                return 1
            if self.dfs(neighbor):
                return 1

        self.mark_as_processed(current)
        return 0

    def has_cycle(self):
        while self.non_visited:
            current = next(iter(self.non_visited))
            if self.dfs(current):
                return 1

        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())  # n = |V|; m = |E|
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))

    # G.print_graph()

    print(G.has_cycle())

