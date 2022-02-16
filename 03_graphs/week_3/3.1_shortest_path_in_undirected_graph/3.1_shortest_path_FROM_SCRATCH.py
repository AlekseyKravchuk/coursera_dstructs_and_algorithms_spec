from collections import deque
import array as arr
from math import inf
from math import isinf


class UndirectedGraph:
    def __init__(self, n):
        self.dist = arr.array('f', [inf for _ in range(n+1)])
        self.G = {vertex_id: set() for vertex_id in range(1, n+1)}

    def add_edge(self, src_id, dst_id):
        self.G[src_id].add(dst_id)
        self.G[dst_id].add(src_id)

    def print_graph(self):
        for key, vertex in self.G.items():
            print(f'{key}: {vertex.G}')

    def bfs(self, src_id: int):  # src_id: id of source vertex passed to bfs, that is the vertex start traversal from
        self.dist[src_id] = 0
        q = deque([src_id])

        while q:
            vertex_id = q.popleft()
            for neighbor_id in self.G[vertex_id]:
                if isinf(self.dist[neighbor_id]):
                    self.dist[neighbor_id] = self.dist[vertex_id] + 1
                    q.append(neighbor_id)

    def get_shortest_path(self, src: int, dst: int):
        self.bfs(src)
        return -1 if isinf(self.dist[dst]) else int(self.dist[dst])


if __name__ == '__main__':
    n, m = map(int, input().split())
    ugraph = UndirectedGraph(n)

    for _ in range(m):
        ugraph.add_edge(*map(int, input().split()))
    src, dst = map(int, input().split())

    print(ugraph.get_shortest_path(src, dst))
