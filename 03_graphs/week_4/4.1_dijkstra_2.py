"""
https://github.com/SSQ/Coursera-Stanford-Graph-Search-Shortest-Paths-and-Data-Structures/blob/master/Programming%20Assignment%20%202/dijkstraData.py
"""

src_file_name = '/home/kav/PycharmProjects/coursera_dstructs_and_algorithms_spec/03_graphs/week_4/4.1_tests/dijkstraDataStanford.txt'
dict_nested = {}
with open(src_file_name) as f:
    for line in f:
        lst = line.split()  # list of strings, first str in list is vertex_id, others are 'neighbor_id, weight'
        src_id = int(lst[0])
        dict_nested[src_id] = dict([[*map(int, s.split(','))] for s in lst[1:]])


def dijkstra():
    scores = []
    # print node_list
    V = [*dict_nested.keys()]
    X = [1]
    A = {1: 0}
    data_v = []
    data_w = []

    while X != V:
        for v in X:
            for w in dict_nested[v].keys():
                if w not in A:
                    data_v.append(v)
                    data_w.append(w)
                    scores.append(A[v] + dict_nested[v][w])

        find_w = data_w[scores.index(min(scores))]
        X.append(find_w)
        A[find_w] = min(scores)
        X.sort()
        scores = []
        data_v = []
        data_w = []
        # print A
    tmp = []
    for keys in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        tmp.append(A[keys])
    print(tmp)


dijkstra()
