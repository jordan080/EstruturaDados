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

  def buscar(self, ch):
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

  def inserir(self, CovidLine):
    #busca se a chave que se deseja adicionar já existe
    (aux, prev) = self.buscar(CovidLine.ch)

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

  def excluir(self, ch):
    #busca se a chave que se deseja apagar já existe
    (aux, prev) = self.buscar(ch)

    #se não existir, retorna falso
    if(aux == None):
      return False

    #se existir, o anterior vai apontar para o proximo da chave excluida,
    #e depois apaga a chave desejada
    prev.next = aux.next
    del aux
    return True

  def apagarEstrutura(self):
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


  


    
 





