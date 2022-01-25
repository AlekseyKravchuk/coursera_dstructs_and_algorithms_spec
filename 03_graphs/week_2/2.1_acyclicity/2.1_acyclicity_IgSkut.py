class DirectedGraph:

    def __init__(self, n):
        self.adjList = {key: set() for key in range(1, n + 1)}

    def add_edge(self, src, dest):
        self.adjList[src].add(dest)

    def has_cycle(self):
        def dfs(v):
            if v in not_visited:
                not_visited.remove(v)
                visited.add(v)
            elif v in visited:
                return True
            else:
                return False
            for neighbour in self.adjList[v]:
                if dfs(neighbour):
                    return True
            visited.remove(v)
            return False

        visited = set()
        not_visited = set(self.adjList.keys())
        while not_visited:
            start = next(iter(not_visited))
            if dfs(start):
                return 1
        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())

    DG = DirectedGraph(n)

    for i in range(m):
        DG.add_edge(*map(int, input().split()))

    print(DG.has_cycle())
