import Grafo
import random
import Struct

L = 10
rrr = list(range(L))
random.shuffle(rrr)
ggg = Grafo.Grafo()
for node in Struct.starwars["nodes"]:
    ggg.add_vertice(node)

for link in Struct.starwars["links"]:
    ggg.add_aresta(link["source"], link["target"], 10.0 / link["value"])
    ggg.add_aresta(link["target"], link["source"], 10.0 / link["value"])

print(ggg)

for i in range(100):
    nome1 = ggg.vertice[random.randint(0, ggg.total_vertices-1)]
    nome2 = ggg.vertice[random.randint(0, ggg.total_vertices-1)]
    ggg.menor_dist(nome1.nome, nome2.nome)
j = -1
d_max = -1
for i in range(ggg.total_vertices):
    d = ggg.menor_dist(ggg.vertice[i].nome)
    if d > d_max:
        j = i
        d_max = d
ggg.menor_dist("PLO KOON")
#A personagem R2-D2 não está conectado com GOLD FIVE
#A personagem ADMIRAL ACKBAR conecta com ele mesmo
#A personagem GOLD FIVE não está conectado com ORN FREE TAA
#O personagem mais distante de R2-D2 é COLONEL DATOO:
#R2-D2 -> C-3PO(0.18) -> HAN(0.37) -> REY(0.96) -> KYLO REN(3.46) -> GENERAL HUX(5.46) -> COLONEL DATOO(15.46)
#A personagem GOLD FIVE não se conecta com ninguém
#A personagem mais distante de PLO KOON é COLONEL DATOO:
#A distância entre PLO KOON e COLONEL DATOO é 28.775338888197986:
#PLO KOON -> KI-ADI-MUNDI(10.00) -> YODA(12.50) -> OBI-WAN(13.00) -> LUKE(13.45) -> HAN(13.69) -> REY(14.28) -> KYLO REN(16.78) -> GENERAL HUX(18.78) -> COLONEL DATOO(28.78)