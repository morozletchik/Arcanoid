from pygame.rect import Rect
import random
import numpy as np

class GameObject(object):
    def __init__(self, x, y, vx, vy, color, simulation):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.simulation = simulation

    def move_object(self, dt):
        pass

    def intersect(self, obj):
        pass

    def on_collide(self, other):
        pass

class Ball(GameObject):

    def __init__(self, x, y, vx, vy, r, color, simulation):
        '''
        constructor
        :param r: radius
        '''
        super().__init__(x, y, vx, vy, color, simulation)
        self.r = r

    def move_object(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def intersect(self, obj):
        '''
        checks whether the ball collides with any objects

        :param obj: object that might be shot by the ball
        :return: object's side shot by the ball or None (if none of the sides were shot)
        '''
        edges = {"left": Rect(obj.left, obj.top, 1, obj.height),
                 "right": Rect(obj.right - 1, obj.top, 1, obj.height),
                 "top": Rect(obj.left, obj.top, obj.width, 1),
                 "bottom": Rect(obj.left, obj.bottom - 1, obj.width, 1)}

        collisions = set(edge for (edge, rect) in edges.items() if obj.collideobjects(self))

        if len(collisions) == 0:
            return None

        if len(collisions) == 1:
            return list(collisions)[0]

        if "top" in collisions:
            if "right" in collisions:
                if np.abs((self.y - obj.top) / (self.x - obj.right)) < 1:
                    return "right"
                else:
                    return "top"

            if "left" in collisions:
                if np.abs((self.y - obj.top) / (self.x - obj.left)) < 1:
                    return "left"
                else:
                    return "top"

        elif "bottom" in collisions:
            if "right" in collisions:
                if np.abs((self.y - obj.bottom) / (self.x - obj.right)) < 1:
                    return "right"
                else:
                    return "bottom"

            if "left" in collisions:
                if np.abs((self.y - obj.bottom) / (self.x - obj.left)) < 1:
                    return "left"
                else:
                    return "bottom"

class Rectangle(GameObject):
    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        self.rect = Rect(x, y, width, height)
        self.top = y
        self.bottom = y + height
        self.left = x
        self.right = x + width

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def on_collide(self, obj: Ball):
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

class Paddle(Rectangle):

    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        pass

class Simulation:
    def __init__(self):
        self.objects = []
        self.life = 1
        self.points = 0

    def score(self, obj):
        self.points += 1

    def update(self, dt):
        for obj in self.objects:
            self.collision_handle(obj)
        self.move_bodies(dt)

    def move_bodies(self, dt):
        """Пересчитывает координаты объектов."""
        for obj in self.objects:
            obj.move_object(dt)

    def delete_body(self, obj):
        self.objects.remove(obj)

    def collision_handle(self, obj1):
        for obj2 in self.objects:
            if obj1 is not obj2 and obj1.intersect(obj2):
                obj1.on_collide(obj2)

    def add_wall(self, x, y, width, height, color):
        wall = Rectangle(x, y, width, height, color, self)
        self.objects.append(wall)
