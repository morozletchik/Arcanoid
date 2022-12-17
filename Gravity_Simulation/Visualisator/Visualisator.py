import pygame

from Gravity_Simulation.Simulation.Simulation import Simulation
from pygame.surface import Surface
from pygame.draw import circle
from pygame.rect import Rect


class Visualisator(object):

    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self._view_point = (0, 0)
        self._scale = 1

    def from_screen_to_world_coordinates(self, position, rect: Rect):
        return (
            (position[0] - rect.width / 2) / self.scale + self.view_point[0],
            (position[1] - rect.height / 2) / self.scale + self.view_point[1]
        )

    def from_worl_to_screen_coordinates(self, position, rect: Rect):
        x = (position[0] - self._view_point[0]) * self._scale + rect.width // 2
        y = (position[1] - self._view_point[1]) * self._scale + rect.height // 2

        return x, y

    def visualize(self, width, height) -> Surface:
        surface = Surface((width, height), flags=pygame.SRCALPHA)
        for obj in self.simulation.space_objects:
            (x, y) = self.from_worl_to_screen_coordinates((obj.x, obj.y), Rect(0, 0, width, height))
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


