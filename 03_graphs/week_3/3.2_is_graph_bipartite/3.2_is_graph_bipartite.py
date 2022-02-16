from collections import deque
from math import inf
from math import isinf
from enum import IntEnum
from random import randrange


class Color(IntEnum):
    RED = 0
    BLUE = 1


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = set()  # each element in neighbors has 'int' type

        self.dist = inf  # distance from source vertex to the current one
        self.predecessor_id = None
        self.color = None

    def __str__(self):
        return f'{self.id}(dist = {self.dist}; predecessor = {self.predecessor_id})'

    def add_neighbor(self, vertex_id):
        if vertex_id not in self.neighbors:
            self.neighbors.add(vertex_id)


class UndirectedGraph:
    def __init__(self, n):
        self.G = {key: Vertex(key) for key in range(1, n+1)}
        self.n = n
        self.left2visit = set(self.G.keys())

    def add_edge(self, src_id, dst_id):
        self.G[src_id].add_neighbor(dst_id)
        self.G[dst_id].add_neighbor(src_id)

    def print_graph(self):
        for key, vertex in self.G.items():
            print(f'{key}: {vertex.G}')

    def bfs(self, src_id):
        if src_id in self.left2visit:
            self.left2visit.remove(src_id)

        self.G[src_id].dist = 0
        self.G[src_id].color = Color.RED
        q = deque([src_id])

        while q:
            vertex_id = q.popleft()

            for neighbor_id in self.G[vertex_id].G:
                if isinf(self.G[neighbor_id].dist):
                    if neighbor_id in self.left2visit:
                        self.left2visit.remove(neighbor_id)

                    self.G[neighbor_id].dist = self.G[vertex_id].dist + 1
                    self.G[neighbor_id].predecessor_id = vertex_id
                    self.G[neighbor_id].color = Color.RED if self.G[vertex_id].color == Color.BLUE else Color.BLUE
                    q.append(neighbor_id)
                elif self.G[neighbor_id].color == self.G[vertex_id].color:
                    return 0  # i.e. given graph is NOT bipartite
        return 1  # i.e. given graph is bipartite

    def is_graph_bipartite(self):
        while self.left2visit:
            src_id = next(iter(self.left2visit))
            if self.bfs(src_id) == 0:
                return 0
        return 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    ugraph = UndirectedGraph(n)

    for _ in range(m):
        ugraph.add_edge(*map(int, input().split()))

    print(ugraph.is_graph_bipartite())

