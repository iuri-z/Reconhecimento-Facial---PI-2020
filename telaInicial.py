# -*- coding: utf-8 -*-
from tkinter import *
import os


#Criando a tela
root = Tk(className='Reconhecimento Facial - Tela Inicial')
canvas = Canvas(root, width=400, height=400)
canvas.grid(columnspan=5,rowspan=9)


#Criando as funções para cada botão
def onBotIniciar():
	os.system('python detect_mask_video.py')

def onBotConfig():
	os.system('python config.py')

def onBotSair():
	quit()


#Criando os botões 'Iniciar', 'Configurações' e 'Sair'
bot1 = Button(root, text="Iniciar", font="Stark", borderwidth=0,	width=15, command=onBotIniciar) 
bot2 = Button(root, text="Configurações", font="Stark", borderwidth=0, width=15, command=onBotConfig) 
bot3 = Button(root, text="Sair", font="Stark", borderwidth=0, width=15, command=onBotSair)

	
#Posicionando os botões na tela
bot1.grid(row=3, column=2)
bot2.grid(row=4, column=2)
bot3.grid(row=5, column=2)


#Rodando o software
root.mainloop()