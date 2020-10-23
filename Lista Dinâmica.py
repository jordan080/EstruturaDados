class CovidLine:
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
    
class CovidLine:
  def __init__(self, ch, case_in_country):
    self.ch = ch
    self.case_in_country = case_in_country

class CovidLineElement:
  def __init__(self, dadoCovid):
    self.dadoCovid = dadoCovid
    self.next = None

class CoviList:
  def __init__(self):
    self.head = CovidLineElement(None)
    self.head.next = self.head
  def visualizar(self):
    aux = self.head.next
    while(aux != self.head):
      print("{0} - {1}".format(aux.dadoCovid.ch, aux.dadoCovid.case_in_country))
      aux = aux.next
  def busca(self, ch):
    prev = self.head
    aux = prev.next
    while(aux != self.head and aux.dadoCovid.ch < ch):
      prev = aux
      aux = aux.next
    if(aux != self.head and aux.dadoCovid.ch == ch):
      return (aux, prev)
    return (None, prev)
  def incerirAlterar(self, dadoCovid):
    (aux, prev) = self.busca(dadoCovid.ch)
    if(aux != None):
      aux.dadoCovid = dadoCovid
      return False
    novo = CovidLineElement(dadoCovid)
    novo.next = prev.next
    prev.next = novo
    return True
  def exclui(self, ch):
    (aux, prev) = self.busca(ch)
    if(aux == None):
      return False
    prev.next = aux.next
    del aux
    return True
  def apagaLista(self):
    aux = self.head.next
    while(aux != self.head):
      apg = aux
      aux = aux.next
      del apg
    self.head.next = self.next

if __name__ == "__main__":
  lista1 = CoviList()
