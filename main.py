import pygame
from pygame.locals import *
from gamelib import SimpleGame

class SquashGame(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
 
	def __init__(self):
		super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
		# .... init something here
 
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
