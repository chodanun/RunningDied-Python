import pygame
from pygame.locals import *

class SimpleGame(object):
	def __init__(self, title, background_color, window_size=(640,480), fps=60):
		self.background_color = background_color
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.is_terminated = False
 
	def run(self):
		self.init()
		while not self.is_terminated :
			self.__handle_events()
			self.update()
			self.render(self.surface)
			pygame.display.update()
			self.clock.tick(self.fps)
			
	def terminate(self):
		self.is_terminated = True

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT :
				self.terminate()    
			elif event.type == KEYDOWN :
				if event.key == K_UP:
					if ( self.player_1.getY() >= 300):
						self.player_1.Jump()	
				if event.key == K_LEFT:
					self.player_1.moveLeft()
				if event.key == K_RIGHT:
					self.player_1.moveRight()
					
				if event.key == K_w:
					if ( self.player_2.getY() >= 300):
						self.player_2.Jump()
				if event.key == K_a:
					self.player_2.moveLeft()
				if event.key == K_d:
					self.player_2.moveRight()

	def init(self):
		self.__game_init()

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)


	def update(self):
		print "gamelib"

	def render(self,surface):
		pass


