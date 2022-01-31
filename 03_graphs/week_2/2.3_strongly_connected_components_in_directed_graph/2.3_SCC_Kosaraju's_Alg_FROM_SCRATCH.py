from copy import deepcopy


class DGraph:
    def __init__(self, n):
        self.n = n
        self.G = {key: set() for key in range(1, n+1)}
        self.G_rev = deepcopy(self.G)

        self.visited = set()
        self.stack_revG = []
        self.SCC = []

    def add_edge(self, src, dst):
        self.G[src].add(dst)
        self.G_rev[dst].add(src)

    def print_graph(self):
        for vertex, neighbors in self.G.items():
            print(f'{vertex}: {neighbors}')

    def dfs_in_rev_graph(self, vertex):
        self.visited.add(vertex)

        for neighbor in self.G_rev[vertex]:
            if neighbor in self.visited:
                continue
            self.dfs_in_rev_graph(neighbor)

        self.stack_revG.append(vertex)

    def dfs(self, vertex, scc_holder):
        self.visited.add(vertex)

        for neighbor in self.G[vertex]:
            if neighbor in self.visited:
                continue
            self.dfs(neighbor, scc_holder)

        scc_holder.add(vertex)

    def get_strongly_connected_components(self):
        # pass 1: at the end of this pass 'self.stack_revG' will be generated
        left2visit = set(self.G_rev.keys())
        while left2visit:
            vertex = left2visit.pop()
            self.dfs_in_rev_graph(vertex)
            left2visit = set(self.G.keys()).difference(self.visited)

        # pass 2
        self.visited.clear()
        while self.stack_revG:
            vertex = self.stack_revG.pop()
            if vertex in self.visited:
                continue

            scc_holder = set()
            self.dfs(vertex, scc_holder)
            self.SCC.append(scc_holder)

        return self.SCC


if __name__ == '__main__':
    n, m = map(int, input().split())

    G = DGraph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))

    # G.print_graph()
    scc = G.get_strongly_connected_components()
    for component in scc:
        print(component)






