

from Gravity_Simulation.Simulation.simulation import Simulation
from pygame.surface import Surface


class Visualisator(object):

    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self._view_point = (0, 0)
        self._scale = 1

    def visualize(self) -> Surface:
        #TODO: сделать фукнцию визуализации
        pass

    def change_view_point(self, new_point):
        self._view_point = new_point

    @property
    def view_point(self):
        return self._view_point

    def change_scale(self, new_scale):
        self._scale = new_scale

    @property
    def scale(self):
        return self._scale