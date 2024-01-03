import pygame, sys
import pygame.mixer
from pygame.locals import *
from constants import *
from game_entities import pitch, bar, ball, score, welcome
import time

class Game(object):
    def __init__(self):
        self.pitch = pitch.Pitch()
        self.score = score.Score()
        self.bar_left   = bar.paddle_left
        self.bar_right  = bar.paddle_right
        self.ball = ball.Ball()
        self.mixer = pygame.mixer.init()

    def beep_sound(self):
        pygame.mixer.music.load('sounds/beep.ogg')
        pygame.mixer.music.play(0)

    def crash_sound(self):
        pygame.mixer.music.load('sounds/squish.wav')
        pygame.mixer.music.play(0)

    def draw(self, time_passed):
        """
        draw all game entities,
        the order of execution is curcial
        """
        self.pitch.draw(self.game_surface)
        self.bar_left.draw(self.game_surface)
        self.bar_right.draw(self.game_surface)
        self.ball.draw(self.game_surface)
        self.score.draw(self.game_surface)

    def event_queue(self, time_passed):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.bar_left.move_up(time_passed)
        if pressed[pygame.K_DOWN]:
            self.bar_left.move_down(time_passed)
        if pressed[pygame.K_w]:
            self.bar_right.move_up(time_passed)
        if pressed[pygame.K_s]:
            self.bar_right.move_down(time_passed)

    def ball_paddle_collision(self):
        if pygame.sprite.collide_rect(self.bar_left, self.ball):
            self.ball.reflect((1, 0), left=self.bar_left.rect.right)
            self.beep_sound()
        if pygame.sprite.collide_rect(self.bar_right, self.ball):
            self.ball.reflect((1, 0), right=self.bar_right.rect.left)
            self.beep_sound()

    def boundary_collision(self):
        boundary_collision = False
        if self.ball.rect.top >= PITCH_HEIGHT:
            self.ball.reflect((0, 1), bottom=PITCH_HEIGHT)
        if self.ball.rect.top <= PITCH_TOP:
            self.ball.reflect((0, 1), top=PITCH_TOP)
        if self.ball.rect.left <= PITCH_LEFT:
            boundary_collision = True
            self.ball.reflect((1, 0), left=PITCH_LEFT)
            self.crash_sound()
            self.score.away_scored()
        if self.ball.rect.right >= PITCH_WIDTH:
            boundary_collision = True
            self.crash_sound()
            self.ball.reflect((1, 0), right=PITCH_WIDTH)
            self.score.home_scored()
        return boundary_collision

    def run(self):
        pygame.init()
        running = False
        self.game_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        """======WELCOME SCREEN====="""
        welcome.Welcome().draw(self.game_surface) 
        while not running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif pygame.key.get_pressed()[pygame.K_SPACE]:
                    running = True
        """======GAME LOOP====="""
        clock = pygame.time.Clock()
        while running:
            boundary_collision = False
            self.ball.reset()
            while not boundary_collision:
                time_passed = clock.tick(FPS) / 1000.0
                """======INPUTS====="""
                self.event_queue(time_passed)
                """======UPDATE===="""
                self.ball.update(time_passed)
                """=====RULES====="""
                self.ball_paddle_collision()
                boundary_collision = self.boundary_collision()
                """======DRAW FRAME====="""
                self.draw(time_passed)
                pygame.display.update()
