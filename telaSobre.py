from tkinter import * # GUI nativo do python
from PIL import ImageTk, Image

# Criando e configurando a tela
root = Tk(className=' Sobre')
root.resizable(0,0)

canvas = Canvas(root, width=200, height=200)
canvas.grid(columnspan=5,rowspan=16)

img_logo = Image.open("imagens/Logo_IFSC.png")
resize_logo = img_logo.resize((300,300), Image.ANTIALIAS)
get_logo = ImageTk.PhotoImage(resize_logo)
logo = Label(root, image=get_logo)

label = Label(root, text = "Desenvolvedora Face Mask Detection: Chandrika Deb. \nhttps://github.com/chandrikadeb7/Face-Mask-Detection\n\n Este projeto foi elaborado pelos alunos do Instituto Federal de Santa Catarina.\n\nDesenvolvedores: \nAdriel Antunes; Iuri Zimmermann; \nMatheus Sena; Oliver Alexander.", 
	justify=LEFT, padx=50, pady=50)
label.grid(column=1,row=10)
logo.grid(column=1, row=9)

icon = PhotoImage(file='imagens/logo_sobre.png')
root.iconphoto(False, icon)

root.mainloop()