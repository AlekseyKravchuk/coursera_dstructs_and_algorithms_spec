class Graph:
    def __init__(self, n):
        self.G = {key: set() for key in range(1, n + 1)}
        self.in_deg_v = {key: 0 for key in range(1, n+1)}

    def add_edge(self, start, end):
        self.G[start].add(end)
        self.in_deg_v[end] += 1

    def print_graph(self):
        for vertex, neighbors in self.G.items():
            print('{}: {}'.format(vertex, ', '.join(map(str, neighbors))))

    def print_in_deg_v(self):
        for vertex, in_deg_v in self.in_deg_v.items():
            print('{}: {}'.format(vertex, in_deg_v))

    def generate_topology_ordering(self):
        topology = []
        with_zero_incoming_degree = set()

        for vertex, degree in self.in_deg_v.items():
            if degree == 0:
                with_zero_incoming_degree.add(vertex)

        while with_zero_incoming_degree:
            current = with_zero_incoming_degree.pop()
            topology.append(current)

            for neighbor in self.G[current]:
                self.in_deg_v[neighbor] -= 1
                if self.in_deg_v[neighbor] == 0:  # if incoming degree of given neighbor becomes 0
                    with_zero_incoming_degree.add(neighbor)
        return topology


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)

    for _ in range(m):
        G.add_edge(*map(int, input().split()))

    print(*G.generate_topology_ordering())
