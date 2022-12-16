

from Gravity_Simulation.Simulation.simulation import Simulation
from Gravity_Simulation.Visualisator.Visualitor import Visualisator


class Controller(object):

    def __init__(self, simulation: Simulation, visualisator: Visualisator):
        self._simulation = simulation
        self._visualisator = visualisator

    def add_body(self, mouse_start_pos, mouse_cur_pos):
        position = (
                mouse_start_pos[0] / self._visualisator.scale - self._visualisator.view_point[0],
                mouse_start_pos[1] / self._visualisator.scale - self._visualisator.view_point[1]
        )
        mass = 10
        radius = 5
        velocity = (
            (mouse_cur_pos[0] - mouse_start_pos[0]) / self._visualisator.scale,
            (mouse_start_pos[0] - mouse_start_pos[0]) / self._visualisator.scale
        )
        self._simulation.add_body(
            mass,
            position[0],
            position[1],
            velocity[0],
            velocity[1],
            radius,
            (0, 0, 255)
        )
