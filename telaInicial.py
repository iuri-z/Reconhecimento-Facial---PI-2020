# -*- coding: utf-8 -*-
from tkinter import *
import os
from PIL import ImageTk, Image

#Criando e configurando a tela
root = Tk(className=' Tela Inicial')
root.resizable(0,0)

canvas = Canvas(root, width=600, height=600)
canvas.grid(columnspan=5,rowspan=16)

icon = PhotoImage(file='Imagens/logoPI_v5.png')
root.iconphoto(False, icon)

#Criando as funções para cada botão
def onBotIniciar():
	os.system('python detect_mask_video.py')

def onBotConfig():
	os.system('python telaConfig.py')

def onBotSair():
	quit()


#Criando os botões 'Iniciar', 'Configurações' e 'Sair'
bot1 = Button(root, text="Iniciar", borderwidth=0, height=2, width=15, fg="white", bg="black", font=('Raleway', 10, 'bold'), command=onBotIniciar) 
bot2 = Button(root, text="Configurações", borderwidth=0, height=2, width=15, fg="white", bg="black", font=('Raleway', 10, 'bold'), command=onBotConfig) 
bot3 = Button(root, text="Sair", borderwidth=0, height=2, width=15, fg="white", bg="black", font=('Raleway', 10, 'bold'), command=onBotSair)

#Inserindo a logo
img_logo = Image.open("Imagens/logoPI_v6.png")
resize_logo = img_logo.resize((300,300), Image.ANTIALIAS)
get_logo = ImageTk.PhotoImage(resize_logo)
logo = Label(root, image=get_logo)

#Posicionando o necessário na tela
logo.grid(row=3,column=2)

bot1.grid(row=7, column=2)
bot2.grid(row=8, column=2)
bot3.grid(row=9, column=2)

#Rodando o software
root.mainloop()