import random
import pandas as pd


class CovidLine:
    def __init__(self, ch, observation_date, province_state, country_region, last_update, confirmed, deaths, recovered):
        self.ch = ch
        self.observation_date = observation_date
        self.province_state = province_state
        self.country_region = country_region
        self.last_update = last_update
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered


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

    def ver(self):
        print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(self.covid_line.ch,
                                                                     self.covid_line.observation_date,
                                                                     self.covid_line.province_state,
                                                                     self.covid_line.country_region,
                                                                     self.covid_line.last_update,
                                                                     self.covid_line.confirmed,
                                                                     self.covid_line.deaths,
                                                                     self.covid_line.recovered))

    def visualizar(self):
        if self.left:
            self.left.visualizar()
        self.ver()
        if self.right:
            self.right.visualizar()

    def contagem(self):
        count = 0
        if self.left:
            count += self.left.contagem()
        count += 1
        if self.right:
            count += self.right.contagem()
        return count

    def inserir(self, raiz):
        if not raiz:
            return self
        if self.chave < raiz.chave:
            raiz.left = self.inserir(raiz.left)
        else:
            raiz.right = self.inserir(raiz.right)
        return raiz

    def busca(self, ch):
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


class CoviList:
    def __init__(self, ch_index=0):
        self.ch_index = ch_index
        self.raiz = None

    def visualizar(self):
        if not self.raiz:
            return
        self.raiz.visualizar()

    def contagem(self):
        if not self.raiz:
            return 0
        return self.raiz.contagem()

    def busca(self, ch):
        if not self.raiz:
            return None
        return self.raiz.busca(ch)

    def inserir(self, covid_line):
        self.raiz = CovidLineElement(covid_line, self.ch_index).inserir(self.raiz)

    def exclui(self, ch):
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
            if q:
                while q.right:
                    p = q
                    q = q.right
            if p != no:
                p.right = q.left
                if q:
                    q.left = no.left
            if q:
                q.right = no.right
        if pai:
            if ch < pai.chave:
                pai.left = q
            else:
                pai.right = q
        else:
            self.raiz = q
        del no

    def apaga_lista(self):
        return


if __name__ == "__main__":
    # incia a lista
    lista1 = CoviList()
    lista2 = CoviList(1)
    lista3 = CoviList(3)

    # lê o arquivo que contem os dados e coloca numa variavel
    data = pd.read_csv("./covid_19_data.csv")

    # cria um array com 11000 numeros, os misturando depois
    aux = list(range(len(data)))
    random.shuffle(aux)
    x = 0

    # faz o processo de criar uma nova struct, armazena dentro dela os dados de uma certa linha aleatória
    # de acordo com o array de numeros e os insere na lista, isso 100 vezes
    while x < 10:
        dado = CovidLine(*data.loc[aux[x]])

        lista1.inserir(dado)
        lista2.inserir(dado)
        lista3.inserir(dado)

        x += 1
    print("Arvore 1 ({0} elementos):".format(lista1.contagem()))
    lista1.visualizar()
    print("Arvore 2 ({0} elementos):".format(lista2.contagem()))
    lista2.visualizar()
    print("Arvore 3 ({0} elementos):".format(lista3.contagem()))
    lista3.visualizar()



