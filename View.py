#_*_coding:UTF-8_*_
import Tkinter as tk
import numpy as np
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(padx=10,pady=10)
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Entry(self, font= 18, width = 30)
        self.label.insert(0, 'Nome do Ganhador')
        self.label.grid(padx=5,pady=5)
        self.quitButton = tk.Button(self, text='Sortear',font= 18 ,width = 15, command = self.sortear)
        self.quitButton.grid(padx=2,pady=2)

    def sortear (self):
        self.label.delete(0,'end')
        sorteado = random.choice(li)
        if sorteado in ganhadores:
            try:
                self.sortear()
            except RuntimeError:
                print ("Todas as pessoas foram sorteadas!")
        else:

            ganhadores.append(sorteado)
            self.label.insert(0, "Parabéns: %s " % str(sorteado))
            print (str(ganhadores.index(ganhadores[-1])+1) + "º Prêmio | Ganhador: "+ str(ganhadores[-1]))


print ('*** LISTA DE GANHADORES ***')
li = np.genfromtxt("indicados.txt",delimiter=',',dtype='str')
ganhadores = []
app = Application()
app.master.title('Ganhadores AVON')
app.mainloop()