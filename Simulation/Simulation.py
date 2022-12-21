
from pygame.rect import Rect
import random
import numpy as np
from typing import Callable

BRICK_COLORS = [(95, 9, 243), (111, 140, 253), (0, 239, 144)]
VALUES = [100, 50, 10]

class GameObject(object):
    def __init__(self, x, y, vx, vy, color, simulation):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.simulation = simulation

    def move_object(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

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
        return Rect(self.x - self.r/2, self.y - self.r/2, self.r, self.r)

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
            self.vx = -self.vx + obj.vx
            if intersect == "left":
                self.x = obj.left - self.r
            if intersect == "right":
                self.x = obj.right + self.r

        if intersect == "top" or intersect == "bottom":
            self.vy = -self.vy + obj.vy
            if intersect == "top":
                self.y = obj.top - self.r
            if intersect == "bottom":
                self.y = obj.bottom + self.r


class Rectangle(GameObject):
    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, 0, 0, color, simulation)
        self.width = width
        self.height = height

    def intersect(self, obj):
        if type(obj) == Ball:
            return obj.intersect(self) is not None

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


class AcceleratingWall(Rectangle):

    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        self.acceleration_scale = 5

    def on_collide(self, obj: Ball):
        obj.vx *= 1 + self.acceleration_scale / 100
        obj.vy *= 1 + self.acceleration_scale / 100


class Brick(Rectangle):
    def __init__(self, x, y, width, height, color, value, simulation):
        super().__init__(x, y, width, height, color, simulation)
        self.value = value

    def on_collide(self, obj):
        self.simulation.delete_body(self)
        obj.on_collide(self)
        self.simulation.increase_score(self.value)


class Paddle(Rectangle):

    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)
        pass

    def player_move(self, delta_move):
        self.move_on_delta(delta_move)
        self.vx = delta_move[0]

    def move_object(self, dt):
        pass


class Trigger(Rectangle):

    def __init__(self, x, y, width, height, color, simulation):
        super().__init__(x, y, width, height, color, simulation)

    def is_out_of_screen(self, obj: Ball):
        '''
        checks if the ball fell under the bottom
        :param obj: ball
        :return: (True or False) - is the ball out of the screen
        '''
        return


class SimulationState(object):
    READY_TO_START = 0,
    PAUSED = 1,
    GAMEOVER = 2,
    PLAYING = 3,
    WIN = 4


