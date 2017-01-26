import pygame
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY, BALL_VELOCITY_MAX
from math import acos, cos, sin, pi

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = BALL_VELOCITY_MAX
        self.speed_y = BALL_VELOCITY_MAX-100
        self.velocity_x = 1
        self.velocity_y = 1

    def normalize_pos(self):
        magnitude = self.x**2 + self.y**2
        return self.x/magnitude,self.y/magnitude

    def hit_wall(self, normal):
        #x_, y_ = self.normalize_pos()
        #angle = acos(x_) * (180/pi)
        x,y = normal
        if x == 1:
            self.speed_x *= -1
        if y == 1:
            self.speed_y *= -1

        #print angle


    def draw(self, surface):
        pygame.draw.circle(surface, BALL_COLOR, (self.x, self.y), BALL_RADIUS)

    def update(self, time_passed):
        #self.velocity_x += time_passed * BALL_VELOCITY
        #self.velocity_y += time_passed * BALL_VELOCITY
        #self.velocity_x = self.velocity_x if self.velocity_x < BALL_VELOCITY_MAX * time_passed \
            #else BALL_VELOCITY_MAX * time_passed
        #self.velocity_y = self.velocity_y if self.velocity_y < BALL_VELOCITY_MAX * time_passed \
            #else BALL_VELOCITY_MAX * time_passed
        #self.x += self.velocity_x
        #self.y += self.velocity_y
        #self.x = int(self.x)
        #self.y = int(self.y)
        self.x += int(time_passed * self.speed_x)
        self.y += int(time_passed * self.speed_y)
        return self
