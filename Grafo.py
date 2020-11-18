import HeapMin
import sys


class Adjacente:
    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso
        self.next = None


class Vertice:
    def __init__(self, dado, chave):
        self.dado = dado
        self.chave = chave
        self.head = None


class Grafo:
    def __init__(self, index_chave=0):
        self.index_chave = index_chave
        self.total_vertices = 0
        self.arestas = 0
        self.vertice = []

    def add_vertice(self, dado):
        self.vertice.append(Vertice(dado, dado[self.index_chave]))
        self.total_vertices += 1

    def add_aresta(self, i, j, peso):
        if (i < 0) or (j < 0) or (j >= self.total_vertices) or (i >= self.total_vertices):
            return False
        novo = self.vertice[i].head
        while novo:
            if novo.vertice == j:
                novo.peso = peso
                return True
            novo = novo.next
        novo = Adjacente(j, peso)
        novo.next = self.vertice[i].head
        self.vertice[i].head = novo
        self.arestas += 1
        return True

    def __str__(self):
        print("Vértices: {0}, Arestas: {1}\n".format(self.total_vertices, self.arestas))
        i = 0
        s = ""
        for vertice in self.vertice:
            s += "v" + str(i) + ": "
            adj = vertice.head
            while adj:
                s += "v{0}({1}) ".format(adj.vertice, adj.peso)
                adj = adj.next
            s += "\n"
            i += 1
        return s

    def djikstra(self, vi):
        d = []
        p = []
        heap_min = HeapMin.HeapMin(self.total_vertices)
        for i in range(self.total_vertices):
            d.append(sys.maxsize)
            p.append(-1)
            heap_min.fila[i].senha = i
            heap_min.fila[i].prioridade = d[i]
            heap_min.posicao[i] = i
        d[vi] = 0
        heap_min.decrease_key(vi, 0)
        heap_min.size = self.total_vertices
        while not heap_min.is_empty():
            u = heap_min.pop()
            adj = self.vertice[u].head
            while adj:
                v = adj.vertice
                if heap_min.exists(v) and (d[u] != sys.maxsize) and (d[u] + adj.peso < d[v]):
                    d[v] = d[u] + adj.peso
                    p[v] = u
                    heap_min.decrease_key(v, d[v])
                adj = adj.next
        return d, p
