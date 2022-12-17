

stiffness_koef = 10**15

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

    def move_space_object(self, dt):
        self.Vx += self.ax * dt
        self.x += self.Vx * dt
        self.Vy += self.ay * dt
        self.y += self.Vy * dt

    def is_collide(self, obj2):
        return (self.x - obj2.x)**2 + (self.y - obj2.y)**2 <= (self.radius + obj2.radius)**2

    def on_collide(self, obj):
        length = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
        if length != 0:
            delta = ((self.radius + obj.radius) - length) / 2
            impulse_x = stiffness_koef * delta * (self.x - obj.x) / length
            impulse_y = stiffness_koef * delta *(self.y - obj.y) / length

            self.Vx += impulse_x / self.mass
            self.Vy += impulse_y / self.mass