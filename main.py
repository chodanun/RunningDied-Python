import pygame
from pygame.locals import *
from gamelib import SimpleGame

class SquashGame(SimpleGame):

	def __init__(self):
		super(SquashGame,self).__init__("SquashGame")

	def init(self):
		super(SquashGame, self).init()


def main():
		game = SquashGame()
		game.run()
 
if __name__ == '__main__':
	main()
