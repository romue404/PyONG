import pygame, sys
from pygame.locals import *
from constants import *
from game_entities import pitch, bar, ball


class Game(object):
    def __init__(self):
        self.pitch = pitch.Pitch()
        self.bar_left = bar.Bar(0)
        self.bar_right = bar.Bar(WINDOW_WIDTH-BAR_WIDTH)
        self.ball = ball.Ball(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

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
            self.bar_left.draw(game_surface)
            self.bar_right.draw(game_surface)
            self.ball.draw(game_surface)
            pygame.display.update()
            clock.tick(FPS)