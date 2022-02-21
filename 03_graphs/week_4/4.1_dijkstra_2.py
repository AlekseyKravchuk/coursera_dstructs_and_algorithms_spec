import sys
import os
"""
https://github.com/SSQ/Coursera-Stanford-Graph-Search-Shortest-Paths-and-Data-Structures/blob/master/Programming%20Assignment%20%202/dijkstraData.py
"""


def dijkstra():
    scores = []
    V = [*graph.keys()]  # all the vertices in graph
    X = [1]  # vertices processed so far; all of the nodes we've already processed (correctly computed shortest path)
    A = {1: 0}  # computed shortest path distances for all vertices from the source vertex with id = 1
    B = [[None] for _ in range(len(V)+1)]
    data_v = []
    neighbors_lst = []

    while X != V:
        for vert_id in X:
            for nbr_id in graph[vert_id].keys():  # iterate over all neighbors of vertex with 'vert_id' id
                if nbr_id not in A:
                    data_v.append(vert_id)
                    neighbors_lst.append(nbr_id)
                    scores.append(A[vert_id] + graph[vert_id][nbr_id])
        idx_of_nbr_with_min_dist = scores.index(min(scores))
        nbr_with_min_dist = neighbors_lst[idx_of_nbr_with_min_dist]
        X.append(nbr_with_min_dist)
        B[nbr_with_min_dist] = B[vert_id] + [nbr_with_min_dist]
        A[nbr_with_min_dist] = min(scores)
        X.sort()
        scores = []
        data_v = []
        neighbors_lst = []

    # tmp = []
    # tmp_pred = []
    for vertex_id in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        print(f'dist({vertex_id}) = {A[vertex_id]}, path = {B[vertex_id]}')
        # tmp.append(A[vertex_id])
        # tmp_pred.append(B[vertex_id])
    # print(tmp)


if __name__ == '__main__':
    fname = '4.1_tests/dijkstraDataStanford.txt'
    fpath = '/'.join([os.path.dirname(os.path.abspath(__file__)), fname])
    graph = {}
    with open(fpath) as f:
        for line in f:
            lst = line.split()  # list of strings, first str in list is vertex_id, others are 'neighbor_id, weight'
            src_id = int(lst[0])
            graph[src_id] = dict([[*map(int, s.split(','))] for s in lst[1:]])
    dijkstra()






