from collections import defaultdict
from copy import deepcopy


class Graph:
    def __init__(self, n: int):
        self.vertices = defaultdict(set, {k: set() for k in range(1, n + 1)})
        self.visited = set()
        self.left2process = deepcopy(set(self.vertices.keys()))

    def add_edge(self, start: int, end: int):
        self.vertices[start].add(end)
        self.vertices[end].add(start)

    def print_graph(self):
        for vertex, neighbors in self.vertices.items():
            print('{}: {}'.format(vertex, ', '.join(map(str, neighbors))))

    # modified DFS (Depth-First Search) to count connected components in given graph
    def dfs_m(self, start):
        self.visited.add(start)
        self.left2process.remove(start)

        for neighbor in self.vertices[start]:
            if neighbor not in self.visited:
                self.dfs_m(neighbor)

    def count_connected_components(self, num=0):
        while True:
            if self.left2process:
                start_from = self.left2process.pop()
                self.left2process.add(start_from)

                self.dfs_m(start_from)
                num += 1
            else:
                return num


if __name__ == '__main__':
    n, m = map(int, input().split())  # n = |V|; m = |E|
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))

    # G.print_graph()
    num_of_connected_components = G.count_connected_components()
    print(num_of_connected_components)
