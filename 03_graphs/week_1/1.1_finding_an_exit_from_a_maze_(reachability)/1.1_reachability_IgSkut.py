# This is a sample Python script.
# Press the green button in the gutter to run the script.
class Graph:
    # Constructor
    def __init__(self, n):
        # A list of lists to represent an adjacency list
        self.adjList = {key: set() for key in range(1, n + 1)}

    def add_edge(self, src, dest):
        self.adjList[src].add(dest)
        self.adjList[dest].add(src)

    def print_graph(self):
        for k, v in self.adjList.items():
            print('{}: {}'.format(k, v))


def is_reachable(graph, v1, v2):
    visited = set()

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

    return dfs(v1)


# def num_of_components(graph):
#     not_visited = {key for key in graph.adjList.keys()}
#
#     def dfs(v):
#         if v not in not_visited:
#             return
#         not_visited.remove(v)
#         for neighbour in graph.adjList[v]:
#             dfs(neighbour)
#     num = 0
#
#     while len(not_visited) > 0:
#         start = not_visited[0]
#         dfs(start)
#         num += 1
#     return num


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)
    for i in range(m):
        G.add_edge(*map(int, input().split()))
    v1, v2 = map(int, input().split())
    # G.print_graph()
    print(int(is_reachable(G, v1, v2)))
    # print(num_of_components(G))
