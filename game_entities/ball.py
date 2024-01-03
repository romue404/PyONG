import pygame
import math
import random
from constants import BALL_COLOR, BALL_RADIUS, BALL_SPEED, PITCH_WIDTH, PITCH_HEIGHT


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.reset()
    
    def reset(self):
        self.rect = self.image.get_rect()
        self.rect.center = (PITCH_WIDTH//2, PITCH_HEIGHT//2)
        angle = random.uniform(math.radians(0), math.radians(65))
        x, y = math.cos(angle), math.sin(angle)
        self.speed_x = BALL_SPEED * x * random.choice([-1, 1])
        self.speed_y = BALL_SPEED * y * random.choice([-1, 1])

    def normalize_pos(self):
        magnitude = self.rect.left**2 + self.rect.top**2
        return self.rect.left/magnitude, self.rect.top/magnitude

    def reflect(self, normal, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self.rect, k):
                setattr(self.rect, k, v)
            else:
                print('the ball\'s rect has no attribute {}'.format(k))
        x, y = normal
        if x == 1:
            self.speed_x *= -1
        if y == 1:
            self.speed_y *= -1
            
    def draw(self, surface):
        pygame.draw.ellipse(self.image, BALL_COLOR, [0, 0, BALL_RADIUS*2, BALL_RADIUS*2])
        surface.blit(self.image, self.rect)

    def update(self, time_passed):
        self.rect.left += int(time_passed * self.speed_x)
        self.rect.top  += int(time_passed * self.speed_y)
        return self
