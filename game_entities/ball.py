import pygame
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY, BALL_VELOCITY_MAX
from math import acos, cos, sin, pi


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed_x = BALL_VELOCITY_MAX
        self.speed_y = BALL_VELOCITY_MAX

    def normalize_pos(self):
        magnitude = self.x**2 + self.y**2
        return self.x/magnitude, self.y/magnitude

    def reflect(self, normal, **kwargs):
        #x_, y_ = self.normalize_pos()
        #angle = acos(x_) * (180/pi)
        # print angle
        for k, v in kwargs.iteritems():
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
        self.rect.top += int(time_passed * self.speed_y)
        return self
