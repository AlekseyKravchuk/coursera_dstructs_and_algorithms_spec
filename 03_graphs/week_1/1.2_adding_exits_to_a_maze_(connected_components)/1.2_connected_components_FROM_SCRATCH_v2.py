from collections import defaultdict
from copy import deepcopy


class Graph:
    def __init__(self, n):
        self.G = {key: set() for key in range(1, n + 1)}
        self.left2process = deepcopy(set(self.G.keys()))

    def add_edge(self, v1, v2):
        self.G[v1].add(v2)
        self.G[v2].add(v1)

    def print_graph(self):
        for vertex, neighbors in self.G.items():
            print('{}: {}'.format(vertex, *neighbors))

    def dfs(self, current):
        self.left2process.remove(current)

        for neighbor in self.G[current]:
            if neighbor in self.left2process:
                self.dfs(neighbor)

    def count_connected_components(self):
        num = 0

        while self.left2process:
            current = next(iter(self.left2process))
            self.dfs(current)
            num += 1

        return num


if __name__ == '__main__':
    n, m = map(int, input().split())  # n = |V|; m = |E|
    graph = Graph(n)

    for _ in range(m):
        graph.add_edge(*map(int, input().split()))

    # G.print_graph()
    num_of_connected_components = graph.count_connected_components()
    print(num_of_connected_components)
