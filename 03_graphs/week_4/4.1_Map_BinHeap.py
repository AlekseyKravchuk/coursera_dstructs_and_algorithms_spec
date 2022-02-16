from sys import maxsize
from collections import namedtuple

Info = namedtuple('Info', ['vertex_id', 'dist'])


class MapBinHeap:
    def __init__(self, n):
        inf = maxsize
        self.heap = [Info(vertex_id, inf) for vertex_id in range(1, n + 1)]
        self.heap_last_idx = n-1
        self.map = {vertex_id: id_in_heap for vertex_id, id_in_heap in enumerate(range(n), start=1)}

    def decreasePriority(self, vertex_id, new_prt):
        i = self.map[vertex_id]
        assert new_prt <= self.heap[i].dist
        self.heap[i] = Info(vertex_id, new_prt)
        self.sift_up(i)

    def sift_up(self, i):
        while True:
            if i == 0:
                return
            p = (i - 1) / 2  # p: parent index
            if self.heap[p].dist < self.heap[i].dist:
                self.swap(p, i)
                i = p

    def extractMin(self):
        if not self.heap:
            return

        tmp = self.heap[0]
        self.heap[0] = self.heap[self.heap_last_idx]
        self.heap_last_idx -= 1
        self.sift_down(0)

    def sift_down(self, i):
        left = 2*i+1 if 2*i+1 <= self.heap_last_idx else None
        right = 2*i+2 if 2*i+2 <= self.heap_last_idx else None
        while left is not None:
            if left is not None and right is not None:
                child_idx = self.map[min(self.heap[2 * i + 1:2 * i + 3], key=lambda x: x[1]).vertex_id]
                self.swap(i, child_idx)
                continue
            elif right is not None and right is None:
                self.swap(i, left)
            else:
                return

    def swap(self, p, i):  # p: parent_index, i: index_of_current_node
        self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
        self.map[self.heap[p].vertex_id] = p
        self.map[self.heap[i].vertex_id] = i


if __name__ == '__main__':
    n = 5
    mb = MapBinHeap(n)
    pass
