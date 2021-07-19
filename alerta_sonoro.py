import pygame
#import telaConfig.getVolValue

# Som para quando o rosto da pessoa for reconhecido pelo software
def getAlerta():
	pygame.mixer.init()
	#pygame.mixer.music.set_volume(telaConfig.getVolValue())
	pygame.mixer.music.load("audios/alerta_sonoro.mp3")
	pygame.mixer.music.play(loops = 0) 	#eh necessario sempre setar a quantidade de loops
									   	#neste caso zero, para nao haver repetições

# Som para quando a pessoa passa o mouse emcima de algum botão
def getSomMouseOn():
	pygame.mixer.init()
	pygame.mixer.music.set_volume(0.2)
	pygame.mixer.music.load("audios/alerta_click.mp3")
	pygame.mixer.music.play(loops = 0)