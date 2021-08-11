from tkinter import *
import pygame

root = Tk()
root.title('Codemy.com')
root.geometry("500x400")

pygame.mixer.init()

def play():
	pygame.mixer.music.load("AlertaSonoro.mp3")
	pygame.mixer.music.play(loops=0)

my_button = Button(root, text="Play", command=play)
my_button.pack(pady=20)

root.mainloop()	