import pygame
from pygame.locals import *

class bomb(object):

	def __init__(self):
		self.x = 445
		self.y = 480/8
		self.vx = 0
		self.vy = 2
		self.bomb = pygame.image.load("grenade.png")

	def update(self):
		self.y += self.vy
		self.x += self.vx
		self.handle()
		if (self.y >= 480):
			self.y = 0 

	def render(self,surface):
		surface.blit(self.bomb,(self.x,self.y))

	def handle(self):
		if (self.y == 0): 
			self.vy *= -1
		if (self.x <= 0):
			self.vx *= -1
		if (self.x >= 640-60):
			self.vx *= -1

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def inverseVy(self):
		self.vy *= -1	

	def detVx(self):
		self.vx = 2

	def inverseVx(self):
		self.vx *= -1 

