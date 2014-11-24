import pygame
from pygame.locals import *
from gamelib import SimpleGame

class SquashGame(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
 
	def __init__(self):
		super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
		# .... init something here
 
	def init (self):
		super(SquashGame, self).init()
		self.init_Bg()	
		self.init_Players()
		self.init_Bomp()

	def init_Bg (self):
		bg = pygame.image.load("bg2.png")
		self.surface.blit(bg,(0,0))

	def init_Players(self):
		player_1 = pygame.image.load("boy_right.png")
		player_2 = pygame.image.load("boy_left.png")
		self.surface.blit(player_1,(445,300))
		self.surface.blit(player_2,(95,300))

	def init_Bomp(self):
		bomp = pygame.image.load("grenade.png")
		self.surface.blit(bomp,(445,480/8))

	def update(self):
		pass
		# ... update the position
 
	def render(self, surface):
		pass
		# ... draw something
 
	# ...
 
def main():
	game = SquashGame()
	game.run()
 
if __name__ == '__main__':
	main()
