from pygame.rect import Rect
import random

from Simulation import Simulation

class GameObject(object):

    def __init__(self, x, y, Vx, Vy, color, simulation: Simulation):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.color = color
        self.simulation = simulation

    def move_object(self, dt):
        pass

    def is_collide(self, obj):
        pass

    def on_collide(self, other):
        pass

class Ball(GameObject):

    def __init__(self, x, y, Vx, Vy, r, color, simulation):
        super().__init__(x, y, Vx, Vy, color, simulation)
        self.r = r

    def move_object(self, dt):
        self.x += self.Vx * dt
        self.y += self.Vy * dt

    def is_collide(self, obj):
        if (obj.collideobjects(self) == None): return True
        return False

    def on_collide(self, obj):
        pass
class Rectangle(GameObject):
    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        self.rect = Rect(x - width / 2, y - height / 2, width, height)

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def apply_friction(self):
        pass

    def intersect(self, obj: Ball):
        pass

class Wall(Rectangle):
    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        pass


class Brick(Rectangle):
    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        pass

    def on_collide(self, obj):
        if self.intersect(obj):
            self.simulation.delete_body(obj)
            return True

class Racket(Rectangle):
    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        pass
