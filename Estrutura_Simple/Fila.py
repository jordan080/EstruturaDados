#FIFO - First in First out - FILA

class CovidLineElement:
  #representa uma celula da fila
  def __init__(self, CovidLine):
    self.CovidLine = CovidLine
    self.next = None

class CoviList:
  #inicia a lista/celula
  #o primeiro elemento será tbm o ultimo
  def __init__(self):
    self.head = None
    self.last = None

  def visualizar(self):
    #função que imprime na tela
    aux = self.head
    while(aux != None):
      print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

  def __str__(self):
    aux = self.head
    s = []
    while(aux != None):
      s.append("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}\n".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next
    return s

  def excluir(self):
    #remove um item da fila, em um esquema semelhante o da lista e pilha
    if (self.head == None):
      return False

    elem = self.head.CovidLine
    self.head = self.head.next
    return elem

  def inserir(self, CovidLine):
    #cria uma nova celula e a preenche com uma struct
    novo = CovidLineElement(CovidLine)
    novo.next = None

    #se a fila estiver vazia, a cabeça aponta para essa nova celula
    if self.head is None:
      self.head = novo

    #se o final da fila não estiver vazio, o ultimo aponta para essa nova celula
    if (self.last != None):
      self.last.next = novo

    #a nova celula passa a ser ultima, de acordo com o esquema da fila
    self.last = novo

  def apagarEstrutura(self):
    #função que passa por todas as celulas, as apagando
    while(self.head != None):
      self.excluir()

  def escrever(self, outf):
    #função que escreve num arquivo de saida
    aux = self.head

    while(aux != None):
      outf.write("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}\n".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next
