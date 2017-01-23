import pygame
from constants import BAR_COLOR, BAR_WIDTH, BAR_HEIGHT


class Bar(object):
    def __init__(self, x_pos):
        self.x = x_pos
        self.y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, BAR_COLOR, ((self.x, self.y), (BAR_WIDTH, BAR_HEIGHT)))