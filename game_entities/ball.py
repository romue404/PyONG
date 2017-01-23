import pygame
from constants import BALL_COLOR, BALL_RADIUS

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.circle(surface, BALL_COLOR, (self.x, self.y), BALL_RADIUS)