# from sys import maxsize as inf
from collections import namedtuple
from math import inf
from math import isinf

Info = namedtuple('Info', ['vertex_id', 'dist'])


class DWGraph:
    """
    DWGraph stands for Directed Weighted Graph
    Includes additional data structure: Map + MinHeap, needed to implement Dijkstra's algorithm with priority queue
    'Map + MinHeap' supports following main operations:
        => extractMin:        O(log_n)
        => contains:          O(1)
        => decrease_priority: O(log_n), where priority is meant as minimum distance from source vertex in Graph
    """
    def __init__(self, n):
        # size of Directed Graph, |V|
        self.n = n

        # pq: priority queue implemented as standard min_heap, i.e. as array with special heap indices arithmetic
        # each tuple in min_heap has following format: Info('vertex_id', 'distance_from_source_vertex')
        # initially all distances are set to infinity (sys.maxsize)
        self.pq = [Info(vertex_id, inf) for vertex_id in range(1, n + 1)]
        self.last_idx = n-1

        # map allows to map 'vertex_id' to it's index in 'heap' array
        self.map = {vertex_id: index_in_heap_array for vertex_id, index_in_heap_array in enumerate(range(n), start=1)}

        # Directed Graph as dict: {vertex_id_A: {neighbor_id_C: weight_C, neighbor_id_D: weight_D, ...},
        #                          vertex_id_B: {neighbor_id_F: weight_F, neighbor_id_E: weight_E, ...},
        #                           ...
        #                          vertex_id_K: {neighbor_id_L: weight_L, neighbor_id_M: weight_M, ...}
        #                          }
        self.G = {vertex_id: {} for vertex_id in range(1, n+1)}

    def add_weighted_edge(self, src, dst, weight):
        self.G[src][dst] = weight

    def pq_is_not_empty(self):
        return self.last_idx >= 0

    def print_graph(self):
        for vertex_id, neighbors in self.G.items():
            print(f'{vertex_id}: {neighbors}')

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
        return 2*i + 1 <= self.last_idx

    def has_right_child(self, i):
        return 2*i + 2 <= self.last_idx

    def swap(self, i, j):  # p: parent_index, i: index_of_current_node
        self.map[self.pq[i].vertex_id] = j
        self.map[self.pq[j].vertex_id] = i
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def decreasePriority(self, vertex_id, new_dist):
        i = self.map[vertex_id]
        assert new_dist <= self.pq[i].dist
        self.pq[i] = Info(vertex_id, new_dist)
        self.sift_up(i)

    def sift_up(self, i):
        while self.has_parent(i):
            parent = self.get_parent(i)
            if self.pq[i].dist < self.pq[parent].dist:
                self.swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        while self.has_left_child(i):
            index_of_min_child = self.get_index_of_min_child(i)

            # self.heap[i] is already a leaf node, so nothing to do
            if index_of_min_child == -1:
                break
            if self.pq[index_of_min_child] < self.pq[i]:
                self.swap(i, index_of_min_child)
                i = index_of_min_child
            else:
                break

    def extract_vertex_with_min_dist(self):
        if self.last_idx > 0:
            self.swap(0, self.last_idx)
            self.last_idx -= 1
            self.sift_down(0)
            return self.pq[self.last_idx + 1].vertex_id
        elif self.last_idx == 0:
            self.last_idx -= 1
            return self.pq[0].vertex_id
        else:
            return None  # there are no elements in heap

    def get_index_of_min_child(self, i):
        if self.has_left_child(i) and self.has_right_child(i):
            left, right = self.get_left_child(i), self.get_right_child(i)
            return self.map[min(self.pq[left:right + 1], key=lambda x: x[1]).vertex_id]
        elif self.has_left_child(i) and not self.has_right_child(i):
            return self.get_left_child(i)
        else:
            return -1  # self.heap[i] corresponds to a leaf node

    def pq_contains(self, vertex_id):
        return vertex_id in self.map

    def get_shortest_path_dijkstra(self, src, dst):
        self.decreasePriority(src, 0)

        while self.pq_is_not_empty():
            vertex_id = self.extract_vertex_with_min_dist()
            for nbr_id, weight in self.G[vertex_id].items():
                if self.pq_contains(nbr_id):
                    new_dist = self.pq[self.map[vertex_id]].dist + self.G[vertex_id][nbr_id]
                    if new_dist < self.pq[self.map[nbr_id]].dist:
                        self.decreasePriority(nbr_id, new_dist)
        # return -1 if self.pq[self.map[dst]].dist == inf else self.pq[self.map[dst]].dist
        return -1 if isinf(self.pq[self.map[dst]].dist) else int(self.pq[self.map[dst]].dist)

    def get_shortest_path_dijkstra_lst(self, src, dst_lst):
        self.decreasePriority(src, 0)

        while self.pq_is_not_empty():
            vertex_id = self.extract_vertex_with_min_dist()
            for nbr_id, weight in self.G[vertex_id].items():
                if self.pq_contains(nbr_id):
                    new_dist = self.pq[self.map[vertex_id]].dist + self.G[vertex_id][nbr_id]
                    if new_dist < self.pq[self.map[nbr_id]].dist:
                        self.decreasePriority(nbr_id, new_dist)

        return [-1 if isinf(self.pq[self.map[dst]].dist) else int(self.pq[self.map[dst]].dist) for dst in dst_lst]


if __name__ == '__main__':
    # TODO: построить граф на основе данного файла, выполнить задание Graph Search, Shortest Paths, and Data Structures
    # https://www.coursera.org/learn/algorithms-graphs-data-structures/exam/Ij5au/programming-assignment-2/attempt
    src_file_name = '/home/kav/PycharmProjects/coursera_dstructs_and_algorithms_spec/03_graphs/week_4/4.1_tests/dijkstraDataStanford.txt'
    with open(src_file_name, 'r') as f:
        lines = f.readlines()
        dwg = DWGraph(len(lines))
        for line in lines:  # lines - это список строк
            lst = line.split()
            vertex_id, lst_of_str = int(lst[0]), lst[1:]
            neighbors_as_dict = dict([[*map(int, s.split(','))] for s in lst_of_str])
            dwg.G[vertex_id] = neighbors_as_dict
        src = 1
        dst_lst = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        lst = dwg.get_shortest_path_dijkstra_lst(src, dst_lst)
        for elm in lst:
            print(elm, end=',')

    # n, m = map(int, input().split())
    # dwg = DWGraph(n)
    # for _ in range(m):
    #     dwg.add_weighted_edge(*map(int, input().split()))
    # src, dst = map(int, input().split())
    #
    # print(dwg.get_shortest_path_dijkstra(src, dst))
