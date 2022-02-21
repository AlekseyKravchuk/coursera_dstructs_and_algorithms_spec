import sys
import os
"""
https://github.com/SSQ/Coursera-Stanford-Graph-Search-Shortest-Paths-and-Data-Structures/blob/master/Programming%20Assignment%20%202/dijkstraData.py
"""


def dijkstra():
    dist = []
    V = [*graph.keys()]
    X = [1]  # vertices processed so far; all of the nodes we've already processed
    visited = {1: 0}  # computed shortest path distance
    data_v = []
    neighbors_lst = []

    while X != V:
        for v in X:
            for nbr_id in graph[v].keys():
                if nbr_id not in visited:
                    data_v.append(v)
                    neighbors_lst.append(nbr_id)
                    dist.append(visited[v] + graph[v][nbr_id])
        idx_of_nbr_with_min_dist = dist.index(min(dist))
        nbr_with_min_dist = neighbors_lst[idx_of_nbr_with_min_dist]
        X.append(nbr_with_min_dist)
        visited[nbr_with_min_dist] = min(dist)
        X.sort()
        dist = []
        data_v = []
        neighbors_lst = []
    tmp = []
    for keys in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        tmp.append(visited[keys])
    print(tmp)


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






