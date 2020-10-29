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
  #elemento que armazena os dados da celula
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
  #inicia a pilha
  def __init__(self):
    self.head = None

  #função de teste para visualizar a lista
  def visualizar(self):
    aux = self.head
    while(aux != None):
      print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

  def pop(self):
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

  def apagaLista(self):
    #enquanto não tiver nada na pilha, ele chama a função que remove os items dela
    while(self.head != None):
      self.pop()

  def escrever(self, outf):
    aux = self.head

    #ele passa por cada celula da pilha, escrevendo no arquivo o seu conteúdo
    while(aux != None):
      outf.write("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}\n".format(aux.CovidLine.ch, aux.CovidLine.observation_date, aux.CovidLine.province_state, aux.CovidLine.country_region, aux.CovidLine.last_update, aux.CovidLine.confirmed, aux.CovidLine.deaths, aux.CovidLine.recovered))
      aux = aux.next

if __name__ == "__main__":
  #incia a pilha
  lista1 = CoviList()

  #lê o arquivo que contem os dados e coloca numa variavel
  data = pd.read_csv('./covid_19_data.csv')

  #cria um array com 11000 numeros, os misturando depois
  aux = list(range(11000))
  random.shuffle(aux)  
  x = 0

  #faz o processo de criar uma nova struct, armazena dentro dela os dados de uma certa linha aleatória
  #de acordo com o array de numeros e os insere na pilha, isso 100 vezes
  while (x < 100):
    dado = CovidLine(*data.loc[aux[x]])

    lista1.inserir(dado)

    x += 1

  #no final, ele pergunta o usuario se deseja imprimir no terminal ou exportar para um arquivo de texto
  dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

  while(dig != 1 and dig != 2):
    dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

  if dig == 1:    
    lista1.visualizar()

  elif dig == 2:   
    outf = open("saida_pilha.txt", "w")
    lista1.escrever(outf)



