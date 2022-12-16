

from objects import Body

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Simulation:

    def __init__(self):
        self.space_objects = []

    @staticmethod
    def calculate_force_between_two_bodies(obj1, obj2):
        """1 действует на 2"""
        r = ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
        Fx = gravitational_constant * obj1.mass * obj2.mass / (r ** 2) * ((obj2.x - obj1.x) / r)
        Fy = gravitational_constant * obj1.mass * obj2.mass / (r ** 2) * ((obj2.y - obj1.y) / r)
        return Fx, Fy

    def change_accelerations(self):

        for obj in self.space_objects:
            Fx = 0
            Fy = 0
            for obj_iter in self.space_objects:
                if obj == obj_iter:
                    continue
                F = Simulation.calculate_force_between_two_bodies(obj_iter, obj)
                Fx += F[0]
                Fy += F[1]

            obj.ax += Fx / obj.mass
            obj.ay += Fy / obj.mass

    def recalculate_space_objects_positions(self, dt):
        """Пересчитывает координаты объекта.

        Параметры:

        **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
        **dt** — шаг по времени
        """
        self.change_accelerations()
        for obj in self.space_objects:
            obj.move_space_object(dt)

    def add_body(self, mass, x, y, Vx, Vy, radius, color):
        """Создаёт новое тело"""
        self.space_objects.append(Body(mass, x, y, Vx, Vy, radius, color))


