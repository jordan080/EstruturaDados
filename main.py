import Struct
import ListaDinamica
import Pilha
import Fila
import Arvore
import pandas as pd
import random

opt = int(input('''\033[1;37mEscolha uma opção para como deseja estruturar seus dados:
    1-Lista Dinâmica
    2-Pilha
    3-Fila
    4-Árvore
    5-Sair do programa
Opção:\033[m '''))
while(opt not in range(1, 6)):
    print("\033[1;31mOPÇÃO INVALIDA\033[0m")
    opt = int(input('''\033[1;37mEscolha uma opção para como deseja estruturar seus dados:
    1-Lista Dinâmica
    2-Pilha
    3-Fila
    4-Árvore
    5-Sair do programa
Opção:\033[m '''))

while(opt != 5):
    if (opt == 1):
        estrutura = ListaDinamica.CoviList()

    elif (opt == 2):
        estrutura = Pilha.CoviList()

    elif (opt == 3):
        estrutura = Fila.CoviList()

    elif (opt == 4):
        print('''\033[1;37mEscolha a lista dos dados que irão ser escolhidos para cada árvore:
0-Somente a chave
1-Data da observação
2-Província (China)
3-País
4-Última atualização
5-Casos Confirmados
6-Número de mortos
7-Número de recuperados\033[m''')

        estrutura1 = Arvore.CoviList(int(input("\033[1;37mEscolha uma opção para a primeira árvore:\033[m ")))
        estrutura2 = Arvore.CoviList(int(input("\033[1;37mEscolha uma opção para a segunda árvore:\033[m ")))
        estrutura3 = Arvore.CoviList(int(input("\033[1;37mEscolha uma opção para a terceira árvore:\033[m ")))

    else:
        break

    # lê o arquivo que contem os dados e coloca numa variavel
    data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)

    # cria um array com 11000 numeros, os misturando depois
    aux = list(range(len(data)))
    random.shuffle(aux)  
    x = 0

    # faz o processo de criar uma nova struct, armazena dentro dela os dados de uma certa linha aleatória
    # de acordo com o array de numeros e os insere na lista, isso 100 vezes
    if opt == 1 or opt == 2:
        print("\033[1;33mEstrutura lida com sucesso!\033[0m")
        while (x < 100):
            dado = Struct.CovidLine(*data.loc[aux[x]])

            estrutura.inserir(dado)

            x += 1
        
        dig = int(input('''\033[1;37mDigite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto 
Opção:\033[m '''))
        while(dig != 1 and dig != 2):
            print("\033[1;31mOPÇÃO INVALIDA\033[0m")
            dig = int(input('''\033[1;37mDigite 1 para visualizar no terminal ou 2 para exportar para um arquivo de texto 
Opção:\033[m '''))

        if dig == 1:  
            print("\033[1;35m")  
            estrutura.visualizar()
            print("\033[m") 

        elif dig == 2:   
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)

    elif opt == 3:
        while (x < 100):
            dado = Struct.CovidLine(*data.loc[aux[x]])

            estrutura.inserir(dado)

            x += 1

        print("\033[1;33mEstrutura lida com sucesso!\033[0m")
        dig = int(input('''\033[1;37mEscolha uma opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da fila
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))
        while(dig not in range(1, 6)):
            print("\033[1;31mOPÇÃO INVALIDA\033[0m")
            dig = int(input('''\033[1;37mEscolha uma opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da fila
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))
        while dig != 4:
            if dig == 1:  
                print("\033[1;35m")  
                estrutura.visualizar()
                print("\033[m") 

            elif dig == 2:   
                outf = open("saida.txt", "w")
                estrutura.escrever(outf)
                print("passou dig 2")

            elif dig == 3:
                estrutura.excluir()
                print("\033[1;33mO primeiro valor da fila foi apagado! Visualize a fila para conferir!\033[0m")

            elif dig == 5:
                opt = 5
                break

            dig = int(input('''\033[1;37mEscolha uma nova opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da fila
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))
            while(dig not in range(1, 6)):
                print("\033[1;31mOPÇÃO INVALIDA\033[0m")
                dig = int(input('''\033[1;37mEscolha uma opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da fila
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))
###########################################################################################################
    else:
        print("\033[1;33mEstruturas lidas com sucesso!\033[0m")
        while (x < 100):
            dado = Struct.CovidLine(*data.loc[aux[x]])

            estrutura1.inserir(dado)
            estrutura2.inserir(dado)
            estrutura3.inserir(dado)

            x += 1
            
        arvores = [estrutura1, estrutura2, estrutura3]

        dig = int(input('''\033[1;37mEscolha uma opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da arvore
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))
        while(dig not in range(1, 6)):
            print("\033[1;31mOPÇÃO INVALIDA\033[0m")
            dig = int(input('''\033[1;37mEscolha uma opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da arvore
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))

        while dig != 4:
            if dig == 1:
                print("\033[1;36mArvore 1:")    
                estrutura1.visualizar()
                print("\033[m")
                print("\033[1;32mArvore 2:")    
                estrutura2.visualizar()
                print("\033[m")
                print("\033[1;33mArvore 3:")    
                estrutura3.visualizar()
                print("\033[m")

            elif dig == 2:   
                outf = open("saida1.txt", "w")
                estrutura1.escrever(outf)
                outf = open("saida2.txt", "w")
                estrutura2.escrever(outf)
                outf = open("saida3.txt", "w")
                estrutura3.escrever(outf)
                print("\033[1;33mAs arvores foram escritas com sucesso! Procure-as na raiz do documento!\033[0m")

            elif dig == 3:
                escolha = int(input('''\033[1;37mEscolha a arvore que terá o valor excluido
Arvore:\033[m '''))

                while escolha not in range(1,4):
                    print("\033[1;31mOPÇÃO INVALIDA\033[0m")
                    escolha = int(input('''\033[1;37mEscolha a arvore que terá o valor excluido
Arvore:\033[m '''))
                
                valor = type(arvores[escolha - 1].raiz.chave)(input('''\033[1;37mDigite a chave do valor da Arvore {0} que deseja excluir 
Valor:\033[m '''.format(escolha)))
                arvores[escolha - 1].excluir(valor)

                print("\033[1;33mValor excluido com sucesso! Visualize a lista para conferir!\033[0m")
                
            elif dig == 5:
                opt = 5
                break
            
            dig = int(input('''\033[1;37mEscolha uma opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da arvore
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))
            while(dig not in range(1, 6)):
                print("\033[1;31mOPÇÃO INVALIDA\033[0m")
                dig = int(input('''\033[1;37mEscolha uma opção:
    1-Visualizar no terminal
    2-Exportar para um arquivo de texto 
    3-Excluir um valor da arvore
    4-Ler novos dados
    5-Sair do programa
Opção:\033[m '''))
    
    if opt != 5:
        opt = int(input('''\033[1;37mEscolha uma opção para como deseja estruturar seus dados:
    1-Lista Dinâmica
    2-Pilha
    3-Fila
    4-Árvore
    5-Sair do programa
Opção:\033[m '''))
        while(opt not in range(1, 6)):
            print("\033[1;31mOPÇÃO INVALIDA\033[0m")
            opt = int(input('''\033[1;37mEscolha uma opção para como deseja estruturar seus dados:
    1-Lista Dinâmica
    2-Pilha
    3-Fila
    4-Árvore
    5-Sair do programa
Opção:\033[m '''))

    else:
        break