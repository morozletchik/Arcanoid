

import sys
import pygame
from UI.UIsystem import UISystem
from Simulation.simulation import Simulation

WIDTH = 1000
HEIGHT = 700

FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ui_system = UISystem(WIDTH, HEIGHT)

simulation = Simulation()


running = True
while running:
    clock.tick(FPS)

    screen.fill((0, 0, 0))
    ui_system.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        ui_system.event_handler(event)

        if event.type == pygame.QUIT:
            running = False

sys.exit()
