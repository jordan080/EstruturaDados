import PySimpleGUI as sg
import Struct
import ListaDinamica
import Pilha
import Fila
import Arvore
import pandas as pd
import random

estrutura = None
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
            estrutura = Arvore.CoviList()
            x = 0
            while (x < 100):
                dado = Struct.CovidLine(*data.loc[aux[x]])
                estrutura.inserir(dado)
                x += 1
            win.close()
            janela1()

class janela1():
    def __init__(self):
        layout = [ [sg.Button('Ver dados')],
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Lista', layout)

        event, value = win.read()
        if (event == 'Ver dados'):
            win.close()
            janela1_tel()

        elif(event == 'Exportar para arquivo de texto'):
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)
            sg.popup('Arquivo criado com sucesso!')

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

app = Main()
