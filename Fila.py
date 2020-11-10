import random
import pandas as pd

#FIFO - First in First out - FILA

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

  def excluir(self):
    if (self.head == None):
      return False

    elem = self.head.CovidLine
    self.head = self.head.next
    return elem

  def inserir(self, CovidLine):
    #se não existir, cria-se um novo elemento que adiciona o dado,
    #ele vai apontar para o próximo que era do anterior e o anterior aponta agora para o novo dado
    novo = CovidLineElement(CovidLine)
    novo.next = None

    if self.head is None:
      self.head = novo

    if (self.last != None):
      self.last.next = novo
    
    self.last = novo

  def apagarEstrutura(self):
    #ele cria uma variavel temporaria, pegando a variavel que vai ser apagada
    #o aux aponta para o proxima e chave é apagada
    while(self.head != None):
      self.pop()

  def escrever(self, outf):
    aux = self.head

    while(aux != None):
      outf.write("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}\n".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next