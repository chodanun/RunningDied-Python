import pygame
from pygame.locals import *

class player(object):
	def __init__(self,loc,posX,posY): 
		self.x = posX
		self.y = posY
		self.vy = 0
		self.player = pygame.image.load(loc)

	def update(self):
		self.y -= self.vy 
		if (self.y < 300):
			self.vy -= 0.1
		if (self.y >= 300):
			self.y = 300
			self.vy = 0

	def moveRight(self):
		self.x += 5

	def moveLeft(self):
		self.x -= 5

	def Jump(self):
		self.vy = 7

	def getY(self):
		return self.y

	def render(self,surface):
		surface.blit(self.player,(self.x,self.y))
