import PySimpleGUI as sg
import Struct
import ListaDinamica
import Pilha
import Fila
import Arvore
import pandas as pd
import random

class Main():
    def __init__(self):
        layout = [ [sg.Button('Lista'), sg.Button('Fila'), sg.Button('Pilha'), sg.Button('Árvore'), sg.Button('Grafo')],
        [sg.Button('Fechar')] ]

        win = sg.Window('Projeto de ED', layout)
        event, value = win.read()

        if (event == sg.WIN_CLOSED or event == 'Fechar'):
            win.close()

        elif (event == "Lista"):
            win.close()
            janela1()

        elif (event == "Fila"):
            win.close()
            janela2()

        elif (event == "Pilha"):
            win.close()
            janela3()

class janela1():
    def __init__(self):
        layout = [ [sg.Button('Ver dados')],
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Lista', layout)
        event, value = win.read()

        estrutura = ListaDinamica.CoviList()
        data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)
        aux = list(range(len(data)))
        random.shuffle(aux)
        x = 0

        while (x < 100):
            dado = Struct.CovidLine(*data.loc[aux[x]])
            estrutura.inserir(dado)
            x += 1

        if (event == 'Ver dados'):
            janela1_tel(estrutura = estrutura)

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
    def __init__(self, estrutura):
        layout = [ [sg.Listbox(estrutura.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela1()

class janela2():
    def __init__(self):
        layout = [ [sg.Button('Ver dados')],
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Fila', layout)
        event, value = win.read()

        estrutura = Fila.CoviList()
        data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)
        aux = list(range(len(data)))
        random.shuffle(aux)
        x = 0

        while (x < 100):
            dado = Struct.CovidLine(*data.loc[aux[x]])
            estrutura.inserir(dado)
            x += 1

        if (event == 'Ver dados'):
            janela2_tel(estrutura = estrutura)

        elif(event == 'Exportar para arquivo de texto'):
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)
            sg.popup('Arquivo criado com sucesso!')

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela2_tel():
    def __init__(self, estrutura):
        layout = [ [sg.Listbox(estrutura.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela2()

class janela3():
    def __init__(self):
        layout = [ [sg.Button('Ver dados')],
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Pilha', layout)
        event, value = win.read()

        estrutura = Pilha.CoviList()
        data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)
        aux = list(range(len(data)))
        random.shuffle(aux)
        x = 0

        while (x < 100):
            dado = Struct.CovidLine(*data.loc[aux[x]])
            estrutura.inserir(dado)
            x += 1

        if (event == 'Ver dados'):
            janela3_tel(estrutura = estrutura)

        elif(event == 'Exportar para arquivo de texto'):
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)
            sg.popup('Arquivo criado com sucesso!')

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela3_tel():
    def __init__(self, estrutura):
        layout = [ [sg.Listbox(estrutura.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela3()

app = Main()
