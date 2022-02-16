import heapq
from sys import maxsize


class DWG:
    """
    DWG: Directed Weighted Graph
    pq: priority queue, implemented by using 'heapq' module
    """
    def __init__(self, n):
        inf = maxsize
        self.G = {key: {} for key in range(1, n + 1)}
        self.vertex_info = {vert_id: {'dist': inf,
                                      'predecessors': []
                                      }
                            for vert_id in range(1, n+1)}

    def add_weighted_edge(self, v1: int, v2: int, weight: int):
        self.G[v1][v2] = weight

    def print_graph(self):
        for key, vertex in self.G.items():
            print(f'{key}: {vertex.G}')

    def dijkstra(self, src_id):
        self.pq.decreasePriority(src_id, 0)

        while self.pq:
            src_id = self.pq.pop()
            for dst_id in self.G[src_id]:
                if dst_id in self.pq.left2visit:
                    new_dist = self.pq.dist[src] + self.weights[(src_id, dst_id)]
                    if new_dist < self.pq.dist[dst_id]:
                        self.pq.decreasePriority(dst_id, new_dist)

    def get_shortest_path(self, src_id: int, dst_id: int):
        self.dijkstra(src_id)
        return -1 if isinf(self.pq.dist[dst_id]) else int(self.pq.dist[dst_id])


if __name__ == '__main__':
    n, m = map(int, input().split())
    dwg = DWG(n)

    for _ in range(m):
        dwg.add_weighted_edge(*map(int, input().split()))

    src, dst = map(int, input().split())

    print(dwg.get_shortest_path(src, dst))
