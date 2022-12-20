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

    def event_handler(self, event):
        '''
        processes events: mouse movement and start of a new game
        :param event:
        '''
        if event.type == pygame.MOUSEMOTION:
            mouse_move = (event.rel[0] / self._visualisator.scale, event.rel[1] / self._visualisator.scale)
            mouse_move = (mouse_move[0], 0)
            self._simulation.move_paddle(mouse_move)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and (self._simulation.is_paused() or self._simulation.is_ready()):
                self._simulation.start()

    def pause_simulation(self):
        self._simulation.pause_simulation()

    def continue_simulation(self):
        self._simulation.continue_simulation()
