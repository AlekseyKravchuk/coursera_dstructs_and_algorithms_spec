# This is a sample Python script.
# Press the green button in the gutter to run the script.
class Graph:
    def __init__(self, n):
        self.adjList = {key: set() for key in range(1, n + 1)}

    def add_edge(self, src, dest):
        self.adjList[src].add(dest)
        self.adjList[dest].add(src)

    def print_graph(self):
        for k, v in self.adjList.items():
            print('{}: {}'.format(k, v))


def is_reachable(graph, v1, v2):
    def dfs(v1):
        if v1 == v2:
            return True

        if v1 in visited:
            return False
        visited.add(v1)
        for v in graph.adjList[v1]:
            if dfs(v):
                return True
        return False

    visited = set()
    return dfs(v1)


def num_of_components(graph):
    def dfs(v):
        if v not in left2process:
            return
        left2process.remove(v)
        for neighbour in graph.adjList[v]:
            dfs(neighbour)

    # left2process = {key for key in graph.adjList.keys()}
    left2process = set(graph.adjList.keys())
    num = 0
    while left2process:
        start = next(iter(left2process))
        dfs(start)
        num += 1
    return num


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)
    for i in range(m):
        G.add_edge(*map(int, input().split()))
    # v1, v2 = map(int, input().split())
    # G.print_graph()
    # print(is_reachable(G, v1, v2))
    print(num_of_components(G))
