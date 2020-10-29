import random
import pandas as pd

'''class CovidLine:
  #essa é a classe que armazena todos os dados
  def __init__(self, ch, case_in_country, age, if_onset_approximated, visiting_Wuhan, from_Wuhan, death, recovered, symptom, reporting_date, summary, location, country, gender, symptom_onset, hosp_visit_date, exposure_start, exposure_end, source, link):
    self.ch = ch
    self.case_in_country = case_in_country
    self.age = age
    self.if_onset_approximated = if_onset_approximated
    self.visiting_Wuhan = visiting_Wuhan
    self.from_Wuhan = from_Wuhan
    self.death = death
    self.recovered = recovered
    self.symptom = symptom
    self.reporting_date = reporting_date
    self.summary = summary
    self.location =location
    self.country = country
    self.gender = gender
    self.symptom_onset = symptom_onset
    self.hosp_visit_date = hosp_visit_date
    self.exposure_start = exposure_start
    self.exposure_end = exposure_end
    self.source = source
    self.link = link
'''
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

if __name__ == "__main__":
  lista1 = CoviList()

  data = pd.read_csv('covid_19_data.csv')

  aux = list(range(11000))
  random.shuffle(aux)  
  x = 0

  while (x < 100):
    dado = CovidLine(*data.loc[aux[x]])

    lista1.inserirAlterar(dado) 

    x += 1



