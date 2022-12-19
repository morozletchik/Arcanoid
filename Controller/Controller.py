

from Simulation.Simulation import Simulation
from Visualisator.Visualisator import Visualisator

from pygame.rect import Rect


class Controller(object):

    def __init__(self, rect: Rect, simulation: Simulation, visualisator: Visualisator):
        self._simulation = simulation
        self._visualisator = visualisator
        self._rect = rect

    def change_rect(self, rect: Rect):
        self._rect = rect

    def add_body(self, mouse_start_pos, mouse_cur_pos):
        position = (
            (mouse_start_pos[0] - self._rect.width / 2) / self._visualisator.scale + self._visualisator.view_point[0],
            (mouse_start_pos[1] - self._rect.height / 2) / self._visualisator.scale + self._visualisator.view_point[1]
        )
        mass = 10
        radius = 10
        velocity = (
            (mouse_cur_pos[0] - mouse_start_pos[0]) / self._visualisator.scale,
            (mouse_start_pos[0] - mouse_start_pos[0]) / self._visualisator.scale
        )
        self._simulation.add_ball(
            mass,
            position[0],
            position[1],
            velocity[0],
            velocity[1],
            radius,
            (255, 255, 255)
        )

    def strike(self, start_mouse_pos, cur_mouse_pos):
        position = (
            (start_mouse_pos[0] - self._rect.width / 2) / self._visualisator.scale + self._visualisator.view_point[0],
            (start_mouse_pos[1] - self._rect.height / 2) / self._visualisator.scale + self._visualisator.view_point[1]
        )

        impulse = (
            (start_mouse_pos[0] - cur_mouse_pos[0]),
            (start_mouse_pos[1] - cur_mouse_pos[1])
        )
        self._simulation.strike_in_point(position, impulse)

    def update(self):
        pass
