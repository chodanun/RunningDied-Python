import pygame
from pygame.locals import *

class SimpleGame(object):
	def __init__(self, title, window_size=(640,480), fps=60):
		self.title = title
		self.window_size = window_size
		self.fps = fps

	def init(self):
		self.__game_init()

	def run(self):
		self.init()
		while (1) :
			self.update()
			self.render()
			self.clock.tick(self.fps)

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)

	def update(self):
		pass

	def render(self):
		pass


