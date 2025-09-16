"""r
Máme na vstupu graph G. Chceme zjistit, zda existuje množina S t.ž. je zároveň max. nezávislá a min. pokrytí.

Pozorování: Pokud už máme hotovou a nalezenou množinu S, tak kudy mohou vést hrany? No vždycky mezi S a V \\ S

Tedy musíme ve finále mít rozdělené vrcholy na dvě barvy. Podle toho, na jaké straně hran se nacházejí.

Důležité je, že můžeme řešit každou komponentu souvislosti zvlášť. Proč?

Pokud v nějaké komponentě nelze zařídit, aby S byl max nzmna a min vtx cov, tak to určitě už nespraví zbylé komponenty.
Naopak pokud pro každou komponentu zvlášť takovou množinu máme, tak můžeme pouze vzít sjednocení těchto množin jako výsledek.

Algoritmus:
1. obarvi graf dvema barvami (hladove)
2. pokud kazda barva ma jiny pocet prvku, tak konec

"""

from typing import Optional

class Vertex:

    def __init__(self, id):
        self.id = id
        self.visited = False
        self.color : Optional[int] = None
        self.neighbors : list[Vertex] = []


    def __repr__(self):
        return f"{self.id}"


class Graph:

    def __init__(self, vertices_no : int, edges : list[tuple[int,int]]):
        self.vertices = [Vertex(i) for i in range(1,vertices_no+1)]
        self.edges = [(self.vertices[i-1],self.vertices[j-1]) for (i,j) in edges]
        
        self.set_neighbors()

    def set_neighbors(self):
        for e in self.edges:
            e[0].neighbors.append(e[1])
            e[1].neighbors.append(e[0])

    def print_colors(self):
        for vtx in self.vertices:
            print(f"({vtx}:{vtx.color})",end=", ")
        print()

    def print_graph(self):
        print(self.vertices)
        print(self.edges)
        for vtx in self.vertices:
            print(f"{vtx}: {vtx.neighbors}")

def parse_input(path : str) -> tuple[int,list[tuple[int,int]]]:
    with open(path) as file:
        num_vertices = int(file.readline())
        num_edges = int(file.readline())
        edges = []
        for i in range(num_edges):
            edges.append(tuple([int(x) for x in file.readline().split()]))
        return num_vertices,edges


def color_comp_w_colors(start_vtx : Vertex):
    stack = [start_vtx]
    start_vtx.visited = True
    start_vtx.color = 0
    while stack:
        vtx = stack.pop()
        for neigh in vtx.neighbors:
            if neigh.visited and neigh.color == vtx.color: 
                raise RuntimeError("Impossible to color component using two colors")
            if not neigh.visited:
                if vtx.color is None: 
                    raise AssertionError("Current vertex does not have color")
                neigh.color = 1 - vtx.color
                neigh.visited = True
                stack.append(neigh)

def alg(graph : Graph):
    for vtx in graph.vertices:
        if vtx.visited:
            continue
        color_comp_w_colors(vtx)

def colorgroups(g : Graph) -> tuple[list[Vertex],list[Vertex]]:
    return [vtx for vtx in g.vertices if vtx.color == 0],[vtx for vtx in g.vertices if vtx.color == 1]


vtx_n, edges = parse_input("graph3.txt")

g = Graph(vtx_n,edges)

try:
    alg(g)
    group_a, group_b = colorgroups(g)
    if len(group_a) != len(group_b):
        print("Impossible")
    else:
        print(len(group_a))
        print(" ".join([str(vtx) for vtx in group_a]))
except RuntimeError:
    print("Impossible")



