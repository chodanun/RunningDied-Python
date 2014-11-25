import pygame
from pygame.locals import *
from gamelib import SimpleGame
from player import player
from bomb import bomb

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
		self.bomb = bomb()

	def update(self):
		self.surface.blit(self.bg,(0,0))
		self.player_1.update()
		self.player_2.update()
		self.bomb.update()
		self.check_Collision()
		
		# ... update the position
 
	def render(self, surface):
		self.player_1.render(surface)
		self.player_2.render(surface)
		self.bomb.render(surface)

	def check_Collision(self):
		if ( self.bomb.getX() > 290):
			if ( abs(self.bomb.getY()+60 - self.player_1.getY()) <= 2):

				if ( abs(self.player_1.getX()+50 - (self.bomb.getX()+30)) <= 10):
					self.bomb.inverseVy()
				elif ( 0 < self.player_1.getX()+50 - (self.bomb.getX()+30) <= 50 ):
					self.bomb.inverseVy()
					self.bomb.detVx()
					self.bomb.inverseVx()
				elif ( 0 < abs(self.player_1.getX()+50 - (self.bomb.getX()+30)) <= 50 ):
					self.bomb.inverseVy()
					self.bomb.detVx()
		else :
			if ( abs(self.bomb.getY()+60 - self.player_2.getY()) <= 5):

				if ( abs(self.player_1.getX()+50 - (self.bomb.getX()+30)) <= 25):
					pass
				elif ( 0 < self.player_1.getX()+50 - (self.bomb.getX()+30) <= 50 ):
					pass
				elif ( 0 < abs(self.player_1.getX()+50 - (self.bomb.getX()+30)) <= 50 ):
					pass
		
	# ...
 
def main():
	game = SquashGame()
	game.run()
 
if __name__ == '__main__':
	main()
