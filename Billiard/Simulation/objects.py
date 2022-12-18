
import random

stiffness_koef = 100


class Body(object):

    def __init__(self, mass, x, y, velx, vely, radius, color):
        self.mass = mass
        self.x = x
        self.y = y
        self.Vx = velx
        self.Vy = vely
        self.ax = self.ay = 0
        self.radius = radius
        self.color = color

    def move_object(self, dt):
        self.Vx += self.ax * dt
        self.x += self.Vx * dt
        self.Vy += self.ay * dt
        self.y += self.Vy * dt

    def is_collide(self, obj2):
        return (self.x - obj2.x)**2 + (self.y - obj2.y)**2 <= (self.radius + obj2.radius)**2

    def on_collide(self, obj):
        if type(obj) == Body:
            length = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
            if length != 0:
                delta = ((self.radius + obj.radius) - length) / 2
                impulse_x = stiffness_koef * delta * (self.x - obj.x) / length
                impulse_y = stiffness_koef * delta *(self.y - obj.y) / length

                self.apply_impulse((impulse_x, impulse_y))
            else:
                self.Vx += (random.random() - 0.5) / 10**4
                self.Vy += (random.random() - 0.5) / 10**4

        if type(obj) == Wall:
            pass

    def apply_impulse(self, impulse):
        self.Vx += impulse[0] / self.mass
        self.Vy += impulse[1] / self.mass


class Wall(object):

    def __init__(self, x, y, width, height, orientation):
        self.left_top = (x-width//2, y-height//2)
        self.right_top = (x+width//2, y-height//2 - width//2)
        self.left_bottom = (x - width // 2, y + height // 2)
        self.right_bottom = (x + width // 2, y + height // 2 + width // 2)

    def move_objects(self, dt):
        pass

    def is_collide(self, obj: Body):
        pass

    def on_collide(self, obj):
        pass

    def apply_impulse(self, impulse):
        pass