gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

space_objects = []


class Simulation:

    def __init__(self):
        self.Vy = None
        self.Vx = None
        self.m = None
        self.y = None
        self.x = None
        self.Fy = None
        self.Fx = None

    def calculate_force(self, space_objects):
        """Вычисляет силу, действующую на тело.

        Параметры:

        **body** — тело, для которого нужно вычислить дейстующую силу.
        **space_objects** — список объектов, которые воздействуют на тело.
        """

        self.Fx = self.Fy = 0
        for obj in space_objects:
            if self == obj:
                continue  # тело не действует гравитационной силой на само себя!
            r = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
            self.Fx += gravitational_constant * self.m * obj.m / (r ** 2) * ((obj.x - self.x) / r)
            self.Fy += gravitational_constant * self.m * obj.m / (r ** 2) * ((obj.y - self.y) / r)

    def move_space_object(self, dt):
        """Перемещает тело в соответствии с действующей на него силой.

        Параметры:

        **body** — тело, которое нужно переместить.
        """

        ax = self.Fx / self.m
        self.Vx += ax * dt
        self.x += self.Vx * dt
        ay = self.Fy / self.m
        self.Vy += ay * dt
        self.y += self.Vy * dt

    def recalculate_space_objects_positions(self, dt):
        """Пересчитывает координаты объекта.

        Параметры:

        **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
        **dt** — шаг по времени
        """
        self.calculate_force(space_objects)
        self.move_space_object(dt)

    def add_body(self):
        """Создаёт новое тело"""
        self.Vy = float(input())
        self.Vx = float(input())
        self.m = float(input())
        self.y = float(input())
        self.x = float(input())
        self.Fy = float(input())
        self.Fx = float(input())
        space_objects.append(self)