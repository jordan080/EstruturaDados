import PySimpleGUI as sg
import Struct
import ListaDinamica
import Pilha
import Fila
import Arvore
import Grafo
import pandas as pd
import random

estrutura = None
estrutura2 = None
estrutura3 = None
data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)
aux = list(range(len(data)))

class Main():
    def __init__(self):
        layout = [ [sg.Button('Lista'), sg.Button('Fila'), sg.Button('Pilha'), sg.Button('Árvore'), sg.Button('Grafo')],
        [sg.Button('Fechar')] ]

        win = sg.Window('Projeto de ED', layout)
        event, value = win.read()
        random.shuffle(aux)
        global estrutura
        global estrutura2
        global estrutura3

        if (event == sg.WIN_CLOSED or event == 'Fechar'):
            win.close()

        elif (event == "Lista"):
            estrutura = ListaDinamica.CoviList()
            x = 0
            while (x < 100):
                dado = Struct.CovidLine(*data.loc[aux[x]])
                estrutura.inserir(dado)
                x += 1
            win.close()
            janela1()

        elif (event == "Fila"):
            estrutura = Fila.CoviList()
            x = 0
            while (x < 100):
                dado = Struct.CovidLine(*data.loc[aux[x]])
                estrutura.inserir(dado)
                x += 1
            win.close()
            janela1()

        elif (event == "Pilha"):
            estrutura = Pilha.CoviList()
            x = 0
            while (x < 100):
                dado = Struct.CovidLine(*data.loc[aux[x]])
                estrutura.inserir(dado)
                x += 1
            win.close()
            janela1()

        elif (event == "Árvore"):
            texto = '''Escolha a lista dos dados que irão ser escolhidos para cada árvore:
0-Somente a chave
1-Data da observação
2-Província (China)
3-País
4-Última atualização
5-Casos Confirmados
6-Número de mortos
7-Número de recuperados
            '''
            for i in range(3):
                aux2 = sg.popup_get_text(message=texto, title='Digite uma chave:')

                while (aux2 == None or aux2.isnumeric() == False or not(int(aux2) in range(8)) ):
                    aux2 = sg.popup_get_text(message=texto, title='Digite uma chave:')
                
                if (i == 0):
                    estrutura = Arvore.CoviList(int(aux2))
                    x = 0
                    while (x < 100):
                        dado = Struct.CovidLine(*data.loc[aux[x]])
                        estrutura.inserir(dado)
                        x += 1
                
                if (i == 1):
                    estrutura2 = Arvore.CoviList(int(aux2))
                    x = 0
                    while (x < 100):
                        dado = Struct.CovidLine(*data.loc[aux[x]])
                        estrutura2.inserir(dado)
                        x += 1

                if (i == 2):
                    estrutura3 = Arvore.CoviList(int(aux2))
                    x = 0
                    while (x < 100):
                        dado = Struct.CovidLine(*data.loc[aux[x]])
                        estrutura3.inserir(dado)
                        x += 1
            janela_arvore()

        elif (event == 'Grafo'):
            estrutura = Grafo.Grafo()

            for node in Struct.starwars["nodes"]:
                estrutura.add_vertice(node)

            for link in Struct.starwars["links"]:
                estrutura.add_aresta(link["source"], link["target"], 10.0 / link["value"])
                estrutura.add_aresta(link["target"], link["source"], 10.0 / link["value"])

            win.close()
            janela_grafo()

class janela1():
    def __init__(self):
        layout = [ [sg.Button('Ver dados')],
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Opções', layout)

        event, value = win.read()
        if (event == 'Ver dados'):
            win.close()
            janela1_tel()

        elif(event == 'Exportar para arquivo de texto'):
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)
            sg.popup('Arquivo criado com sucesso!')
            win.close()
            janela1()

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela1_tel():
    def __init__(self):
        layout = [ [sg.Listbox(estrutura.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela1()


class janela_arvore():
    def __init__(self):
        layout = [ [sg.Button('Ver árvore 1'), sg.Button('Ver árvore 2'), sg.Button('Ver árvore 3')],
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Opções', layout)

        event, value = win.read()
        if (event == 'Ver árvore 1'):
            win.close()
            janela_arvore_tel(1)

        if (event == 'Ver árvore 2'):
            win.close()
            janela_arvore_tel(2)

        if (event == 'Ver árvore 3'):
            win.close()
            janela_arvore_tel(3)

        elif(event == 'Exportar para arquivo de texto'):
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)
            sg.popup('Arquivo criado com sucesso!')
            janela_arvore()

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela_arvore_tel():
    def __init__(self, opcao):
        if opcao == 1:
            layout = [ [sg.Listbox(estrutura.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]
        elif opcao == 2:
            layout = [ [sg.Listbox(estrutura2.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]
        elif opcao == 3:
            layout = [ [sg.Listbox(estrutura3.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela_arvore()

class janela_grafo():
    def __init__(self):
        layout = [ [sg.Button('Ver dados')],
                    [sg.Button('Ver a menor distancia')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Opções', layout)

        event, value = win.read()
        if (event == 'Ver dados'):
            win.close()
            janela_grafo_tel()

        elif(event == 'Ver a menor distancia'):
            aux1 = sg.popup_get_text('Digite o nome do primeiro personagem, em letras maiúsculas', title='Primeiro personagem')
            while (aux1 == None):
                aux1 = sg.popup_get_text('Digite o nome do primeiro personagem', title='Primeiro personagem')

            aux2 = sg.popup_get_text('Digite o nome do segundo personagem', title='Segundo personagem')
            while (aux2 == None):
                aux2 = sg.popup_get_text('Digite o nome do segundo personagem', title='Segundo personagem')

            dis, traj = estrutura.menor_dist(aux1, aux2)
            pop = sg.popup("A distância entre " + aux1 + " e " + aux2 + " é " + str(round(dis, 2)), traj, title='Busca')
            win.close()
            janela_grafo()

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela_grafo_tel():
    def __init__(self):
        layout = [ [sg.Listbox(estrutura.__str__(), size=(180, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela_grafo()

app = Main()
