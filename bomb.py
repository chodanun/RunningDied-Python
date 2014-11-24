import pygame
from pygame.locals import *

class bomp (object):
	def __init__(self,loc,posX,posY):
		self.x = posX
		self.y = posY
		self.vx = 5
		self.vy = 2
		self.bomb = pygame.image.load("grenade.png")

	def update(self):
		pass

	def render(self,surface):
		surface.blit(self.bomb,(self.x,self.y))




		
		
		