from random import randint

from pygame import Surface
from pygame.draw import circle

from mycolors import MyColors


class Ball:

    MIN_RADIUS = 40
    MAX_RADIUS = 60

    def __init__(self, screen: Surface, color):
        self.screen = screen
        self.color = color

        self.x = randint(self.MAX_RADIUS, self.screen.get_width()-self.MAX_RADIUS)
        self.y = randint(self.MAX_RADIUS, self.screen.get_height()-self.MAX_RADIUS)
        self.r = randint(self.MIN_RADIUS, self.MAX_RADIUS)

        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)

        self.paint(color=self.color)

    def point_inside_ball(self, point_x, point_y):
        return (point_x - self.x)**2 + (point_y - self.y)**2 <= self.r**2

    def paint(self, color):
        circle(self.screen, color, (self.x, self.y), self.r)

    def repaint(self):
        self.paint(color=MyColors.BLACK)
        self.x += self.vx
        self.y += self.vy
        if self.x < self.r or self.x > self.screen.get_width()-self.r:
            self.vx = -self.vx
            self.x += self.vx
        if self.y < self.r or self.y > self.screen.get_height()-self.r:
            self.vy = -self.vy
            self.y += self.vy
        self.paint(color=self.color)
