class HeapMinNode:
    def __init__(self, senha, prioridade):
        self.senha = senha
        self.prioridade = prioridade


class HeapMin:

    def __init__(self, n):
        self.size = 0
        self.capacity = n
        self.fila = []
        self.posicao = []
        for i in range(n):
            self.posicao.append(i)
            self.fila.append(HeapMinNode(i, 0))

    def swap(self, i, j):
        temp = self.fila[i]
        self.fila[i] = self.fila[j]
        self.fila[j] = temp

    def heapfy(self, v):
        smallest = v
        left = 2 * v + 1
        right = left + 1
        if left >= self.size:
            return
        if self.fila[smallest].prioridade > self.fila[left].prioridade:
            smallest = left
        if self.fila[smallest].prioridade > self.fila[right].prioridade:
            smallest = right
        if v != smallest:
            small_node = self.fila[smallest]
            v_node = self.fila[v]
            self.posicao[small_node.senha] = v
            self.posicao[v_node.senha] = smallest
            self.swap(v, smallest)
            self.heapfy(smallest)

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            return -1
        root = self.fila[0]
        senha = root.senha
        last = self.fila[self.size - 1]
        self.fila[0] = last
        self.posicao[root.senha] = self.size - 1
        self.posicao[last.senha] = 0
        self.size -= 1
        self.heapfy(0)
        del root
        return senha

    def exists(self, v):
        return self.posicao[v] < self.size

    def decrease_key(self, v, d):
        i = self.posicao[v]
        pai = (i - 1) // 2
        self.fila[i].prioridade = d
        while(i > 0) and (self.fila[i].prioridade < self.fila[pai].prioridade):
            self.posicao[self.fila[i].senha] = pai
            self.posicao[self.fila[pai].senha] = i
            self.swap(i, pai)
            i = pai
            pai = (i - 1) // 2
