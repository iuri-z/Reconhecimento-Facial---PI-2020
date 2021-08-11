import pygame

arquivoVolume = open('volume.txt', 'r')

vol = int(arquivoVolume.read())

# Som para quando o rosto da pessoa for reconhecido pelo software
def getAlerta():
	pygame.mixer.init()
	pygame.mixer.music.set_volume(vol/100)
	pygame.mixer.music.load("audios/alerta_sonoro.mp3")
	pygame.mixer.music.play(loops = 0) 	#eh necessario sempre setar a quantidade de loops
									   	#neste caso zero, para nao haver repetições