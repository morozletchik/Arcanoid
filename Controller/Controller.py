import pygame

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

    def event_handler(self, event):
        if event.type == pygame.MOUSEMOTION:
            mouse_move = (event.rel[0] / self._visualisator.scale, event.rel[1] / self._visualisator.scale)
            mouse_move = (mouse_move[0], 0)
            self._simulation.move_paddle(mouse_move)


