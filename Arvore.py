class CovidLineElement:
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
        return "{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(self.covid_line.ch,
                                                                      self.covid_line.observation_date,
                                                                      self.covid_line.province_state,
                                                                      self.covid_line.country_region,
                                                                      self.covid_line.last_update,
                                                                      self.covid_line.confirmed,
                                                                      self.covid_line.deaths,
                                                                      self.covid_line.recovered)

    def visualizar(self):
        if self.left:
            self.left.visualizar()
        print(self)
        if self.right:
            self.right.visualizar()

    def inserir(self, raiz):
        if not raiz:
            return self
        if self.chave < raiz.chave:
            raiz.left = self.inserir(raiz.left)
        else:
            raiz.right = self.inserir(raiz.right)
        return raiz

    def buscar(self, ch):
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
        atual = self
        pai = None
        while atual:
            if atual.chave == ch:
                atual.ver()
                return atual, pai
            pai = atual
            if atual.chave > ch:
                atual = atual.left
            else:
                atual = atual.right
        return None, pai

    def escrever(self, outf):
        if self.left:
            self.left.escrever(outf)
        outf.write(self.__str__() + "\n")
        if self.right:
            self.right.escrever(outf)

    def apagar(self):
        if self.left:
            self.left.apagar()
        if self.right:
            self.right.apagar()
        del self


class CoviList:
    def __init__(self, ch_index=0):
        self.ch_index = ch_index
        self.raiz = None

    def visualizar(self):
        if not self.raiz:
            return
        self.raiz.visualizar()

    def buscar(self, ch):
        if not self.raiz:
            return None
        return self.raiz.buscar(ch)

    def inserir(self, covid_line):
        self.raiz = CovidLineElement(covid_line, self.ch_index).inserir(self.raiz)

    def excluir(self, ch):
        if not self.raiz:
            return
        no, pai = self.raiz.busca_pai(ch)
        if not no:
            return
        if not no.left or not no.right:
            if not no.left:
                q = no.right
            else:
                q = no.left
        else:
            p = no
            q = no.left
            while q.right:
                p = q
                q = q.right
            if p != no:
                p.right = q.left
                q.left = no.left
            q.right = no.right
        if pai:
            if ch < pai.chave:
                pai.left = q
            else:
                pai.right = q
        else:
            self.raiz = q
        del no

    def apagarEstrutura(self):
        if self.raiz:
            self.raiz.apagar()
        self.raiz = None

    def escrever(self, outf):
        if self.raiz:
            self.raiz.escrever(outf)
