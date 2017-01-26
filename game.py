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

    def draw(self, time_passed):
        """
        draw all game entities,
        the order of execution is curcial
        """
        self.pitch.draw(self.game_surface)
        self.bar_left.draw(self.game_surface)
        self.bar_right.draw(self.game_surface)
        self.ball.draw(self.game_surface)
        self.score.draw(self.game_surface)

    def event_queue(self, time_passed):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.bar_left.move_up(time_passed)
        if pressed[pygame.K_DOWN]:
            self.bar_left.move_down(time_passed)
        if pressed[pygame.K_w]:
            self.bar_right.move_up(time_passed)
        if pressed[pygame.K_s]:
            self.bar_right.move_down(time_passed)

    def run(self):
        pygame.init()
        running = True
        clock = pygame.time.Clock()
        self.game_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        """======GAME LOOP====="""
        while running:
            time_passed = clock.tick(60) / 1000.0
            """======INPUTS====="""
            self.event_queue(time_passed)
            """======UPDATE===="""
            self.ball.update(time_passed)
            """=====RULES====="""
            if self.ball.rect.top >= WINDOW_HEIGHT or self.ball.rect.top <=0:
                self.ball.reflect((0, 1))
            if self.ball.rect.left <= 0:
                self.ball.reflect((1, 0))
                self.score.away_scored()
            if self.ball.rect.right >= WINDOW_WIDTH:
                self.ball.reflect((1, 0))
                self.score.home_scored()
            if self.ball.y >= self.bar_left.rect.top and \
                self.ball.y <= self.bar_left.rect.bottom:
                print 'in y'
            """======DRAW FRAME====="""
            self.draw(time_passed)
            pygame.display.update()
