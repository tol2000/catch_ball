from random import randint

import pygame
from pygame.draw import circle

from ball import Ball


class CatchBall:

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [BLUE, YELLOW, MAGENTA, CYAN]

    def __init__(self, balls_per_second: float):
        self.ball = None
        self.balls = 0
        self.hits = 0
        self.missed = 0

        self.frames = 0

        pygame.init()

        self.FPS: int = 100
        self.screen = pygame.display.set_mode((1200, 900))

        self.FRAMES_BETWEEN_BALLS = self.FPS / balls_per_second

        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.finished = False

    '''
    Creates and draws new ball
    '''
    def new_ball(self):
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        color = self.COLORS[randint(0, len(self.COLORS)-1)]
        self.ball = Ball(self.screen, color, x, y, r)
        self.ball.paint()
        self.balls += 1

    def key_down_event_handler(self, event):
        if event.key == pygame.K_q:
            self.finished = True

    def mouse_down_event_handler(self, event):
        if event.button == 1:
            if self.ball:
                if self.ball.point_inside_ball(event.pos[0], event.pos[1]):
                    circle(self.screen, self.GREEN, event.pos, 20)
                    self.hits += 1
                else:
                    circle(self.screen, self.RED, event.pos, 20)
                    self.missed += 1
                print(f'Balls: {self.balls}, Hits: {self.hits}, Missed: {self.missed}')

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif event.type == pygame.KEYDOWN:
                    self.key_down_event_handler(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down_event_handler(event)

            if self.frames < self.FRAMES_BETWEEN_BALLS:
                self.frames += 1
            else:
                self.screen.fill(self.BLACK)
                self.new_ball()
                self.frames = 0

            pygame.display.update()
            self.clock.tick(self.FPS)

        pygame.quit()
