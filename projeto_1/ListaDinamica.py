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
  #inicia uma celula
  def __init__(self, CovidLine):
    self.CovidLine = CovidLine
    self.next = None

class CoviList:
  #inicia a lista
  def __init__(self):
    self.head = CovidLineElement(None)
    self.head.next = self.head

  #função de teste para visualizar a lista
  def visualizar(self):
    aux = self.head.next

    while(aux != self.head):
      print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

  def busca(self, ch):
    #prev recebe o atual e aux recebe o proximo
    prev = self.head
    aux = prev.next

    #enquanto não for o ultimo/cabeça e a chave buscada não for maior que as existentes
    while(aux != self.head and aux.CovidLine.ch < ch):
      prev = aux
      aux = aux.next

    #verifica se não for o ultimo/cabeça e a chave buscada for igual a chave existente
    #se tiver, retorna ela e o seu próximo
    if(aux != self.head and aux.CovidLine.ch == ch):
      return (aux, prev)

    #retorna nada se o while acima falhar
    return (None, prev)

  def inserirAlterar(self, CovidLine):
    #busca se a chave que se deseja adicionar já existe
    (aux, prev) = self.busca(CovidLine.ch)

    #se já existir, retorna false
    if(aux != None):
      aux.CovidLine = CovidLine
      return False

    #se não existir, cria-se um novo elemento que adiciona o dado, 
    #ele vai apontar para o próximo que era do anterior e o anterior aponta agora para o novo dado
    novo = CovidLineElement(CovidLine)
    novo.next = prev.next
    prev.next = novo
    return True

  def exclui(self, ch):
    #busca se a chave que se deseja apagar já existe
    (aux, prev) = self.busca(ch)

    #se não existir, retorna falso
    if(aux == None):
      return False

    #se existir, o anterior vai apontar para o proximo da chave excluida,
    #e depois apaga a chave desejada
    prev.next = aux.next
    del aux
    return True

  def apagaLista(self):
    aux = self.head.next

    #ele cria uma variavel temporaria, pegando a variavel que vai ser apagada
    #o aux aponta para o proxima e chave é apagada
    while(aux != self.head):
      apg = aux
      aux = aux.next
      del apg

    #cria uma lista nova, com a cabeça apontando pra si mesma
    self.head.next = self.head

  def escrever(self, outf):
    aux = self.head.next

    #ele passa por cada celula da lista, escrevendo no arquivo o seu conteúdo
    while(aux != self.head):
      outf.write("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}\n".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

if __name__ == "__main__":
  #incia a lista
  lista1 = CoviList()

  #lê o arquivo que contem os dados e coloca numa variavel
  data = pd.read_csv("./covid_19_data.csv")

  #cria um array com 11000 numeros, os misturando depois
  aux = list(range(11000))
  random.shuffle(aux)  
  x = 0

  #faz o processo de criar uma nova struct, armazena dentro dela os dados de uma certa linha aleatória
  #de acordo com o array de numeros e os insere na lista, isso 100 vezes
  while (x < 100):
    dado = CovidLine(*data.loc[aux[x]])

    lista1.inserirAlterar(dado) 

    x += 1
  
  #no final, ele pergunta o usuario se deseja imprimir no terminal ou exportar para um arquivo de texto
  dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

  while(dig != 1 and dig != 2):
    dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

  if dig == 1:    
    lista1.visualizar()

  elif dig == 2:   
    outf = open("saida_lista.txt", "w")
    lista1.escrever(outf)

  


    
 





