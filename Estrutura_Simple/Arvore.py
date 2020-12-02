#todas as funções daqui usam a "pre-order" como forma de percorrer pela árvore
#ou seja, a partir da raiz, se percorre para a esquerda e depois para a direita

class CovidLineElement:
    #redireciona para a arvore de acordo com a chave escolhida
    def __init__(self, covid_line, ch_index):
        self.covid_line = covid_line
        if ch_index == 0:
            self.chave = self.covid_line.ch
        elif ch_index == 1:
            self.chave = self.covid_line.observation_date
        elif ch_index == 2:
            self.chave = self.covid_line.province_state
        elif ch_index == 3:
            self.chave = self.covid_line.country_region
        elif ch_index == 4:
            self.chave = self.covid_line.last_update
        elif ch_index == 5:
            self.chave = self.covid_line.confirmed
        elif ch_index == 6:
            self.chave = self.covid_line.deaths
        elif ch_index == 7:
            self.chave = self.covid_line.recovered
        else:
            self.chave = self.covid_line.ch
        self.right = None
        self.left = None

    def __str__(self):
        #função separada que retorna a linha que contem os dados.
        return "{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(self.covid_line.ch,
                                                                      self.covid_line.observation_date,
                                                                      self.covid_line.province_state,
                                                                      self.covid_line.country_region,
                                                                      self.covid_line.last_update,
                                                                      self.covid_line.confirmed,
                                                                      self.covid_line.deaths,
                                                                      self.covid_line.recovered)

    def auxstr(self, s):
        if self.left:
            self.left.auxstr(s)
        s.append(self.__str__())
        if self.right:
            self.right.auxstr(s)

    def visualizar(self):
        #função que imprime no terminal, percorrendo nós recursivamente
        if self.left:
            self.left.visualizar()
        print(self)
        if self.right:
            self.right.visualizar()

    def inserir(self, raiz):
        #verifica se não é a raiz e percorre os nós até chegar numa certa posição e adicionar o novo nó 
        #de acordo com o valor da chave, ficando ordenado com o resto da árvore
        if not raiz:
            return self
        if self.chave < raiz.chave:
            raiz.left = self.inserir(raiz.left)
        else:
            raiz.right = self.inserir(raiz.right)
        return raiz

    def buscar(self, ch):
        #pequena função que busca um certo nó, percorrendo os nós recursivamente, fazendo as comparações de chave
        if self.chave == ch:
            return self
        if self.chave > ch:
            if not self.left:
                return None
            return self.left.busca(ch)
        if not self.right:
            return None
        return self.right.busca(ch)

    def busca_pai(self, ch):
        #função que busca um certo nó e o seu pai, da mesma forma que a função "buscar"
        atual = self
        pai = None
        while atual:
            if atual.chave == ch:
                return atual, pai
            pai = atual
            if atual.chave > ch:
                atual = atual.left
            else:
                atual = atual.right
        return None, pai

    def escrever(self, outf):
        #função que escreve no arquivo de saida, percorrendo os nós da árvore
        if self.left:
            self.left.escrever(outf)
        outf.write(self.__str__() + "\n")
        if self.right:
            self.right.escrever(outf)

    def apagar(self):
        #pequena função que sai apagando todos os nós da árvore
        if self.left:
            self.left.apagar()
        if self.right:
            self.right.apagar()
        del self


class CoviList:
    def __init__(self, ch_index=0):
        #inicia a árvore
        self.ch_index = ch_index
        self.raiz = None

    def visualizar(self):
        #metodo que chama a função de visualizar no terminal
        if not self.raiz:
            return
        self.raiz.visualizar()

    def __str__(self):
        if not self.raiz:
            return
        s = []
        self.raiz.auxstr(s)
        return s

    def buscar(self, ch):
        #metodo que chama a função de buscar um certo nó
        if not self.raiz:
            return None
        return self.raiz.buscar(ch)

    def inserir(self, covid_line):
        #metodo que insere um novo nó, respeitando o tipo da árvore, chamando a função de inserir
        self.raiz = CovidLineElement(covid_line, self.ch_index).inserir(self.raiz)

    def excluir(self, ch):
        #função que apaga um certo nó, a partir de uma serie de procedimentos

        #notacao:
        #no = nó que vai ser apagado
        #pai = pai desse nó que vai ser apagado
        #q = nó que vai subsitituir o nó que será apagado, neste caso sendo o mais a direita da parte esquerda da árvore, pois a sua chave
        #tem valor mais próximo que o da raiz
        #p = pai desse nó subsitituto

        #verfica que não é a raiz e busca pela posição onde está o nó que se deseja apagar e o seu pai
        if not self.raiz:
            return False
        no, pai = self.raiz.busca_pai(ch)
        #se o no não existe, retorna
        if not no:
            return False
        #se o nó só tiver um filho, verifica se ele está na direita ou na esquerda e o atribui em q 
        if not no.left or not no.right:
            if not no.left:
                q = no.right
            else:
                q = no.left
        #se não, ele faz o procedimento de buscar q e p, localizando q na mais direita da parte esquerda da árvore
        else:
            p = no
            q = no.left
            while q.right:
                p = q
                q = q.right
            #troca os ponteiros do "no" e o "q", sendo que o pai(p) de q adota o seu filho a esquerda
            #e o filho a esquerda de q passa a ser o seu pai(p)
            if p != no:
                p.right = q.left
                q.left = no.left
            #e a direita de q adota o filho a direita do nó a ser exluido
            q.right = no.right
        #o pai do nó que vai ser apagado passa a ter como filho q, se ele não existir, é a raiz que adota
        if pai:
            if ch < pai.chave:
                pai.left = q
            else:
                pai.right = q
        else:
            self.raiz = q
        #o nó é apagado
        del no
        return True

    def apagarEstrutura(self):
        #apaga a arvore, apagando todos os nós recursivamente e depois fazendo a raiz ter valor nulo
        if self.raiz:
            self.raiz.apagar()
        self.raiz = None

    def escrever(self, outf):
        #metodo que chama a função de escrever num arquivo de saida
        if self.raiz:
            self.raiz.escrever(outf)
