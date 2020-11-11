import Struct
import ListaDinamica
import Pilha
import Fila
import Arvore
import pandas as pd
import random

opt = int(input('''Escolha uma opção para como deseja estruturar seus dados:
1-Lista Dinâmica
2-Pilha
3-Fila
4-Árvore
Opção: '''))

while (opt < 0 or opt > 4):
    opt = int(input("Tente novamente: "))

if (opt == 1):
    estrutura = ListaDinamica.CoviList()

elif (opt == 2):
    estrutura = Pilha.CoviList()

elif (opt == 3):
    estrutura = Fila.CoviList()

elif (opt == 4):
    print('''Lista dos dados que irão ser escolhidos para cada árvore:
    0-Somente a chave
    1-Data da observação
    2-Província (China)
    3-País
    4-Última atualização
    5-Casos Confirmados
    6-Número de mortos
    7-Número de recuperados
    ''')

    estrutura1 = Arvore.CoviList(int(input("Escolha uma opção para a primeira árvore: ")))
    estrutura2 = Arvore.CoviList(int(input("Escolha uma opção para a segunda árvore: ")))
    estrutura3 = Arvore.CoviList(int(input("Escolha uma opção para a terceira árvore: ")))

#lê o arquivo que contem os dados e coloca numa variavel
data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)

#cria um array com 11000 numeros, os misturando depois
aux = list(range(len(data)))
random.shuffle(aux)  
x = 0

#faz o processo de criar uma nova struct, armazena dentro dela os dados de uma certa linha aleatória
#de acordo com o array de numeros e os insere na lista, isso 100 vezes
if (opt != 4):
    while (x < 100):
        dado = Struct.CovidLine(*data.loc[aux[x]])

        estrutura.inserir(dado)

        x += 1
    
    dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

    while(dig != 1 and dig != 2):
        dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

    if dig == 1:    
        estrutura.visualizar()

    elif dig == 2:   
        outf = open("saida.txt", "w")
        estrutura.escrever(outf)

else:
    while (x < 100):
        dado = Struct.CovidLine(*data.loc[aux[x]])

        estrutura1.inserir(dado)
        estrutura2.inserir(dado)
        estrutura3.inserir(dado)

        x += 1

    dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

    while(dig != 1 and dig != 2):
        dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

    if dig == 1:
        print("Arvore 1:")    
        estrutura1.visualizar()
        print("Arvore 2:")    
        estrutura2.visualizar()
        print("Arvore 3:")    
        estrutura3.visualizar()

    elif dig == 2:   
        outf = open("saida1.txt", "w")
        estrutura1.escrever(outf)
        outf = open("saida2.txt", "w")
        estrutura2.escrever(outf)
        outf = open("saida3.txt", "w")
        estrutura3.escrever(outf)