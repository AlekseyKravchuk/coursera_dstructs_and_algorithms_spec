from collections import deque
from math import inf
from math import isinf


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = set()  # each element in neighbors has 'int' type

        self.dist = inf  # distance from source vertex to the current one
        self.predecessor_id = None

    def __str__(self):
        return f'{self.id}(dist = {self.dist}; predecessor = {self.predecessor_id})'

    def add_neighbor(self, vertex_id):
        if vertex_id not in self.neighbors:
            self.neighbors.add(vertex_id)


class UndirectedGraph:
    def __init__(self, n):
        self.G = {key: Vertex(key) for key in range(1, n+1)}

    def add_edge(self, src_id, dst_id):
        self.G[src_id].add_neighbor(dst_id)
        self.G[dst_id].add_neighbor(src_id)

    def print_graph(self):
        for key, vertex in self.G.items():
            print(f'{key}: {vertex.G}')

    def bfs(self, src_id: int):  # src_id: id of source vertex passed to bfs, that is the vertex start traversal from
        self.G[src_id].get_dist = 0
        q = deque([src_id])

        while q:
            vertex_id = q.popleft()

            for neighbor_id in self.G[vertex_id].G:
                if isinf(self.G[neighbor_id].get_dist):
                    self.G[neighbor_id].get_dist = self.G[vertex_id].get_dist + 1
                    self.G[neighbor_id].predecessor_id = vertex_id
                    q.append(neighbor_id)

    def get_shortest_path(self, src: int, dst: int):
        N = 0
        current = src

        while self.G[current].predecessor_id is not None:
            N += 1
            if self.G[current].predecessor_id == dst:
                return N
            current = self.G[current].predecessor_id
        return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    ugraph = UndirectedGraph(n)

    for _ in range(m):
        ugraph.add_edge(*map(int, input().split()))
    src, dst = map(int, input().split())

    ugraph.bfs(dst)
    print(ugraph.get_shortest_path(src, dst))
