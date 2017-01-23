import pygame
from constants import BAR_COLOR, BAR_WIDTH, BAR_HEIGHT


class Bar(object):
    def __init__(self, x_pos):
        self.x = x_pos
    def draw(self, surface):
        pygame.draw.rect(surface, BAR_COLOR, ((self.x, 0), (BAR_WIDTH, BAR_HEIGHT)))