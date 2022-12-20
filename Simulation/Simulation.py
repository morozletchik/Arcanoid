
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
        super().__init__(x, y, vx, vy, color, simulation)
        self.r = r

    @property
    def bounds(self):
        return Rect(self.x - self.r/2, self.y - self.r/2, self.x + self.r/2, self.y + self.r/2)

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

        collisions = set(edge for (edge, rect) in edges.items() if self.bounds.colliderect(rect))

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

    def is_collide(self, obj):
        return self.intersect(obj) is not None

    def on_collide(self, obj):
        intersect = self.intersect(obj)
        if intersect == "left" or intersect == "right":
            self.vx = -self.vx

        if intersect == "top" or intersect == "bottom":
            self.vy = -self.vy


class Rectangle(GameObject):
    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        self.width = width
        self.height = height

    @property
    def rect(self):
        return Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    def on_collide(self, obj: Ball):
        pass

    def move_on_delta(self, delta_move):
        self.x += delta_move[0]
        self.y += delta_move[1]


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


class Paddle(Rectangle):

    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        pass

    def player_move(self, delta_move):
        self.move_on_delta(delta_move)


class Simulation:
    def __init__(self, width, height):
        self.objects = []
        self.life = 1
        self.__points = 0
        self.width = width
        self.height = height

    def setup(self):
        self.add_wall(-self.width / 2, 0, 20, self.height, (0, 0, 0))
        self.add_wall(self.width / 2, 0, 20, self.height, (0, 0, 0))
        self.add_wall(0, self.height / 2, self.width, 20, (0, 0, 0))
        self.add_wall(0, -self.height / 2, self.width, 20, (0,0,0))
        self.objects.append(
            Paddle(
                0, self.height / 2 - 40,
                80, 20, (255, 255, 255), self
            )
        )
        self.objects.append(
            Ball(
                0, 0, -10, 10, 10, (255, 255, 255), self
            )
        )

    @property
    def paddle(self):
        paddle = [obj for obj in self.objects if type(obj) == Paddle]
        if len(paddle) == 0:
            return None
        return paddle[0]

    @property
    def score(self):
        return self.__points

    def set_score(self, obj):
        self.__points += 1

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

    def move_paddle(self, delta_move):
        self.paddle.player_move(delta_move)
        if self.paddle.x > self.width / 2 - 60:
            self.paddle.x = self.width / 2 - 60
        if self.paddle.x < -self.width / 2 + 60:
            self.paddle.x = -self.width / 2 + 60



