import pygame, sys
import pygame.mixer
from pygame.locals import *
from constants import *
from game_entities import pitch, bar, ball, score, welcome


class Game(object):
    def __init__(self):
        self.pitch = pitch.Pitch()
        self.score = score.Score(0, 0)
        self.bar_left = bar.Bar(0)
        self.bar_right = bar.Bar(WINDOW_WIDTH-BAR_WIDTH)
        self.ball = ball.Ball(10, WINDOW_HEIGHT/2)
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
        if self.ball.rect.top >= WINDOW_HEIGHT:
            self.ball.reflect((0, 1), bottom=WINDOW_HEIGHT)
        if self.ball.rect.top <= 0:
            self.ball.reflect((0, 1), top=0)
        if self.ball.rect.left <= 0:
            self.ball.reflect((1, 0), left=0)
            self.crash_sound()
            self.score.away_scored()
        if self.ball.rect.right >= WINDOW_WIDTH:
            self.crash_sound()
            self.ball.reflect((1, 0), right=WINDOW_WIDTH)
            self.score.home_scored()

    def run(self):
        pygame.init()
        running = False
        clock = pygame.time.Clock()
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
        while running:
            time_passed = clock.tick(FPS) / 1000.0
            """======INPUTS====="""
            self.event_queue(time_passed)
            """======UPDATE===="""
            self.ball.update(time_passed)
            """=====RULES====="""
            self.ball_paddle_collision()
            self.boundary_collision()
            """======DRAW FRAME====="""
            self.draw(time_passed)
            pygame.display.update()
