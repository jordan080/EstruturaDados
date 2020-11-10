import os
import random
import pandas as pd
import sys

#FIFO - First in First out - FILA

#Cada coluna do Banco de dados/struct
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
  #dadoCovid é o CovidLine, ou seja, a struct
  def __init__(self, CovidLine):
    self.CovidLine = CovidLine
    self.next = None

class CoviList:
  #inicia a lista/celula
  #o primeiro elemento será tbm o ultimo
  def __init__(self):
    self.head = None
    self.last = None

  #função de teste para visualizar a lista
  def visualizar(self):
    aux = self.head
    while(aux != None):
      print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

  def pop(self):
    if (self.head == None):
      return False
    elem = self.head.CovidLine
    self.head = self.head.next
    return elem

  def inserir(self, CovidLine):
    #se não existir, cria-se um novo elemento que adiciona o dado,
    #ele vai apontar para o próximo que era do anterior e o anterior aponta agora para o novo dado
    novo = CovidLineElement(CovidLine)
    novo.next = self.head
    if self.last is None:
        self.last = novo
    else:
        #o "novo" vai ser o proximo e tbm o ultimo da fila
        self.last.next = novo
        self.last = novo

    if self.head is None:
        self.head = novo


  def apagaLista(self):
    #ele cria uma variavel temporaria, pegando a variavel que vai ser apagada
    #o aux aponta para o proxima e chave é apagada
    while(self.head != None):
      self.pop()

  def escrever(self, outf):
    aux = self.head.next

    while(aux != self.head):
      outf.write("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}\n".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

if __name__ == "__main__":
  lista1 = CoviList()

  data = pd.read_csv('./covid_19_data.csv')

  aux = list(range(11000))
  random.shuffle(aux)
  x = 0

  while (x < 10):
    dado = CovidLine(*data.loc[aux[x]])

    lista1.inserir(dado)

    x += 1


  dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

  while (dig != 1 and dig != 2):
    dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

  if dig == 1:
    lista1.visualizar()

  elif dig == 2:
    outf = open(cwd + "/saida.txt", "w")
    lista1.escrever(outf)