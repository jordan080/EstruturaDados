import tkinter as tk
import Struct
import ListaDinamica
import Pilha
import Fila
import Arvore
import pandas as pd
import random

class tkinterApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (Main, P1, P2, P3, P4, P5):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class] 

class Main(tk.Frame):
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 

        label = tk.Label(self, text ="Escolha uma opção para como deseja estruturar seus dados:")
        label.grid(row = 0, column = 1, padx = 5, pady = 5)  

        button1 = tk.Button(self, text = "Lista", 
        command = lambda : controller.show_frame(P1))
        button1.grid(row = 1, column = 0, padx = 5, pady = 5)  

        button2 = tk.Button(self, text = "Fila", 
        command = lambda : controller.show_frame(P2))
        button2.grid(row = 1, column = 1, padx = 5, pady = 5) 

        button3 = tk.Button(self, text = "Pilha", 
        command = lambda : controller.show_frame(P3))
        button3.grid(row = 1, column = 2, padx = 5, pady = 5)
        
        button4 = tk.Button(self, text = "Árvore", 
        command = lambda : controller.show_frame(P4))
        button4.grid(row = 2, column = 0, padx = 5, pady = 5)

        button5 = tk.Button(self, text = "Grafo", 
        command = lambda : controller.show_frame(P5))
        button5.grid(row = 2, column = 2, padx = 5, pady = 5)

class P1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Lista")
        label.grid(row = 0, column = 1, padx = 5, pady = 5)  

        estrutura = ListaDinamica.CoviList()
        data = pd.read_csv("./covid_19_data.csv", header=1, na_filter=True, na_values='nan', keep_default_na=False)
        aux = list(range(len(data)))
        random.shuffle(aux)  
        x = 0

        while (x < 100):            
            dado = Struct.CovidLine(*data.loc[aux[x]])
            estrutura.inserir(dado)
            x += 1

        button1 = tk.Button(self, text= "Voltar",
        command = lambda : controller.show_frame(Main))
        button1.grid(row = 3, column = 1, padx = 5, pady = 5)

        button2 = tk.Button(self, text= "Imprimir na tela",
        command = lambda : controller.show_frame(P1).estrutura.visualizar())
        button2.grid(row = 1, column = 1, padx = 5, pady = 5)

        button3 = tk.Button(self, text= "Exportar para arquivo de texto",
        command = lambda : controller.show_frame())
        button3.grid(row = 2, column = 1, padx = 5, pady = 5) 



class P2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Fila")

        button1 = tk.Button(self, text= "Voltar",
        command = lambda : controller.show_frame(Main))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

class P3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Pilha")

        button1 = tk.Button(self, text= "Voltar",
        command = lambda : controller.show_frame(Main))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

class P4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Árvore")

        button1 = tk.Button(self, text= "Voltar",
        command = lambda : controller.show_frame(Main))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

class P5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Grafo")

        button1 = tk.Button(self, text= "Voltar",
        command = lambda : controller.show_frame(Main))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

app = tkinterApp()
app.mainloop()

        