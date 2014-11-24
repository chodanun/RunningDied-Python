class Ball(object):

	def __init__(self, radius=10, color=WHITE,pos=(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2), speed=(100,0)):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.radius = radius
		self.color = color

	def move(self, delta_t, display, players):
		global score, game_over
		self.x += self.vx*delta_t
		self.y += self.vy*delta_t

		# player-hitting check
	
	for p in players:
		if p.can_hit(self):
			score+=1
			render_score()
			self.vx = abs(self.vx) # bouce ball back

		# make ball bounce if hitting wall
		if self.x < self.radius:
			self.vx = abs(self.vx)
			game_over = True # game over when ball hits left wall
		if self.y < self.radius:
			self.vy = abs(self.vy)
		if self.x > display.get_width()-self.radius:
			self.vx = -abs(self.vx)
		if self.y > display.get_height()-self.radius:
			self.vy = -abs(self.vy)
class Player(object):

	THICKNESS = 10

	def __init__(self,board,pos=WINDOW_SIZE[1]/2, width=100, color=WHITE):
		self.width = width
		self.pos = pos
		self.color = color
	self.board = board
	
	def move(self):
	try :
		self.pos = 0.1*self.board.getLight()+0.9*self.pos
	except:
		pass	

	def can_hit(self, ball):
		return self.pos-self.width/2.0 < ball.y < self.pos+self.width/2.0 \
			and ball.x-ball.radius < self.THICKNESS

	def draw(self, display):
		pygame.draw.rect(display, self.color, pygame.Rect(
			0,
			self.pos - self.width/2.0,
			self.THICKNESS,
			self.width), 2)
