import Struct
import ListaDinamica
import Pilha
import Fila
import pandas as pd
import random

opt = int(input('''Escolha uma opção para como deseja estruturar seus dados:
1-Lista Dinâmica
2-Pilha
3-Fila
4-Árvore
Opção: '''))

if (opt == 1):
    estrutura = ListaDinamica.CoviList()

if (opt == 2):
    estrutura = Pilha.CoviList()

if (opt == 3):
    estrutura = Fila.CoviList()

#lê o arquivo que contem os dados e coloca numa variavel
data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)

#cria um array com 11000 numeros, os misturando depois
aux = list(range(len(data)))
random.shuffle(aux)  
x = 0

#faz o processo de criar uma nova struct, armazena dentro dela os dados de uma certa linha aleatória
#de acordo com o array de numeros e os insere na lista, isso 100 vezes
while (x < 100):
    dado = Struct.CovidLine(*data.loc[aux[x]])

    estrutura.inserir(dado)

    x += 1

#no final, ele pergunta o usuario se deseja imprimir no terminal ou exportar para um arquivo de texto
dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

while(dig != 1 and dig != 2):
    dig = int(input("Digite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto: "))

if dig == 1:    
    estrutura.visualizar()

elif dig == 2:   
    outf = open("saida.txt", "w")
    estrutura.escrever(outf)