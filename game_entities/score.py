import pygame, sys
from pygame.locals import *
from constants import *


class Score(object):
    def __init__(self,home, away):
        self.home = home
        self.away = away

    def draw(self, surface):
        BASICFONT = pygame.font.Font('freesansbold.ttf', SCORE_SIZE)
        resultSurf = BASICFONT.render('{home}      {away}'.format(
            home=self.home, away=self.away),
            True, BAR_COLOR)
        resultRect = resultSurf.get_rect()
        resultRect.center = (WINDOW_WIDTH/2, 30)
        surface.blit(resultSurf, resultRect)

    def home_scored(self):
        self.home += 1

    def away_scored(self):
        self.away += 1