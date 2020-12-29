from random import randint

import pygame
from pygame.draw import circle

from ball import Ball
from mycolors import MyColors


class CatchBall:

    FPS: int = 150
    COLORS = [MyColors.BLUE, MyColors.YELLOW, MyColors.MAGENTA, MyColors.CYAN]
    MIN_SPEED = 50
    MAX_SPEED = FPS
    SPEED_INC = 5

    current_speed = MAX_SPEED

    def __init__(self):
        self.ball = None
        self.balls = 0
        self.hits = 0
        self.missed = 0

        self.frames = 0
        self.frames_between_move = 0

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 900))

        self.recalculate_speed()

        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.finished = False

        self.init_balls()

    '''
    Creates and draws new ball
    '''
    def init_balls(self):
        self.screen.fill(MyColors.BLACK)
        color = self.COLORS[randint(0, len(self.COLORS)-1)]
        self.ball = Ball(self.screen, color)
        self.balls += 1
        self.frames = 0

    def key_down_event_handler(self, event):
        if event.key == pygame.K_q:
            self.finished = True

    def mouse_down_event_handler(self, event):
        if event.button == 1:
            if self.ball:
                if self.ball.point_inside_ball(event.pos[0], event.pos[1]):
                    circle(self.screen, MyColors.GREEN, event.pos, 5)
                    self.hits += 1
                    self.increase_speed()
                    self.init_balls()
                else:
                    circle(self.screen, MyColors.RED, event.pos, 5)
                    self.missed += 1
                    self.decrease_speed()

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif event.type == pygame.KEYDOWN:
                    self.key_down_event_handler(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down_event_handler(event)

            if self.frames < self.frames_between_move:
                self.frames += 1
            else:
                self.ball.repaint()
                self.frames = 0

            pygame.display.set_caption(
                f'Speed: {self.current_speed}, Balls: {self.balls}, Hits: {self.hits}, Missed: {self.missed}'
            )
            pygame.display.update()
            self.clock.tick(self.FPS)

        pygame.quit()

    def recalculate_speed(self):
        self.frames_between_move = self.FPS / self.current_speed

    def increase_speed(self):
        if self.current_speed <= self.MAX_SPEED-self.SPEED_INC:
            self.current_speed += self.SPEED_INC
            self.recalculate_speed()

    def decrease_speed(self):
        if self.current_speed >= self.MIN_SPEED+self.SPEED_INC:
            self.current_speed -= self.SPEED_INC
            self.recalculate_speed()
