# -- coding: utf-8 --
from tkinter import *
import pygame
import os

#criando a tela
root = Tk(className=' Configurações')
root.resizable(0,0)
canvas = Canvas(root, width=400, height=250)
canvas.grid(columnspan=5,rowspan=16)
icon = PhotoImage(file='imagens/logo_config.png')
root.iconphoto(False, icon)

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
    getSomMouseOn()

def mouseFora(e):
    botVoltar['background'] = 'black'

def getVolValue(x):
    return slider.get()

def getSomMouseOn():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load("audios/alerta_click.mp3")
    pygame.mixer.music.play(loops = 0)

#criando botões e textos
botVoltar = Button(root, text='Voltar', font=('Raleway', 10, 'bold'), fg="white", bg="black", borderwidth=0, height=2, width=15, command=onBotVoltar)

labConfig = Label(root, text='Configurações', font=('Raleway', 12, 'bold'), pady=20)
labSlider = Label(root, text='Volume', font=('Raleway', 10, 'bold'))

slider = Scale(root, from_=0, to=100, orient='horizontal', command=getVolValue,
    length=200, cursor='fleur', bd=0, activebackground='black')

#varUm = IntVar()
#varDois = IntVar()

#posicionando botões e textos
botVoltar.grid(row=11, column=2)
botVoltar.bind("<Enter>", mouseEmcimaA)
botVoltar.bind("<Leave>", mouseFora)

labConfig.grid(row=2, column=2)
labSlider.grid(row=5, column=2)

slider.grid(row=6, column=2)

def roda():
    root.mainloop()