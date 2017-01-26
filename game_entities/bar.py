import pygame
from constants import BAR_COLOR, BAR_WIDTH, BAR_HEIGHT, WINDOW_HEIGHT, BAR_VELOCITY


class Bar(pygame.sprite.Sprite):

    def __init__(self, x_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BAR_WIDTH, BAR_HEIGHT))
        self.image.fill(BAR_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos,0)

    def draw(self, surface):
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0
        surface.blit(self.image, self.rect)

    def move_up(self, time_passed):
        self.rect.top -= time_passed * BAR_VELOCITY
        return self

    def move_down(self, time_passed):
        self.rect.bottom += time_passed * BAR_VELOCITY
        return self
