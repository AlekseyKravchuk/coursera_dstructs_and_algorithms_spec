from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)


class DGraph:
    def __init__(self, n):
        self.n = n
        self.G = {key: set() for key in range(1, n+1)}
        self.G_rev = deepcopy(self.G)

        self.visited = set()
        self.left2visit = set(self.G.keys())
        self.stack_revG = []

    def add_edge(self, src, dst):
        self.G[src].add(dst)
        self.G_rev[dst].add(src)

    def print_graph(self):
        for vertex, neighbors in self.G.items():
            print(f'{vertex}: {neighbors}')

    def dfs_in_rev_graph(self, vertex):
        self.visited.add(vertex)
        self.left2visit.remove(vertex)

        for neighbor in self.G_rev[vertex]:
            if neighbor in self.visited:
                continue
            self.dfs_in_rev_graph(neighbor)

        self.stack_revG.append(vertex)

    def dfs(self, vertex):
        self.visited.add(vertex)

        for neighbor in self.G[vertex]:
            if neighbor in self.visited:
                continue
            self.dfs(neighbor)

    def get_scc_num(self):
        # pass 1: at the end of this pass 'self.stack_revG' will be generated
        while self.left2visit:
            vertex = next(iter(self.left2visit))
            self.dfs_in_rev_graph(vertex)

        # pass 2
        self.visited.clear()
        N = 0  # number of strongly connected components

        while self.stack_revG:
            vertex = self.stack_revG.pop()

            if vertex in self.visited:
                continue

            self.dfs(vertex)
            N += 1

        return N


if __name__ == '__main__':
    n, m = map(int, input().split())

    G = DGraph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))

    # G.print_graph()
    scc_num = G.get_scc_num()
    print(scc_num)





