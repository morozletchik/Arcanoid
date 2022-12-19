from .objects import *


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
        for obj in self.objects:
            self.change_acceleration(obj)
        self.move_bodies(dt)


    def change_acceleration(self, obj):
        obj.ax = 0
        # self.apply_gravity(obj)
        obj.apply_friction()

    def move_bodies(self, dt):
        """Пересчитывает координаты объектов."""

        for obj in self.objects:
            obj.move_object(dt)

    def add_ball(self, mass, x, y, Vx, Vy, radius, color):
        self.objects.append(Ball(mass, x, y, Vx, Vy, radius, color, self))

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
        wall = Rectangle(x, y, width, height, self)
        self.objects.append(wall)