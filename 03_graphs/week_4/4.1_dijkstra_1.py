"""
https://github.com/SSQ/Coursera-Stanford-Graph-Search-Shortest-Paths-and-Data-Structures/blob/master/Programming%20Assignment%20%202/dijkstraData.py
"""

src_file_name = '/home/kav/PycharmProjects/coursera_dstructs_and_algorithms_spec/03_graphs/week_4/4.1_tests/dijkstraDataStanford.txt'
with open(src_file_name) as f:
    data = []
    list_data = []
    node_list = []
    u = []
    v = []
    data_u = []
    data_v = []
    dict_nested = {}
    list_nested = []
    for line in f:
        if len(line) > 1:
            data = line.split()
            list_data.append(data)

    for i in range(len(list_data)):
        node_list.append(i + 1)
        del list_data[i][0]

        for j in range(len(list_data[i])):
            u, v = list_data[i][j].split(',')
            # print u,v
            # print type(u)
            data_u.append(int(u))
            data_v.append(int(v))
        list_nested.append(dict(zip(data_u, data_v)))
        data_u, data_v = [], []
    dict_nested = dict(zip(node_list, list_nested))
f.close()


def dijkstra():
    scores = []
    # print node_list
    V = node_list
    # print V
    X = [1]
    # print type(X)
    A = {}
    A[1] = 0
    # print A
    data_v = []
    data_w = []

    while X != V:
        for v in X:
            for w in dict_nested[v].keys():
                # print w
                if w not in A:
                    data_v.append(v)
                    data_w.append(w)
                    scores.append(A[v] + dict_nested[v][w])

        # print "scores: "+str(scores)
        # print "data_w: "+str(data_w)
        find_w = 0
        find_w = data_w[scores.index(min(scores))]
        # print "w: "+ str(find_w)
        X.append(find_w)
        # print "X: "+str(X)
        A[find_w] = min(scores)
        # print "A[w],w: " +str(A[find_w])+" "+str(find_w)
        X.sort()
        scores = []
        data_v = []
        data_w = []
        # print A
    tmp = []
    for keys in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        # print A[keys]
        # print type(A[keys])
        tmp.append(A[keys])
    print(tmp)


dijkstra()
