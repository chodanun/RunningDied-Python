import pygame
from pygame.locals import *
import sys

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

class Draw(object):


    def update(self, screen):
        color = (0,0,0)
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            color = RED
        if key[pygame.K_g]:
            color = BLUE
        if key[pygame.K_b]:
            color = GREEN
        if key[pygame.K_w]:
            color = WHITE

        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (color), (mouse_pos),30)


    def main(self):

        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Basic Pygame program')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                     sys.exit()
            self.update(screen)
            pygame.display.flip()


if __name__ == '__main__':
    draw = Draw()
    draw.main()