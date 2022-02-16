from enum import Enum


class State(Enum):
    UNVISITED = 0
    VISITED = 1
    PROCESSED = 2


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
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
            print(f'{key}: {vertex.G}')

    def dfs(self, vertex: Vertex):
        vertex.discovery_state = State.VISITED
        vertex.pre = UndirectedGraph.time
        UndirectedGraph.time += 1

        for neighbor in vertex.neighbors:
            if self.G[neighbor].state == State.UNVISITED:
                self.dfs(self.G[neighbor])

        vertex.discovery_state = State.PROCESSED
        vertex.post = UndirectedGraph.time
        print(vertex, end=' ')
        UndirectedGraph.time += 1


class DirectedGraph(UndirectedGraph):
    def __init__(self, n):
        UndirectedGraph.__init__(self, n)
        self.left2visit = set(self.G.keys())
        self.is_DAG = None

    def add_edge(self, src, dst):
        self.G[src].add_neighbor(dst)

    def _dfs(self, vertex: Vertex):
        vertex.discovery_state = State.VISITED
        if vertex.id in self.left2visit:
            self.left2visit.remove(vertex.id)

        vertex.pre = UndirectedGraph.time
        UndirectedGraph.time += 1

        for neighbor in vertex.neighbors:
            if self.G[neighbor].state == State.UNVISITED:
                self._dfs(self.G[neighbor])
            elif self.G[neighbor].state == State.VISITED:
                self.is_DAG = False

        vertex.discovery_state = State.PROCESSED
        vertex.post = UndirectedGraph.time
        print(vertex, end=' ')
        UndirectedGraph.time += 1

    def dfs(self):
        while self.left2visit:
            next_vertex_id = next(iter(self.left2visit))
            print(f'\nDFS was started from vertex: {self.G[next_vertex_id]}')
            self._dfs(self.G[next_vertex_id])
        if self.is_DAG is None:
            self.is_DAG = True
        print(f"\nThe given directed graph {'is ACYCLIC' if self.is_DAG else 'has at least 1 cycle'}")


if __name__ == '__main__':
    n, m = map(int, input().split())
    dir_graph = DirectedGraph(n)

    for _ in range(m):
        dir_graph.add_edge(*map(int, input().split()))

    dir_graph.dfs()

