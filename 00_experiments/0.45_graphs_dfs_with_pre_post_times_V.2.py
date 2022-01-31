from enum import Enum
from random import randint


class State(Enum):
    UNVISITED = 0
    VISITED = 1
    PROCESSED = 2


class Vertex:
    def __init__(self, vertex_name):
        if isinstance(vertex_name, str):
            self.id = str(vertex_name)
        elif isinstance(vertex_name, int):
            self.id = vertex_name

        self.neighbors = set()

        self.pre = 0   # time when the vertex began to be processed
        self.post = 0  # time when the vertex finish to be processed, i.e. all its neighbors have already been processed
        self.discovery_state = State.UNVISITED

    def __str__(self):
        return f'{self.id}({self.pre}/{self.post})'

    def add_neighbor(self, vertex_id):
        if vertex_id not in self.neighbors:
            self.neighbors.add(vertex_id)


class UndirectedGraph:
    time = 1

    def __init__(self, n):
        self.G = {key: Vertex(key) for key in range(1, n + 1)}

    def add_edge(self, v_id, u_id):
        self.G[v_id].add_neighbor(u_id)
        self.G[u_id].add_neighbor(v_id)

    def print_graph(self):
        for key, vertex in self.G.items():
            print(f'{key}: {vertex.neighbors}')

    def dfs(self, vertex: Vertex):
        vertex.discovery_state = State.VISITED
        vertex.pre = UndirectedGraph.time
        UndirectedGraph.time += 1

        for neighbor in vertex.neighbors:
            if self.G[neighbor].discovery_state == State.UNVISITED:
                self.dfs(self.G[neighbor])

        vertex.discovery_state = State.PROCESSED
        vertex.post = UndirectedGraph.time
        print(vertex, end=' ')
        UndirectedGraph.time += 1


class DirectedGraph(UndirectedGraph):
    def __init__(self, n):
        UndirectedGraph.__init__(self, n)
        self.left2visit = set(self.G.keys())

    def add_edge(self, src, dst):
        self.G[src].add_neighbor(dst)

    def _dfs(self, vertex: Vertex):
        # TODO
        # fix it: wrong times when calling _dfs()...
        vertex.discovery_state = State.VISITED
        if vertex.id in self.left2visit:
            self.left2visit.remove(vertex.id)

        vertex.pre = UndirectedGraph.time
        UndirectedGraph.time += 1

        for neighbor in vertex.neighbors:
            if self.G[neighbor].discovery_state == State.UNVISITED:
                self._dfs(self.G[neighbor])

        vertex.discovery_state = State.PROCESSED
        vertex.post = UndirectedGraph.time
        print(vertex, end=' ')
        UndirectedGraph.time += 1

    def dfs(self, vertex: Vertex):
        while self.left2visit:
            next_vertex_id = next(iter(self.left2visit))
            print(f'DFS was started from vertex: {self.G[next_vertex_id]}')
            self._dfs(self.G[next_vertex_id])


if __name__ == '__main__':
    n, m = map(int, input().split())

    # graph = UndirectedGraph(n)
    dir_graph = DirectedGraph(n)
    for _ in range(m):
        dir_graph.add_edge(*map(int, input().split()))

    # dir_graph.print_graph()

    vertex2start = dir_graph.G[randint(1, n)]
    print(f'DFS was started from vertex: {vertex2start}')
    dir_graph.dfs(vertex2start)

