from collections import deque
from math import inf
from math import isinf
from collections import namedtuple

Neighbor = namedtuple('Neighbor', ['id', 'weight'])


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = set()  # each element in neighbors has 'int' type

        self.dist = inf  # distance from source vertex to the current one
        self.predecessor_id = None

    def __str__(self):
        return f'{self.id}(dist = {self.dist}; predecessor = {self.predecessor_id})'

    def add_neighbor(self, vertex_id, weight):
        if vertex_id not in self.neighbors:
            self.neighbors.add(Neighbor(vertex_id, weight))


class DirectedWeightedGraph:
    def __init__(self, n):
        self.G = {key: Vertex(key) for key in range(1, n+1)}
        self.mapping = {}

    def add_weighted_edge(self, src_id, dst_id, weight):
        self.G[src_id].add_neighbor(dst_id, weight)
        self.mapping[(src_id, dst_id)] = weight

    def print_graph(self):
        for key, vertex in self.G.items():
            print(f'{key}: {vertex.neighbors}')

    def dijkstra(self, src_id: int):  # src_id: id of source vertex, that is the vertex we start traversal from
        self.G[src_id].dist = 0
        q = deque([src_id])

        while q:
            vertex_id = q.popleft()

            for neighbor in self.G[vertex_id].neighbors:
                if self.G[vertex_id].dist + neighbor.weight < self.G[neighbor.id].dist:
                    q.append(neighbor.id)
                    self.G[neighbor.id].dist = self.G[vertex_id].dist + neighbor.weight
                    self.G[neighbor.id].predecessor_id = vertex_id

    def get_shortest_path(self, src_id: int, dst_id: int):
        self.dijkstra(src_id)
        return -1 if isinf(self.G[dst_id].dist) else self.G[dst_id].dist


if __name__ == '__main__':
    n, m = map(int, input().split())
    dwg = DirectedWeightedGraph(n)

    for _ in range(m):
        dwg.add_weighted_edge(*map(int, input().split()))

    src, dst = map(int, input().split())

    print(dwg.get_shortest_path(src, dst))
