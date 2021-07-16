# -*- coding: utf-8 -*-
from tkinter import *
import os

#criando a tela
root = Tk(className=' Configurações')
root.resizable(0,0)
canvas = Canvas(root, width=400, height=400)
canvas.grid(columnspan=5,rowspan=18)

#definindo as funções
def onBotVoltar():
    quit()

def onBotSalvar():
    quit()

def mouseEmcimaA(e):
    botVoltar['background'] = 'gray'

def mouseEmcimaB(e):
    botSalvar['background'] = 'gray'

def mouseFora(e):
    botVoltar['background'] = 'black'
    botSalvar['background'] = 'black'

#criando botões e textos
botVoltar = Button(root, text='Voltar', font=('Raleway', 10, 'bold'), fg="white", bg="black", borderwidth=0, width=15, command=onBotVoltar)
botSalvar = Button(root, text='Salvar', font=('Raleway', 10, 'bold'), fg="white", bg="black", borderwidth=0, width=15, command=onBotSalvar)

labConfig = Label(root, text='Configurações', font=('Raleway', 12, 'bold'), anchor='w')
labVolume = Label(root, text='volume', font=('Raleway', 10, 'bold'), anchor='w')
labAlerta = Label(root, text='alerta', font=('Raleway', 10, 'bold'), anchor='w')

slider = Scale(root, from_=0, to=100, orient='horizontal')

varUm = IntVar()
varDois = IntVar()

checkSom = Checkbutton(root, text="Som", font=('Raleway', 10), variable=varUm)
checkImg = Checkbutton(root, text="Visual", font=('Raleway', 10), variable=varDois)

#posicionando botões e textos
botVoltar.grid(row=16, column=1)
botSalvar.grid(row=16, column=2)

botVoltar.bind("<Enter>", mouseEmcimaA)
botSalvar.bind("<Enter>", mouseEmcimaB)

botVoltar.bind("<Leave>", mouseFora)
botSalvar.bind("<Leave>", mouseFora)

labConfig.grid(row=2, column=1)
labVolume.grid(row=4, column=1)
labAlerta.grid(row=5, column=1)

slider.grid(row=4, column=2)

checkSom.grid(row=5, column=2)
checkImg.grid(row=5, column=2, padx=(120, 0))

root.mainloop()
