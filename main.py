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
            janela_lista()

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
                aux2 = sg.popup_get_text(message=texto, title="Digite uma chave da árvore {0}:".format(i+1))

                while (aux2 == None or aux2.isnumeric() == False or not(int(aux2) in range(8)) ):
                    aux2 = sg.popup_get_text(message=texto, title="Digite uma chave da árvore {0}:".format(i+1))
                
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
            win.close()
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

class janela_lista():
    def __init__(self):
        layout = [ [sg.Button('Adicionar novo dado'), sg.Button('Remover algum dado')],
                    [sg.Button('Ver dados')], 
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Opções', layout)

        event, value = win.read()
        print(event)
        if (event == 'Ver dados'):
            win.close()
            janela_lista_tel()

        elif (event == 'Adicionar novo dado'):
            pop = sg.popup_get_text(message='Digite a chave nova do dado que vai ser adicionado:')

            if (pop == None):
                win.close()
            else:
                at, prev = estrutura.buscar(int(pop))
                if at:
                    pop_error = sg.popup("A chave digitada já existe")
                else:
                    dado = []
                    dado.append(int(pop))

                    layout = [
                        [sg.Text('Por favor, informe aqui os dados:')],
                        [sg.Text('Data de Observação', size =(30, 1)), sg.InputText()],
                        [sg.Text('Estado da Província (Se for na China)', size =(30, 1)), sg.InputText()],
                        [sg.Text('Região do País', size =(30, 1)), sg.InputText()],
                        [sg.Text('Última Atualização', size =(30, 1)), sg.InputText()],
                        [sg.Text('Casos confirmados', size =(30, 1)), sg.InputText()],
                        [sg.Text('Número de mortos', size =(30, 1)), sg.InputText()],
                        [sg.Text('Números de recuperados', size =(30, 1)), sg.InputText()],
                        [sg.Submit(), sg.Cancel()]
                    ]

                    window_ins = sg.Window('Dados', layout)
                    event,values = window_ins.read()
                    window_ins.close()

                    if (event == 'Cancel'):
                        win.close()
                        janela_lista()

                    for i in values:
                        dado.append(values[i])

                    aux2 = Struct.CovidLine(*dado)

                    for i in values:
                        dado.append(i)

                    estrutura.inserir(aux2)
                
            win.close()
            janela_lista()

        elif (event == 'Remover algum dado'):
            pop = sg.popup_get_text(message='Digite a chave do dado desejado:')

            if (pop == None):
                win.close()
            elif (estrutura.excluir(int(pop)) == False):
                pop_error = sg.popup("A chave digitada não existe")          
            else:
                pop_done = sg.popup("Chave removida com sucesso")   
                
            win.close()
            janela_lista()

        elif(event == 'Exportar para arquivo de texto'):
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)
            sg.popup('Arquivo criado com sucesso!')
            win.close()
            janela_lista()

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela_lista_tel():
    def __init__(self):
        layout = [ [sg.Listbox(estrutura.__str__(), size=(83, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela_lista()

class janela1():
    def __init__(self):
        layout = [ [sg.Button('Adicionar novo dado'), sg.Button('Remover item')],
                    [sg.Button('Ver dados')], 
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Opções', layout)

        event, value = win.read()
        if (event == 'Ver dados'):
            win.close()
            janela1_tel()

        elif (event == 'Adicionar novo dado'):
            dado = []

            layout = [ 
                [sg.Text('Por favor, informe aqui os dados:')],
                [sg.Text('Chave', size =(30, 1)), sg.InputText()],
                [sg.Text('Data de Observação', size =(30, 1)), sg.InputText()], 
                [sg.Text('Estado da Província (Se for na China)', size =(30, 1)), sg.InputText()], 
                [sg.Text('Região do País', size =(30, 1)), sg.InputText()], 
                [sg.Text('Última Atualização', size =(30, 1)), sg.InputText()], 
                [sg.Text('Casos confirmados', size =(30, 1)), sg.InputText()], 
                [sg.Text('Número de mortos', size =(30, 1)), sg.InputText()], 
                [sg.Text('Números de recuperados', size =(30, 1)), sg.InputText()],
                [sg.Submit(), sg.Cancel()]
            ]

            window_ins = sg.Window('Dados', layout)
            event,values = window_ins.read()
            window_ins.close()

            for i in values:
                dado.append(values[i])

            aux2 = Struct.CovidLine(*dado)

            for i in values:
                dado.append(i)

            estrutura.inserir(aux2)
                
            win.close()
            janela1()

        elif (event == 'Remover item'):
            item = estrutura.excluir()
            pop_done = sg.popup("Removido um item 1 item da estrutura")       
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
        layout = [ [sg.Button('Adicionar novo dado'), sg.Button('Remover item')],
                    [sg.Button('Ver árvore 1'), sg.Button('Ver árvore 2'), sg.Button('Ver árvore 3')],
                    [sg.Button('Exportar para arquivo de texto')],
                    [sg.Button('Voltar')] ]

        win = sg.Window('Opções', layout)

        event, value = win.read()
        if (event == 'Ver árvore 1'):
            win.close()
            janela_arvore_tel(1)

        elif (event == 'Ver árvore 2'):
            win.close()
            janela_arvore_tel(2)

        elif (event == 'Ver árvore 3'):
            win.close()
            janela_arvore_tel(3)

        elif (event == 'Adicionar novo dado'):
            popup = sg.popup_get_text('Escolha em qual árvore você deseja adicionar:')
            win.close()
            janela_arvore_ins(int(popup))
            janela_arvore()

        elif (event == 'Remover item'):
            popup = sg.popup_get_text('Escolha em qual árvore você deseja adicionar:')
            win.close()
            janela_arvore_rem(int(popup))
            janela_arvore()

        elif(event == 'Exportar para arquivo de texto'):
            outf = open("saida.txt", "w")
            estrutura.escrever(outf)
            sg.popup('Arquivo criado com sucesso!')
            win.close()
            janela_arvore()

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela_arvore_ins():
    def __init__(self, opcao):
        dado = []

        layout = [ 
            [sg.Text('Por favor, informe aqui os dados:')],
            [sg.Text('Chave', size =(30, 1)), sg.InputText()],
            [sg.Text('Data de Observação', size =(30, 1)), sg.InputText()], 
            [sg.Text('Estado da Província (Se for na China)', size =(30, 1)), sg.InputText()], 
            [sg.Text('Região do País', size =(30, 1)), sg.InputText()], 
            [sg.Text('Última Atualização', size =(30, 1)), sg.InputText()], 
            [sg.Text('Casos confirmados', size =(30, 1)), sg.InputText()], 
            [sg.Text('Número de mortos', size =(30, 1)), sg.InputText()], 
            [sg.Text('Números de recuperados', size =(30, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
    
        window_ins = sg.Window('Dados', layout)
        event,values = window_ins.read()

        print(event)

        if (event == 'Cancel'):
            window_ins.close()
        else:
            for i in values:
                dado.append(values[i])
                
            dado[0] = int(dado[0])

            aux2 = Struct.CovidLine(*dado)

            if (opcao == 1):
                estrutura.inserir(aux2)
            elif (opcao == 2):
                estrutura2.inserir(aux2)
            elif (opcao == 3):
                estrutura3.inserir(aux2)
                
            window_ins.close()

class janela_arvore_rem():
    def __init__(self, opcao):
        popup2 = sg.popup_get_text('Digite a chave do nó a ser removido:') 

        if (opcao == 1):
            if (estrutura.excluir(int(popup2)) == False):
                pop_error = sg.popup('A chave digitada não existe')
            else:
                pop_done = sg.popup('Nó removido com sucesso')
        elif (opcao == 2):
            if (estrutura2.excluir(int(popup2)) == False):
                pop_error = sg.popup('A chave digitada não existe')
            else:
                pop_done = sg.popup('Nó removido com sucesso')
        elif (opcao == 3):
            if (estrutura3.excluir(int(popup2)) == False):
                pop_error = sg.popup('A chave digitada não existe')
            else:
                pop_done = sg.popup('Nó removido com sucesso')


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
            if aux2 == "QUALQUER":
                dis, traj = estrutura.menor_dist(aux1.upper())
            else:
                dis, traj = estrutura.menor_dist(aux1.upper(), aux2.upper())

            if (dis == -1):
                mes = sg.popup(traj)
            else:
                pop = sg.popup(traj, title='Busca')
            
            win.close()
            janela_grafo()

        elif (event == 'Voltar'):
            win.close()
            Main()

        elif(event == sg.WIN_CLOSED):
            win.close()

class janela_grafo_tel():
    def __init__(self):
        layout = [ [sg.Listbox(estrutura.__str__(), size=(45, 20))], [sg.Button('Voltar')] ]

        win = sg.Window('Dados', layout)
        event, value = win.read()

        if(event=='Voltar'):
            win.close()
            janela_grafo()
        elif (event == sg.WIN_CLOSED):
            win.close()

app = Main()
