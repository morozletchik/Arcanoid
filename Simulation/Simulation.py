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
        self.move_bodies(dt)

    def move_bodies(self, dt):
        """Пересчитывает координаты объектов."""
        for obj in self.objects:
            obj.move_object(dt)

    def add_ball(self, x, y, Vx, Vy, radius, color):
        self.objects.append(Ball(x, y, Vx, Vy, radius, color, self))

    def append_body(self, obj: Ball):
        self.objects.append(obj)

    def delete_body(self, obj):
        self.objects.remove(obj)

    def collision_handle(self, obj1):
        for obj2 in self.objects:
            if obj1 is not obj2 and obj1.is_collide(obj2):
                obj1.on_collide(obj2)

    def add_wall(self, x, y, width, height):
        wall = Rectangle(x, y, width, height, self)
        self.objects.append(wall)