import pygame
from pygame.locals import *

class bomb(object):

	def __init__(self):
		self.x = 445
		self.y = 480/8
		self.vx = 0
		self.vy = 3
		self.bomb = pygame.image.load("grenade.png")
		self.time = 0 

	def update(self):
		self.y += self.vy
		self.x += self.vx
		self.handle()
		self.net_collide()
		self.time += 1
		if ( self.vx >= 20):
			self.vx = 2
		self.again()

	def again(self):
		if (self.y >= 480):
			self.x = 180-100
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

	def net_collide(self):
		if self.time >= 100:
			self.time = 0 
			if ( self.y >= 480-190 ):
				if (290-40+20 <= self.x <= 350+40-20):
					if ( self.vx >= 0):
						self.vx = self.vx
					else:
						self.vx = -self.vx

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def inverseVy(self):
		self.vy *= -1	

	def detVx(self):
		self.vx = 2

	def inverseVx(self):
		self.vx *= -1.5




