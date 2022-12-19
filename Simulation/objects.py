
from pygame.rect import Rect
import random

from Simulation import Simulation

stiffness_koef = 100
wall_stiffness_koef = 1000

friction_koef = 0.3


class GameObject(object):

    def __init__(self, mass, x, y, velx, vely, color, simulation : Simulation):

        self.mass = mass
        self.x = x
        self.y = y
        self.Vx = velx
        self.Vy = vely
        self.ax = self.ay = 0
        self.color = color
        self.simulation = simulation

    def move_object(self, dt):
        pass

    def is_collide(self, obj):
        pass

    def on_collide(self, other):
        pass

    def apply_impulse(self, impulse):
        pass

    def apply_friction(self):
        pass


class Ball(GameObject):

    def __init__(self, mass, x, y, velx, vely, radius, color, simulation):
        super().__init__(mass, x, y, velx, vely, color, simulation)
        self.radius = radius

    def move_object(self, dt):
        self.Vx += self.ax * dt
        self.x += self.Vx * dt
        self.Vy += self.ay * dt
        self.y += self.Vy * dt

    def is_collide(self, obj2):
        if type(obj2) == Ball:
            return (self.x - obj2.x)**2 + (self.y - obj2.y)**2 < (self.radius + obj2.radius)**2
        if type(obj2) == Rectangle:
            return obj2.intersect_with_circle(self) is not []

    def on_collide(self, obj):
        if type(obj) == Ball:
            length = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
            if length != 0:
                delta = ((self.radius + obj.radius) - length) / 2
                impulse_x = stiffness_koef * delta * (self.x - obj.x) / length
                impulse_y = stiffness_koef * delta *(self.y - obj.y) / length

                self.apply_impulse((impulse_x, impulse_y))
            else:
                self.Vx += (random.random() - 0.5) / 10**4
                self.Vy += (random.random() - 0.5) / 10**4

        if type(obj) == Rectangle:
            intersects = obj.intersect_with_circle(self)
            if len(intersects) >= 2:
                line_vector = (
                    intersects[1][0] - intersects[0][0],
                    intersects[1][1] - intersects[0][1]
                )
                line_vector_length = (line_vector[0]**2 + line_vector[1]**2)**0.5
                delta_r = (self.x - intersects[0][0], self.y - intersects[0][1])
                multi = delta_r[0] * line_vector[0] + delta_r[1] * line_vector[1]

                normal_vector = (
                    delta_r[0] - multi * line_vector[0] / line_vector_length,
                    delta_r[1] - multi * line_vector[1] / line_vector_length
                )

                print(normal_vector)

                length = (normal_vector[0]**2 + normal_vector[1]**2)**0.5
                delta = self.radius - (
                        self.radius**2
                        - (intersects[1][0] - intersects[0][0])**2 / 4
                        - (intersects[1][1] - intersects[0][1])**2 / 4
                ) ** 0.5

                impulse_x = wall_stiffness_koef * delta**(1.5) * normal_vector[0] / length
                impulse_y = wall_stiffness_koef * delta * normal_vector[1] / length

                self.apply_impulse((impulse_x, impulse_y))

    def apply_impulse(self, impulse):
        self.Vx += impulse[0] / self.mass
        self.Vy += impulse[1] / self.mass

    def apply_friction(self):
        if self.Vx != 0:
            self.ax = -self.Vx / abs(self.Vx) * friction_koef
        else:
            self.ax = 0

        if self.Vy != 0:
            self.ay = -self.Vy / abs(self.Vy) * friction_koef
        else:
            self.ay = 0


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

    def intersect_with_circle(self, obj: Ball):
        intersect_point = []

        if abs(obj.x - self.rect.x) < obj.radius:
            point1 = (self.rect.x, obj.y + (obj.radius**2 - (obj.x - self.rect.x)**2)**0.5)
            point2 = (self.rect.x, obj.y - (obj.radius**2 - (obj.x - self.rect.x)**2)**0.5)

            if (self.rect.y <= point1[1]) and (point1[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point1)

            if (self.rect.y <= point2[1]) and (point2[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point2)

        if abs(obj.x - self.rect.x - self.rect.width) < obj.radius:
            point1 = (
                self.rect.x + self.rect.width,
                obj.y + (obj.radius**2 - (obj.x - self.rect.x - self.rect.width)**2)**0.5
            )
            point2 = (
                self.rect.x + self.rect.width,
                obj.y - (obj.radius**2 - (obj.x - self.rect.x - self.rect.width)**2)**0.5
            )

            if (self.rect.y <= point1[1]) and (point1[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point1)

            if (self.rect.y <= point2[1]) and (point2[1] <= self.rect.y + self.rect.height):
                intersect_point.append(point2)

        if abs(obj.y - self.rect.y) < obj.radius:
            point1 = (
                obj.x + (obj.radius**2 - (obj.y - self.rect.y)**2)**0.5,
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
                obj.x + (obj.radius**2 - (obj.y - self.rect.y - self.rect.height)**2)**0.5,
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


