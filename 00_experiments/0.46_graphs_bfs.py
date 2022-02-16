from enum import Enum
from collections import deque
from math import inf


class State(Enum):
    NOT_VISITED = 0
    VISITED = 1


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = set()  # each element in neighbors has 'int' type

        self.state = State.NOT_VISITED
        self.dist = inf  # distance from source vertex by default
        self.predecessor_id = None

    def __str__(self):
        return f'{self.id}(dist = {self.dist}/ predecessor = {self.predecessor_id})'

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
        self.G[src_id].state = State.VISITED
        self.G[src_id].dist = 0
        q = deque([src_id])
        # bfs_traversal_result = []

        while q:
            vertex_id = q.popleft()
            # bfs_traversal_result.append(self.G[vertex_id])
            print(self.G[vertex_id])

            for neighbor_id in self.G[vertex_id].G:
                if self.G[neighbor_id].state == State.NOT_VISITED:
                    self.G[neighbor_id].state = State.VISITED
                    self.G[neighbor_id].dist = self.G[vertex_id].dist + 1
                    self.G[neighbor_id].predecessor_id = vertex_id
                    q.append(neighbor_id)
        # return bfs_traversal_result


if __name__ == '__main__':
    n, m = map(int, input().split())
    undirected_graph = UndirectedGraph(n)

    for _ in range(m):
        undirected_graph.add_edge(*map(int, input().split()))
    undirected_graph.bfs(1)
