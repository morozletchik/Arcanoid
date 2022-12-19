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

    def __init__(self, x, y, width, height, simulation):
        super().__init__(10, x, y, 0, 0, (0, 0, 0), simulation)
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
        intersect_point = []

        if abs(obj.x - self.rect.x) < obj.radius:
            point1 = (self.rect.x, obj.y + (obj.radius ** 2 - (obj.x - self.rect.x) ** 2) ** 0.5)
            point2 = (self.rect.x, obj.y - (obj.radius ** 2 - (obj.x - self.rect.x) ** 2) ** 0.5)

            if (self.rect.y <= point1[1]) and (point1[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point1)

            if (self.rect.y <= point2[1]) and (point2[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point2)

        if abs(obj.x - self.rect.x - self.rect.width) < obj.radius:
            point1 = (
                self.rect.x + self.rect.width,
                obj.y + (obj.radius ** 2 - (obj.x - self.rect.x - self.rect.width) ** 2) ** 0.5
            )
            point2 = (
                self.rect.x + self.rect.width,
                obj.y - (obj.radius ** 2 - (obj.x - self.rect.x - self.rect.width) ** 2) ** 0.5
            )

            if (self.rect.y <= point1[1]) and (point1[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point1)

            if (self.rect.y <= point2[1]) and (point2[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point2)

        if abs(obj.y - self.rect.y) < obj.radius:
            point1 = (
                obj.x + (obj.radius ** 2 - (obj.y - self.rect.y) ** 2) ** 0.5,
                self.rect.y
            )
            point2 = (
                obj.x - (obj.radius ** 2 - (obj.y - self.rect.y) ** 2) ** 0.5,
                self.rect.y
            )

            if (self.rect.x <= point1[0]) and (point1[0] <= self.rect.x + self.rect.width):
                intersect_point.append(point1)

            if (self.rect.x <= point2[0]) and (point2[0] <= self.rect.x + self.rect.width):
                intersect_point.append(point2)

        if abs(obj.y - self.rect.y - self.rect.height) < obj.radius:
            point1 = (
                obj.x + (obj.radius ** 2 - (obj.y - self.rect.y - self.rect.height) ** 2) ** 0.5,
                self.rect.y + self.rect.height
            )
            point2 = (
                obj.x - (obj.radius ** 2 - (obj.y - self.rect.y - self.rect.height) ** 2) ** 0.5,
                self.rect.y + self.rect.height
            )

            if (self.rect.x <= point1[0]) and (point1[0] <= self.rect.x + self.rect.width):
                intersect_point.append(point1)

            if (self.rect.x <= point2[0]) and (point2[0] <= self.rect.x + self.rect.width):
                intersect_point.append(point2)

        return intersect_point


class Wall(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(self, x, y, width, height)


class Brick(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(self, x, y, width, height)

    def on_collide(self, obj):
        if self.intersect(obj):
            self.simulation.delete_body()
            return True


class Racket(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(self, x, y, width, height)
