import pygame
from pygame.locals import *
from gamelib import SimpleGame
from player import player

class SquashGame(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
 
	def __init__(self):
		super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
 
	def init (self):
		super(SquashGame, self).init()
		self.init_Bg()
		self.init_Player()
		self.init_Bomp()

	def init_Bg (self):
		self.bg = pygame.image.load("bg2.png")
		self.surface.blit(self.bg,(0,0))

	def init_Player(self):
		self.player_1 = player("boy_right.png",445,300)
		self.player_2 = player("boy_left.png",95,300)
		
	def init_Bomp(self):
		bomp = pygame.image.load("grenade.png")
		self.surface.blit(bomp,(445,480/8))

	def update(self):
		self.surface.blit(self.bg,(0,0))
		self.player_1.update()
		self.player_2.update()

		# ... update the position
 
	def render(self, surface):
		self.player_1.render(surface)
		self.player_2.render(surface)
		
 
	# ...
 
def main():
	game = SquashGame()
	game.run()
 
if __name__ == '__main__':
	main()
