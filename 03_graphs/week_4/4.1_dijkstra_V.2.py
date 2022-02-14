from collections import namedtuple
from math import inf
from math import isinf
import heapq
import array

Info = namedtuple('Info', ['idx', 'dist_from_src'])


class PQ:
    """
    Among basic features of heapq PQ supports checking if the given element is IN heap by O(1)
    """

    def __init__(self, n):
        self.left2visit = set([i for i in range(1, n + 1)])
        self.heap = [(inf, Info(vertex_id, inf)) for vertex_id in range(1, n + 1)]
        self.dist = array.array('f', [inf for _ in range(n+1)])

    def decreasePriority(self, vertex_id, new_prt):
        if vertex_id in self.left2visit:
            self.dist[vertex_id] = new_prt
            # TODO
            # fix buggy removal from heap by index (that is not ordinary array)
            self.heap[vertex_id-1] = (new_prt, Info(vertex_id, new_prt))
            heapq.heapify(self.heap)

    def pop(self):
        """
        Extracts element from heap with minimum priority.
        Element format: (priotiry, (vertex_id, priority))
        :return: int  # index of the vertex removed from priority queue
        """
        if self:
            idx2remove = heapq.heappop(self.heap)[1].idx
            self.left2visit.remove(idx2remove)
            return idx2remove


class DirectedWeightedGraph:
    def __init__(self, n):
        self.neighbors = {key: set() for key in range(1, n+1)}
        self.weights = {}
        self.pq = PQ(n)

    def add_weighted_edge(self, v1: int, v2: int, weight: int):
        self.neighbors[v1].add(v2)
        self.weights[(v1, v2)] = weight  # dictionary {edge (v1, v2): weight for the given edge}

    def print_graph(self):
        for key, vertex in self.neighbors.items():
            print(f'{key}: {vertex.neighbors}')

    def dijkstra(self, src_id):
        self.pq.decreasePriority(src_id, 0)

        while self.pq:
            src_id = self.pq.pop()
            for dst_id in self.neighbors[src_id]:
                if dst_id in self.pq.left2visit:
                    new_dist = self.pq.dist[src] + self.weights[(src_id, dst_id)]
                    if new_dist < self.pq.dist[dst_id]:
                        self.pq.decreasePriority(dst_id, new_dist)

    def get_shortest_path(self, src_id: int, dst_id: int):
        self.dijkstra(src_id)
        return -1 if isinf(self.pq.dist[dst_id]) else int(self.pq.dist[dst_id])


if __name__ == '__main__':
    n, m = map(int, input().split())
    dwg = DirectedWeightedGraph(n)

    for _ in range(m):
        dwg.add_weighted_edge(*map(int, input().split()))

    src, dst = map(int, input().split())

    print(dwg.get_shortest_path(src, dst))
