import HeapMin
import sys


class Adjacente:
    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso
        self.next = None


class Vertice:
    def __init__(self, nome, scenes, cor):
        self.nome = nome
        self.scenes = scenes
        self.cor = cor
        self.head = None

    def __str__(self):
        red = int(self.cor[1:3], 16)
        blue = int(self.cor[3:5], 16)
        green = int(self.cor[5:7], 16)
        return "\x1B[38;2;{0};{1};{2}m{3}\x1B[0m".format(red, blue, green, self.nome)


class Grafo:
    def __init__(self):
        self.total_vertices = 0
        self.arestas = 0
        self.vertice = []
        self.dic_vec = {}

    def add_vertice(self, dado):
        self.vertice.append(Vertice(dado["name"], dado["value"], dado["colour"]))
        self.dic_vec[dado["name"]] = self.total_vertices
        self.total_vertices += 1

    def add_aresta(self, i, j, peso): # i = source; j = target
        if (i < 0) or (j < 0) or (j >= self.total_vertices) or (i >= self.total_vertices):
            return False
        novo = self.vertice[i].head
        while novo:
            if novo.vertice == j:
                novo.peso = peso
                return False
            novo = novo.next
        novo = Adjacente(j, peso)
        novo.next = self.vertice[i].head
        self.vertice[i].head = novo
        self.arestas += 1
        return True

    def __str__(self):
        #print("Vértices: {0}, Arestas: {1}\n".format(self.total_vertices, self.arestas))
        i = 0
        ss = []
        for vertice in self.vertice:
            ss.append(vertice.nome + ": ")
            adj = vertice.head
            while adj:
                ss.append("        •  {0}({1:.2f})".format(self.vertice[adj.vertice].nome, adj.peso))
                adj = adj.next
            i += 1

            ss.append("")
        return ss

    def djikstra(self, vi, vf=-1):
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
        u = vi
        while not heap_min.is_empty():
            u_prev = heap_min.pop()
            if d[u_prev] == sys.maxsize or u_prev == vf:
                if u_prev != vf:
                    return d, p, u
                return d, p, u_prev
            u = u_prev
            adj = self.vertice[u].head
            while adj:
                v = adj.vertice
                if heap_min.exists(v) and (d[u] != sys.maxsize) and (d[u] + adj.peso < d[v]):
                    d[v] = d[u] + adj.peso
                    p[v] = u
                    heap_min.decrease_key(v, d[v])
                adj = adj.next
        return d, p, u

    def menor_dist(self, nome_vi, nome_vf=None):
        if not nome_vf:
            vf = -1
        else:
            if nome_vf not in self.dic_vec: #nomes
                s = nome_vf + " nao existe no Grafo."
                return -1, s
            vf = self.dic_vec[nome_vf]
        if nome_vi not in self.dic_vec:
            s = nome_vi + " nao existe no Grafo."
            return -1, s
        vi = self.dic_vec[nome_vi]
        if nome_vf == nome_vi:
            s = nome_vi + " conecta com ele mesmo"
            return -1, s
        d, p, u = self.djikstra(vi, vf)
        ss = ""
        if nome_vf:
            if vf != u or p[u] == -1:
                s = "A personagem" + nome_vi + " não está conectado com " + nome_vf
                return -1, s
        else:
            if vi == u:
                s = "A personagem " + nome_vi + " não se conecta com ninguém"
                return -1, s
            ss = "A personagem mais distante de " + nome_vi + " é " + self.vertice[u].nome + ":\n"
            vf = u
        s = ""
        while p[u] != -1:
            s = " -> " + self.vertice[u].nome + "({0:.2f})".format(d[u]) + s
            u = p[u]
        s = self.vertice[self.dic_vec[nome_vi]].nome + s
        s = ss + "A distância entre " + self.vertice[vi].nome + " e " + self.vertice[vf].nome + " é " + str(round(d[vf], 2)) + ":\n" + s
        #print(s)
        return d[vf], s
