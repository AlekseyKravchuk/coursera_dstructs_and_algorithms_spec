from math import inf
from math import isinf

import heapq


class DirectedWeightedGraph:
    def __init__(self, n):
        self.neighbors = {key: set() for key in range(1, n+1)}
        self.weights = {}
        self.PQ = None

    def add_weighted_edge(self, src: int, dst: int, weight: int):
        self.neighbors[src].add_neighbor(dst, weight)
        self.weights[(src, dst)] = weight

    def print_graph(self):
        for key, vertex in self.neighbors.items():
            print(f'{key}: {vertex.G}')

    def dijkstra(self, src):
        self.PQ = [[vertex_id, 0] if vertex_id == src else [vertex_id, inf] for vertex_id in range(1, n+1)]
        heapq.heapify(self.PQ)

        while self.PQ:
            vertex_id = q.popleft()

            for neighbor in self.neighbors[vertex_id].G:
                if self.neighbors[vertex_id].dist + neighbor.weight < self.neighbors[neighbor.id].dist:
                    q.append(neighbor.id)
                    self.neighbors[neighbor.id].dist = self.neighbors[vertex_id].dist + neighbor.weight
                    self.neighbors[neighbor.id].predecessor_id = vertex_id

    def get_shortest_path(self, src_id: int, dst_id: int):
        self.dijkstra(src_id)
        return -1 if isinf(self.neighbors[dst_id].dist) else self.neighbors[dst_id].dist


if __name__ == '__main__':
    n, m = map(int, input().split())
    dwg = DirectedWeightedGraph(n)

    for _ in range(m):
        dwg.add_weighted_edge(*map(int, input().split()))

    src, dst = map(int, input().split())

    print(dwg.get_shortest_path(src, dst))
