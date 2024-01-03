import pygame, sys
from pygame.locals import *
from constants import WINDOW_WIDTH, SCORE_SIZE, BAR_COLOR, BALL_COLOR, BORDER_SIZE


class Score(object):
    def __init__(self, home=0, away=0):
        self.home = home
        self.away = away

    def draw(self, surface):
        BASICFONT = pygame.font.Font('freesansbold.ttf', SCORE_SIZE)
        resultSurf = BASICFONT.render(f'{self.home}     {self.away}', True, BALL_COLOR)
        resultRect = resultSurf.get_rect()
        resultRect.center = (WINDOW_WIDTH/2, 0)
        resultRect.top = BORDER_SIZE + 10
        surface.blit(resultSurf, resultRect)

    def home_scored(self):
        self.home += 1

    def away_scored(self):
        self.away += 1