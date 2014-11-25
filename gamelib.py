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
			self.handle_event_push()
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

	def handle_event_push(self):
		if self.is_key_pressed(K_UP):
			if ( self.player_1.getY() >= 300):
				self.player_1.Jump()
		if self.is_key_pressed(K_LEFT):
			if (self.player_1.getX()>= 350 ):
				self.player_1.moveLeft()
		if self.is_key_pressed(K_RIGHT):
			if (self.player_1.getX() <= 640-90 ):
				self.player_1.moveRight()

		if self.is_key_pressed(K_w):
			if ( self.player_2.getY() >= 300):
				self.player_2.Jump()
		if self.is_key_pressed(K_a):
			if ( self.player_2.getX() >= -10):
				self.player_2.moveLeft()
		if self.is_key_pressed(K_d):
			if ( self.player_2.getX() <= 200):
				self.player_2.moveRight()

	def init(self):
		self.__game_init()

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)

	def is_key_pressed(self, key):
		keys_pressed = pygame.key.get_pressed()
		if key < 0 or key >= len(keys_pressed):
			return False
		return (keys_pressed[key])


	def update(self):
		pass

	def render(self,surface):
		pass


