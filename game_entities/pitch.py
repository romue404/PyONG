import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUND_COLOR

class Pitch(object):

    def draw(self, surface):
        pygame.draw.rect(surface, BACKGROUND_COLOR, ((0,0), (WINDOW_WIDTH, WINDOW_HEIGHT)))