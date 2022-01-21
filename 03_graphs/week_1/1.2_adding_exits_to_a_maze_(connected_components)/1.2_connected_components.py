from collections import defaultdict
from copy import deepcopy


class Graph:
    def __init__(self, n):  # 'n' = |V|
        self.vertices = set(range(1, n+1))  # this class variable is needed to take into account isolated vertices
        self.G = defaultdict(set)  # self.G = {vertex_id: {set_of_adjacent_vertices}}
        self.visited = set()

    # add edge with vertices 'start' and 'end'
    def add_edge(self, start, end):
        self.G[start].add(end)
        self.G[end].add(start)

    def add_isolated_vertex(self, v):
        self.G[v] = set()

    def print_graph(self):
        for vertex in self.G.keys():
            print('{}: {}'.format(vertex, self.G[vertex]))

    def dfs(self, start):
        # before traversing all the neighbors we need mark the current vertex as 'visited'
        self.visited.add(start)

        for neighbor in self.G[start]:
            if neighbor not in self.visited:
                self.dfs(neighbor)

    # modified dfs to answer the question:
    # "Is the vertex 'end' reachable from the 'start' one in the given graph?"
    # or, in other words: "Do vertices 'start' and 'end' belong to the same connected component"
    def has_path(self, start, end):
        # base case
        if start == end:
            return True

        self.visited.add(start)
        for neighbor in self.G[start]:
            if neighbor not in self.visited:
                if self.has_path(neighbor, end):
                    return True
        return False

    def get_num_of_connected_components(self):
        N = 0  # initialize the number of connected components
        search_within = set(deepcopy(self.G))

        while search_within:
            current = next(iter(search_within))

            self.dfs(current)
            search_within = self.vertices.difference(self.visited)
            N += 1
        return N


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)

    adj_vertices = set()

    for _ in range(m):
        v1, v2 = map(int, input().split())
        adj_vertices.add(v1)
        adj_vertices.add(v2)
        g.add_edge(v1, v2)

    isolated_vertices = g.vertices.difference(adj_vertices)
    for v in isolated_vertices:
        g.add_isolated_vertex(v)

    print(g.get_num_of_connected_components())



