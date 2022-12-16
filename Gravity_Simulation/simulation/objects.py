class Body(object):

    def __init__(self, mass, x, y, velx, vely, radius, color):
        self.mass = 0
        self.x = 0
        self.y = y
        self.Vx = velx
        self.Vy = vely
        self.ax = self.ay = 0
        self.radius = radius
        self.color = color

    def move_space_object(self, dt):
        """Перемещает тело в соответствии с действующей на него силой.

        Параметры:

        **body** — тело, которое нужно переместить.
        """
        self.Vx += self.ax * dt
        self.x += self.Vx * dt
        self.Vy += self.ay * dt
        self.y += self.Vy * dt