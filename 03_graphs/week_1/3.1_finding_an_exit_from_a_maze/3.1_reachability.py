from collections import defaultdict


class Graph:
    def __init__(self, n=0):  # 'n' = |V|
        self.n = n
        self.adj_lst = defaultdict(set)  # self.adj_lst = {vertex_id: set_of_adjacent_vertices}
        self.visited = set()

    # add edge with vertices 'v1' and 'v2'
    def add_edge(self, v1, v2):
        self.adj_lst[v1].add(v2)
        self.adj_lst[v2].add(v1)

    def print_graph(self):
        for vertex in self.adj_lst.keys():
            print('{}: {}'.format(vertex, self.adj_lst[vertex]))

    def has_path(self, start, end):
        if start == end:
            return 1

        # before traversing all the neighbors we need mark current vertex as 'visited'
        self.visited.add(start)

        for neighbor in self.adj_lst[start]:
            if neighbor not in self.visited:
                if self.has_path(neighbor, end):
                    return 1

        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        g.add_edge(v1, v2)
    start, end = map(int, input().split())

    g.print_graph()
    res = g.has_path(start, end)
    print(res)


