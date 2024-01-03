import pygame
from constants import (BAR_COLOR, BAR_WIDTH, BAR_HEIGHT, 
                       PITCH_HEIGHT, PITCH_WIDTH, PITCH_TOP, PITCH_LEFT,
                       BAR_VELOCITY)


class Bar(pygame.sprite.Sprite):

    def __init__(self, x_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BAR_WIDTH, BAR_HEIGHT))
        self.image.fill(BAR_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, PITCH_HEIGHT // 2 - BAR_HEIGHT // 2)
        self.current_velocity = 0

    def draw(self, surface):
        if self.rect.bottom >= PITCH_HEIGHT:
            self.rect.bottom = PITCH_HEIGHT
        if self.rect.top <= PITCH_TOP:
            self.rect.top = PITCH_TOP
        surface.blit(self.image, self.rect)

    def move_up(self, time_passed):
        self.rect.top -= time_passed * BAR_VELOCITY
        self.current_velocity = -BAR_VELOCITY
        return self

    def move_down(self, time_passed):
        self.rect.bottom += time_passed * BAR_VELOCITY
        self.current_velocity = BAR_VELOCITY
        return self
    
    def idle(self):
        self.current_velocity = 0

paddle_left  = Bar(PITCH_LEFT)
paddle_right = Bar(PITCH_WIDTH - BAR_WIDTH)