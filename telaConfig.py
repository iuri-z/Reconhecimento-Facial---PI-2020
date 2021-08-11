# -- coding: utf-8 --
from tkinter import *
#import alerta_sonoro
import pygame
import os

#criando a tela
root = Tk(className=' Configurações')
root.resizable(0,0)
canvas = Canvas(root, width=400, height=250)
canvas.grid(columnspan=5,rowspan=16)

#variavel global para volume
volume = 0

arquivoVolume = open('volume.txt', 'w')

#definindo as funções
def onBotVoltar():
    arquivoVolume.write(str(slider.get()))
    arquivoVolume.close()
    quit()

def mouseEmcimaA(e):
    botVoltar['background'] = 'gray'

def mouseFora(e):
    botVoltar['background'] = 'black'

def getVolValue(x):
    #alerta_sonoro.setPoint(slider.get())
    return slider.get()

#criando botões e textos
botVoltar = Button(root, text='Voltar', font=('Raleway', 10, 'bold'), fg="white", bg="black", borderwidth=0, height=2, width=15, command=onBotVoltar)

labConfig = Label(root, text='Configurações', font=('Raleway', 12, 'bold'), anchor='w')
labVolume = Label(root, text='volume', font=('Raleway', 10, 'bold'), anchor='w')
labScale = Label(root, text='................................................................... ', fg="white", anchor='w')

slider = Scale(root, from_=0, to=100, orient='horizontal', command=getVolValue, width = 50)

varUm = IntVar()
varDois = IntVar()

#posicionando botões e textos
botVoltar.grid(row=14, column=1)

botVoltar.bind("<Enter>", mouseEmcimaA)

botVoltar.bind("<Leave>", mouseFora)

labConfig.grid(row=2, column=1)
labVolume.grid(row=5, column=1)
labScale.grid(row=5, column=2)

slider.grid(row=6, column=2)

def roda():
    root.mainloop()