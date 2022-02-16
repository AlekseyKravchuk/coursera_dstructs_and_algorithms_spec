from sys import maxsize as inf
from collections import namedtuple

Info = namedtuple('Info', ['vertex_id', 'dist'])


class MapBinHeap:
    def __init__(self, n):
        self.heap = [Info(vertex_id, inf) for vertex_id in range(1, n + 1)]
        self.heap_last_idx = n-1
        self.map = {vertex_id: index_in_heap_array for vertex_id, index_in_heap_array in enumerate(range(n), start=1)}

    @staticmethod
    def get_parent(i):
        return (i-1) // 2

    @staticmethod
    def get_left_child(i):
        return 2*i + 1

    @staticmethod
    def get_right_child(i):
        return 2*i + 2

    @staticmethod
    def has_parent(i):
        return (i-1)//2 >= 0

    def has_left_child(self, i):
        return 2*i + 1 <= self.heap_last_idx

    def has_right_child(self, i):
        return 2*i + 2 <= self.heap_last_idx

    def swap(self, i, j):  # p: parent_index, i: index_of_current_node
        self.map[self.heap[i].vertex_id] = j
        self.map[self.heap[j].vertex_id] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def decreasePriority(self, vertex_id, new_dist):
        i = self.map[vertex_id]
        assert new_dist <= self.heap[i].dist
        self.heap[i] = Info(vertex_id, new_dist)
        self.sift_up(i)

    def sift_up(self, i):
        while self.has_parent(i):
            parent = self.get_parent(i)
            if self.heap[i].dist > self.heap[parent].dist:
                self.swap(i, parent)
                i = parent
            else:
                break

    def extractMin(self):
        if self.heap:
            self.swap(0, self.heap_last_idx)
            self.heap_last_idx -= 1
            self.sift_down(0)
            return self.heap[self.heap_last_idx + 1]

    def sift_down(self, i):
        while self.has_left_child(i):
            index_of_min_child = self.get_index_of_min_child(i)

            # self.heap[i] is already a leaf node, so nothing to do
            if index_of_min_child == -1:
                break
            if self.heap[index_of_min_child] < self.heap[i]:
                self.swap(i, index_of_min_child)
                i = index_of_min_child
            else:
                break

    def get_index_of_min_child(self, i):
        if self.has_left_child(i) and self.has_right_child(i):
            left, right = self.get_left_child(i), self.get_right_child(i)
            return self.map[min(self.heap[left:right+1], key=lambda x: x[1]).vertex_id]
        elif self.has_left_child(i) and not self.has_right_child(i):
            return self.get_left_child(i)
        else:
            return -1  # self.heap[i] corresponds to a leaf node


if __name__ == '__main__':
    n = 5
    mb = MapBinHeap(n)
    pass
