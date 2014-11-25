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
		self.first = True
		self.score = 0
		self.score2 = 0 
 
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
		self.check_score()
		self.render_score()
		if (self.score  >= 150 or self.score2 >= 150 ):
			self.terminate()

	def check_score(self):
		if ( self.bomb.getY() >= 400):
			if (self.bomb.getX()>=290):
				self.score += 1
			else :
				self.score2 += 1
			

	def render_score(self):
		self.score_image = self.font.render("Score = %d" % self.score, 0, SquashGame.WHITE)
		self.score_image2 = self.font.render("Score = %d" % self.score2, 0, SquashGame.WHITE)
		

 
	def render(self, surface):
		self.player_1.render(surface)
		self.player_2.render(surface)
		self.bomb.render(surface)
		surface.blit(self.score_image, (10,10))
		surface.blit(self.score_image2, (500,10))

	def check_Collision(self):
		if ( self.bomb.getX() > 290):
			self.check_collision_player1()
		else :
			self.check_collision_player2 ()

	def check_collision_player1(self):
		if ( abs(self.bomb.getY()+60 - self.player_1.getY()) <= 5):
			if ( abs(self.player_1.getX()+50 - (self.bomb.getX()+30)) <= -5):
				self.bomb.inverseVy()
			elif ( 0 < self.player_1.getX()+50 - (self.bomb.getX()+30) <= 50 ):
				if (self.first == True):
					self.bomb.detVx()
					self.first = False 
				self.bomb.inverseVy()
				self.bomb.inverseVx()
			elif ( 0 < abs(self.player_1.getX()+50 - (self.bomb.getX()+30)) <= 50 ):
				if (self.first == True):
					self.bomb.detVx()
					self.first = False 
				self.bomb.inverseVy()
				self.bomb.inverseVx()

	def check_collision_player2 (self):
		if ( abs(self.bomb.getY()+60 - self.player_2.getY()) <= 5):
			if ( abs(self.player_2.getX()+50 - (self.bomb.getX()+30)) <= -5):
				self.bomb.inverseVy()
			elif ( 0 < self.player_2.getX()+50 - (self.bomb.getX()+30) <= 50 ):
				self.bomb.inverseVy()
				self.bomb.inverseVx()
			elif ( 0 < abs(self.player_2.getX()+50 - (self.bomb.getX()+30)) <= 50 ):
				self.bomb.inverseVy()
				self.bomb.inverseVx()
	
# ...
 
def main():
	game = SquashGame()
	game.run()
 
if __name__ == '__main__':
	main()
