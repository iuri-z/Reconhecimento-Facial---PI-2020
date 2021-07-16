import pygame
#import telaConfig.getVolValue

def getSound():
	pygame.mixer.init() #aqui é onde inicializa o mixer
	#pygame.mixer.music.set_volume(telaConfig.getVolValue())
	pygame.mixer.music.load("AlertaSonoro.mp3")
	pygame.mixer.music.play(loops = 0)