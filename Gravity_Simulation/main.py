

import sys
import pygame
from UI.UIsystem import UISystem
from Simulation.Simulation import Simulation
from Controller.Controller import Controller
from Visualisator.Visualisator import Visualisator

WIDTH = 1000
HEIGHT = 700

FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


simulation = Simulation()
simulation.add_body(10**15, 0, 5, 5, 0, 10, (200, 0, 0))
simulation.add_body(10**15, 100, 0, -5, 0, 10, (0, 0, 0))

visualisator = Visualisator(simulation)
visualisator.change_view_point((50, 0))
visualisator.change_scale(1)


controller = Controller(simulation, visualisator)

ui_system = UISystem(WIDTH, HEIGHT, controller, visualisator)

running = True
while running:
    dt = clock.tick(FPS) / 1000

    for i in range(10):
        simulation.update(dt)

    screen.fill((0, 0, 0))
    ui_system.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        ui_system.event_handler(event)

        if event.type == pygame.QUIT:
            running = False

sys.exit()
