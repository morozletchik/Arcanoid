

from .objects import *

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Simulation:

    def __init__(self):
        self.objects = []

    def update(self, dt):
        for obj in self.objects:
            self.collision_handle(obj)
        for obj in self.objects:
            self.change_acceleration(obj)
        self.move_bodies(dt)

    @staticmethod
    def calculate_force_between_two_bodies(obj1, obj2):
        """1 действует на 2"""
        r = ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
        Fx = gravitational_constant * obj1.mass * obj2.mass / (r ** 2) * ((obj1.x - obj2.x) / r)
        Fy = gravitational_constant * obj1.mass * obj2.mass / (r ** 2) * ((obj1.y - obj2.y) / r)
        return Fx, Fy

    def apply_gravity(self, obj):
        Fx = 0
        Fy = 0

        for obj_iter in self.objects:
            if obj == obj_iter:
                continue
            F = Simulation.calculate_force_between_two_bodies(obj_iter, obj)
            Fx += F[0]
            Fy += F[1]

        obj.ax += Fx / obj.mass
        obj.ay += Fy / obj.mass

    def change_acceleration(self, obj):
        obj.ax = 0
        # self.apply_gravity(obj)
        obj.apply_friction()

    def move_bodies(self, dt):
        """Пересчитывает координаты объектов."""

        for obj in self.objects:
            obj.move_object(dt)

    def add_body(self, mass, x, y, Vx, Vy, radius, color):
        self.objects.append(Ball(mass, x, y, Vx, Vy, radius, color))

    def append_body(self, obj: Ball):
        self.objects.append(obj)

    def delete_body(self, obj):
        self.objects.remove(obj)

    def collision_handle(self, obj1):
        for obj2 in self.objects:
            if obj1 is not obj2 and obj1.is_collide(obj2):
                obj1.on_collide(obj2)

    def strike_in_point(self, point, impulse):
        for obj in self.objects:
            if type(obj) is Ball and (point[0] - obj.x) ** 2 + (point[1] - obj.y) ** 2 <= obj.radius ** 2:
                obj.apply_impulse(impulse)

    def add_wall(self, x, y, width, height):
        wall = Wall(x, y, width, height)
        self.objects.append(wall)







