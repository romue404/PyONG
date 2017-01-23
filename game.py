import pygame, sys
from pygame.locals import *
from constants import *
from game_entities import pitch, bar


class Game(object):
    def __init__(self):
        self.pitch = pitch.Pitch()
        self.bar = bar.Bar(0)
        self.bar_ = bar.Bar(WINDOW_WIDTH-BAR_WIDTH)

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

        """======GAME LOOP====="""
        while running:
            """======INPUTS====="""
            self.event_queue()
            """======DRAW FRAME====="""
            self.pitch.draw(game_surface)
            self.bar.draw(game_surface)
            self.bar_.draw(game_surface)
            pygame.display.update()
            clock.tick(FPS)