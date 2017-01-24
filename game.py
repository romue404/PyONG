import pygame, sys
from pygame.locals import *
from constants import *
from game_entities import pitch, bar, ball, score


class Game(object):
    def __init__(self):
        self.pitch = pitch.Pitch()
        self.score = score.Score(0,0)
        self.bar_left = bar.Bar(0)
        self.bar_right = bar.Bar(WINDOW_WIDTH-BAR_WIDTH)
        self.ball = ball.Ball(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    def draw(self):
        """
        draw all game entities,
        the order of execution is curcial
        """
        self.pitch.draw(self.game_surface)
        self.bar_left.draw(self.game_surface)
        self.bar_right.draw(self.game_surface)
        self.ball.draw(self.game_surface)
        self.score.draw(self.game_surface)

    def event_queue(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.bar_left.move_up(BAR_VELOCITY*WINDOW_HEIGHT/FPS)
        if pressed[pygame.K_DOWN]:
            self.bar_left.move_down(BAR_VELOCITY*WINDOW_HEIGHT/FPS)


    def run(self):
        pygame.init()
        running = True
        clock = pygame.time.Clock()
        self.game_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        """======GAME LOOP====="""
        while running:
            """======INPUTS====="""
            self.event_queue()
            """======DRAW FRAME====="""
            self.draw()
            pygame.display.update()
            clock.tick(FPS)
