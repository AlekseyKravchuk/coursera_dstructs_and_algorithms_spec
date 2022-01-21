from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.neighbors = defaultdict(set, {k: set() for k in list(range(1, n + 1))})
        self.visited = set()

    def add_edge(self, start: int, end: int):
        self.neighbors[start].add(end)
        self.neighbors[end].add(start)

    def print_graph(self):
        for v, neighbors in self.neighbors.items():
            print('{}: {}'.format(v, ', '.join(map(str, neighbors))))

    def has_path(self, start, end):
        if start == end:
            return 1

        self.visited.add(start)

        for neighbor in self.neighbors[start]:
            if neighbor not in self.visited:
                if self.has_path(neighbor, end):
                    return 1
        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        graph.add_edge(*list(map(int, input().split())))

    start, end = map(int, input().split())

    # graph.print_graph()
    # print(f'start = {start}, end = {end}')

    result = graph.has_path(start, end)
    print(result)



