from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, n):
        self.G = defaultdict(set, {key: set() for key in range(1, n + 1)})
        self.topology = deque()

        self.not_visited = set(self.G.keys())
        self.processed = set()

    def add_edge(self, start, end):
        self.G[start].add(end)

    def dfs(self, vertex):
        if vertex in self.processed:
            return

        self.not_visited.remove(vertex)

        for neighbor in self.G[vertex]:
            self.dfs(neighbor)

        self.topology.appendleft(vertex)
        self.processed.add(vertex)
        return

    def generate_topology_ordering(self):
        while self.not_visited:
            tmp = next(iter(self.not_visited))
            self.dfs(tmp)
        return self.topology


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))
    # G.print_graph()

    print(*G.generate_topology_ordering())
