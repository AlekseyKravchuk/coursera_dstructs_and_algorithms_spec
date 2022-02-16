# implementation of an undirected graph using Adjacency Lists
# explanation https://www.youtube.com/watch?v=HDUzBEG1GlA
class Vertex:
    def __init__(self, name):
        self.name = name         # name of vertex
        self.neighbors = list()  # adjacency list of neighbors

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
            return True
        else:
            return False


class Graph:
    # dictionary of vertices, vertices = {name_of_vertex: vertex_object}
    # class variable
    vertices = {}

    def add_vertex(self, vertex: Vertex):
        # check that object you passed in is actually a 'Vertex' object
        # and that its name doesn't exist in 'vertices' dictionary yet
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    # add edge with vertices 'u' and 'v' using their names
    def add_edge(self, u_name, v_name):
        # first check if both 'u' and 'v' vertices exist in 'vertices' dictionary
        if u_name in self.vertices and v_name in self.vertices:
            self.vertices[u_name].add_neighbor(v_name)
            self.vertices[v_name].add_neighbor(u_name)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].G))


if __name__ == '__main__':
    g = Graph()
    # print(str(len(g.vertices)))
    # a = Vertex('A')
    # g.add_vertex(Vertex('A'))
    # g.add_vertex(Vertex('B'))

    vertices_lst = [x for x in range(ord('A'), ord(''))]
    for i in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.print_graph()

