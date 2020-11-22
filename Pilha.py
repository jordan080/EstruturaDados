import random
import pandas as pd

class CovidLineElement:
  #inicia uma celula
  def __init__(self, CovidLine):
    self.CovidLine = CovidLine
    self.next = None

class CoviList:
  #inicia a pilha
  def __init__(self):
    self.head = None

  #função de teste para visualizar a lista
  def visualizar(self):
    aux = self.head
    while(aux != None):
      print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

  def excluir(self):
    #se o item atual for a cabeça, ele volta. Se não, ele simplesmente ajusta para que
    #o atual aponte para o proximo e retorna quem ele removeu
    if (self.head == None):
      return False
    aux = self.head.CovidLine
    self.head = self.head.next
    return aux

  def inserir(self, CovidLine):
    #ele cria uma nova celula e o adiciona a pilha, seguindo o modelo da lista, porém, 
    #sem a necessidade de buscar se ela já existe
    novo = CovidLineElement(CovidLine)
    novo.next = self.head
    self.head = novo
    return True

  def apagarEstrutura(self):
    #enquanto não tiver nada na pilha, ele chama a função que remove os items dela
    while(self.head != None):
      self.pop()

  def escrever(self, outf):
    aux = self.head

    #ele passa por cada celula da pilha, escrevendo no arquivo o seu conteúdo
    while(aux != None):
      outf.write("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}\n".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next




