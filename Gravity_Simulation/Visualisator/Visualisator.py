

from Gravity_Simulation.Simulation.Simulation import Simulation
from pygame.surface import Surface
from pygame.draw import circle


class Visualisator(object):

    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self._view_point = (0, 0)
        self._scale = 1

    def visualize(self, width, height) -> Surface:
        surface = Surface((width, height))
        for obj in self.simulation.space_objects:
            x = (obj.x - self._view_point[0]) * self._scale + width // 2
            y = (obj.y - self._view_point[1]) * self._scale + height // 2
            radius = obj.radius * self._scale
            circle(surface, obj.color, (x, y), radius)
        return surface

    def change_view_point(self, new_view_point):
        self._view_point = new_view_point

    @property
    def view_point(self):
        return self._view_point

    def change_scale(self, new_scale):
        self._scale = new_scale

    @property
    def scale(self):
        return self._scale


