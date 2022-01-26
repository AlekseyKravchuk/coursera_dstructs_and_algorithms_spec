from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, n):
        self.G = defaultdict(set, {key: set() for key in range(1, n + 1)})
        self.topology = deque()

        self.left2process = set(self.G.keys())

    def add_edge(self, start, end):
        self.G[start].add(end)

    def dfs(self, vertex):
        if vertex not in self.left2process:
            return

        self.left2process.remove(vertex)

        for neighbor in self.G[vertex]:
            self.dfs(neighbor)

        self.topology.appendleft(vertex)
        return

    def generate_topology_ordering(self):
        while self.left2process:
            tmp = next(iter(self.left2process))
            self.dfs(tmp)
        return self.topology


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))
    # G.print_graph()

    print(*G.generate_topology_ordering())
