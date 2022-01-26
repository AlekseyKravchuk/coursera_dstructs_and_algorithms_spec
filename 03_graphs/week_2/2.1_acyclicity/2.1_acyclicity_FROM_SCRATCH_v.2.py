from collections import defaultdict
from copy import deepcopy


class Graph:
    def __init__(self, n):
        self.G = defaultdict(set, {key: set() for key in range(1, n + 1)})

        self.not_visited = set(self.G.keys())
        self.visited = set()

    def add_edge(self, start, end):
        self.G[start].add(end)

    def mark_as_visited(self, vertex):
        self.not_visited.remove(vertex)
        self.visited.add(vertex)

    def dfs(self, vertex):
        if vertex in self.visited:  # cycle is found
            return 1
        elif vertex in self.not_visited:
            self.mark_as_visited(vertex)
        else:  # vertex is in processed - implicitly defined set
            return 0

        for neighbor in self.G[vertex]:
            if self.dfs(neighbor):
                return 1

        self.visited.remove(vertex)
        return 0

    def has_cycle(self):
        while self.not_visited:
            if self.dfs(next(iter(self.not_visited))):
                return 1
        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))
    # G.print_graph()

    print(G.has_cycle())
