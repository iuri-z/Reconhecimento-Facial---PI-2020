# -*- coding: utf-8 -*-
from tkinter import *
import os

#criando a tela
root = Tk(className='Reconhecimento Facial - Configurações')
canvas = Canvas(root, width=400, height=400)
canvas.grid(columnspan=5,rowspan=18)

#definindo as funções
def onBotVoltar():
    os.system('telaInicial.py')
    quit()

def onBotSalvar():
    quit()


#criando botões e textos
botVoltar = Button(root, text='Voltar', font=('Stark', 10), borderwidth=0, width=15, command=onBotVoltar)
botSalvar = Button(root, text='Salvar', font=('Stark', 10), borderwidth=0, width=15, command=onBotSalvar)

labConfig = Label(root, text='Configurações', font=('Stark', 16))
labVolume = Label(root, text='volume', font=('Stark', 10))
labAlerta = Label(root, text='alerta', font=('Stark', 10))


#posicionando botões e textos
botVoltar.grid(row=16, column=1)
botSalvar.grid(row=16, column=2)


labConfig.grid(row=2, column=1)
labVolume.grid(row=4, column=1)
labAlerta.grid(row=5, column=1)

root.mainloop()
