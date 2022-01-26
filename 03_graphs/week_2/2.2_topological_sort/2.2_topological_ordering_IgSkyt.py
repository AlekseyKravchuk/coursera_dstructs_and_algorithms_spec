class DirectedGraph:
    def __init__(self, n):
        self.adjList = {key: set() for key in range(1, n + 1)}

    def add_edge(self, src, dest):
        self.adjList[src].add(dest)

    # def topological_sort(self):
    #     def dfs(v):
    #         if v in visited:
    #             return True
    #         if v in not_visited:
    #             not_visited.remove(v)
    #             visited.add(v)
    #             for neighbour in self.adjList[v]:
    #                 if dfs(neighbour):
    #                     return True
    #             visited.remove(v)
    #             processed.append(v)
    #
    #     visited = set()
    #     not_visited = set(self.adjList.keys())
    #     processed = []
    #
    #     while not_visited:
    #         start = next(iter(not_visited))
    #         if dfs(start):
    #             return 'Graph can\'t be sorted because of cycle'
    #     processed.reverse()
    #     return processed

    def kahn_sort(self):
        in_degree = {key: 0 for key in self.adjList.keys()}
        for v in self.adjList.values():
            for i in v:
                in_degree[i] += 1
        empty = set()
        n = 0
        for k in in_degree.keys():
            if in_degree[k] == 0:
                empty.add(k)
            n += 1
        result = []
        while empty:
            vertice = empty.pop()
            result.append(vertice)
            for neighbour in self.adjList[vertice]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    empty.add(neighbour)
            n -= 1
        if n != 0:
            return 'Graph can\'t be sorted because of cycle'
        return result


if __name__ == '__main__':
    n, m = map(int, input().split())

    DG = DirectedGraph(n)

    for i in range(m):
        DG.add_edge(*map(int, input().split()))

    # print(*DG.topological_sort())
    print(*DG.kahn_sort())