class Simulation:
    def __init__(self, width, height):
        self.objects = []
        self.lives = 3
        self.__points = 0
        self.width = width
        self.height = height
        self.state = SimulationState.READY_TO_START
        self.all_brick_score = 0
        self.ball = Ball(
            0, height / 3,
            -20, 20,
            self.width / 200, (255, 255, 255), self
        )
        self.paddle = Paddle(
            0, self.height / 2 - self.height / 80,
            self.width / 12, 1.1 * height / 50, (255, 158, 161), self
        )
        self.on_change_state = []

    def setup(self):
        '''
        creates walls and bricks and their properties
        '''
        thickness = self.width / 100
        self.add_wall(
            -self.width / 2 - thickness, thickness / 2 + self.height / 2,
            thickness, 2 * self.height + 2 * thickness,
            (70, 70, 70)
        )
        self.add_wall(
            self.width / 2 + thickness, thickness / 2 + self.height / 2,
            thickness, 2 * self.height + 2 * thickness,
            (70, 70, 70)
        )

        self.objects.append(
            AcceleratingWall(0, -self.height / 2, self.width + 2 * thickness, thickness, (70, 70, 70), self)
        )

        count_x = 10
        count_y = 6

        self.all_brick_score = count_x * count_y

        brick_width = 0.9 * (self.width - thickness) / count_x
        brick_height = 2 * thickness

        brick_indent = (
            0.1 * (self.width - thickness) / count_x,
            thickness
        )

        brick_start = (-self.width / 2 + self.width / 19, -self.height / 3 + self.height / 30)

        for i in range(count_x):
            for j in range(count_y):
                self.objects.append(
                    Brick(
                        brick_start[0] + i * (brick_width + brick_indent[0]),
                        brick_start[1] + j * (brick_height + brick_indent[1]),
                        brick_width, brick_height,
                        BRICK_COLORS[j // 2], VALUES[j // 2], self
                    )
                )
                self.all_brick_score += VALUES[j // 2]

        self.objects.append(
            self.paddle
        )

        self.objects.append(
            self.ball
        )
        self.spawn_ball()

    def spawn_ball(self):
        '''
        "spawns" a new ball (by moving it to the centre of the screen)
        and gives to it randomly directed velocity after pushing SPACE
        '''
        self.state = SimulationState.READY_TO_START
        self.ball.vx = 0
        self.ball.vy = 0
        self.ball.x = 0
        self.ball.y = self.height / 10

    def start(self):
        '''
        starts a new live
        :return:
        '''
        self.paddle.x = 0
        self.paddle.y = self.height / 2 - self.height / 80
        self.ball.vx = 20 * random.choice((-1, 1))
        self.ball.vy = 20 * random.choice((-1, 1))
        self.state = SimulationState.PLAYING

    @property
    def score(self):
        return self.__points

    def increase_score(self, value):
        self.__points += value

    #stick together
    def update(self, dt):
        '''
        updates positions of objects
        :param dt: period of updating positions of the objects
        '''
        self.out_of_screen()
        if self.all_brick_score == self.score:
            self.win()
        if self.state == SimulationState.PLAYING:
            for obj in self.objects:
                self.collision_handle(obj)
            self.move_bodies(dt)

        for event in self.on_change_state:
            event()

    def move_bodies(self, dt):
        """
        changes objects' positions
        :param dt: period of updating positions of the objects
        :return:
        """
        for obj in self.objects:
            obj.move_object(dt)

    def delete_body(self, obj):
        self.objects.remove(obj)

    def out_of_screen(self):
        '''
        reduces the number of the ball's lives if it is positive
        calls game over if it is zero
        :param trigger: bottom of the screen
        :param ball: ball
        '''
        if self.lives > 0:
            if (self.ball.y - self.ball.r > self.width / 2):
                self.lives -= 1
                self.spawn_ball()
        else:
            self.state = SimulationState.GAMEOVER

    def collision_handle(self, obj1):
        for obj2 in self.objects:
            if obj1 is not obj2 and obj1.intersect(obj2):
                obj1.on_collide(obj2)

    def add_wall(self, x, y, width, height, color):
        wall = Rectangle(x, y, width, height, color, self)
        self.objects.append(wall)

    def move_paddle(self, delta_move):
        '''
        processes paddle movement
        :param delta_move: movement of the mouse
        '''
        if self.state == SimulationState.PLAYING:
            if self.paddle is not None:
                self.paddle.player_move(delta_move)

                if self.paddle.x > self.width / 2 - self.width / 25:
                    self.paddle.x = self.width / 2 - self.width / 25
                if self.paddle.x < -self.width / 2 + self.width / 25:
                    self.paddle.x = -self.width / 2 + self.width / 25

    def add_on_change_state_event(self, action: Callable):
        self.on_change_state.append(action)

    def remove_on_change_state_event(self, action: Callable):
        self.on_change_state.remove(action)

    def continue_simulation(self):
        self.state = SimulationState.PLAYING

    def pause_simulation(self):
        self.state = SimulationState.PAUSED

    def game_over(self):
        self.state = SimulationState.GAMEOVER

    def is_game_over(self):
        return self.state == SimulationState.GAMEOVER

    def is_paused(self):
        return self.state == SimulationState.PAUSED

    def is_ready(self):
        return self.state == SimulationState.READY_TO_START

    def win(self):
        self.state = SimulationState.WIN

    def is_win(self):
        return self.state == SimulationState.WIN



