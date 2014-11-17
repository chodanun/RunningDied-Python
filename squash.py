import pygame
from pygame.locals import *
from practicum import findBoards
from peri import PeriBoard

FPS = 50
WINDOW_SIZE = (500,500)
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
GREY  = pygame.Color('grey')
PLAYER_COLORS = ('green','yellow','red','cyan')
#########################################
class Ball(object):

    def __init__(self, radius=10, color=WHITE,
            pos=(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2), speed=(100,0)):
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

    def draw(self, display):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(display, self.color, pos, self.radius, 0)

#########################################
class Player(object):

    THICKNESS = 10

    def __init__(self,board,pos=WINDOW_SIZE[1]/2, width=100, color=WHITE):
        self.width = width
        self.pos = pos
        self.color = color
	self.board = board
    
    def move(self):
	try:
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

#########################################
def render_score():
    '''Render score into an image for display'''
    global font,score,score_image
    score_image = font.render("Score = %d" % score, 0, GREY)

#########################################
def main():
    global game_over,font,score,score_image

    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Squash')
    game_over = False
    font = pygame.font.SysFont("monospace", 20)
    score = 0
    score_image = None
    render_score()

    ball = Ball(speed=(200,50))
    players = []
    for i,dev in enumerate(findBoards()):
        color = PLAYER_COLORS[i % len(PLAYER_COLORS)]
        board = PeriBoard(dev)
	players.append(Player(board,color=pygame.Color(color),pos=100,width=150))
	print "Player#%d (%s): %s" % (i+1, color, board.getDeviceName())
    
    while not game_over:
        for event in pygame.event.get(): # process events
            if (event.type == QUIT) or \
               (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_over = True


        display.fill(BLACK)  # clear screen
        display.blit(score_image, (10,10))  # draw score
        for p in players:
		p.move() # move player
		p.draw(display) # draw playeer

	ball.move(1./FPS, display, players)  # move ball
        ball.draw(display)  # draw ball

        pygame.display.update()  # redraw the screen
        clock.tick(FPS)  # wait to limit FPS requirement

#########################################
if __name__=='__main__':
    main()
    print "Game Over! Total score is %d." % score
    pygame.quit()
