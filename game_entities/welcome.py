import pygame, sys
from constants import *
import time
from game_entities.pitch import Pitch

class Welcome(object):
    def __init__(self):
        pass

    def draw(self, screen):
        Pitch.draw_background(screen)
        BASICFONT = pygame.font.Font('freesansbold.ttf', SCORE_SIZE)
        title_text = BASICFONT.render(f'{GAME_NAME}', True, BAR_COLOR)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        instructions_text = BASICFONT.render("Press SPACE to start", True, (200, 200, 255))
        instructions_rect = instructions_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(instructions_text, instructions_rect)

        pygame.display.flip()