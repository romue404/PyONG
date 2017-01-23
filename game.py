import pygame, sys
from pygame.locals import *
from constants import *


class Game(object):

    def event_queue(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        pygame.init()
        running = True
        clock = pygame.time.Clock()
        game_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_NAME)

        while running:
            self.event_queue()
            pygame.display.update()
            clock.tick(FPS)