from pygame.draw import circle


class Ball:

    def __init__(self, screen, color, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.screen = screen
        self.color = color

    def point_inside_ball(self, point_x, point_y):
        return (point_x - self.x)**2 + (point_y - self.y)**2 <= self.r**2

    def paint(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)
