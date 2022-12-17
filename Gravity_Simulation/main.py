

import sys
import pygame
from UI.UIsystem import UISystem
from Simulation.Simulation import Simulation
from Controller.Controller import Controller
from Visualisator.Visualisator import Visualisator
from pygame.rect import Rect
from UI.ToolBar.Tool import *
from UI.ToolBar.ToolBar import *
from UI.ToolBar.StrikeTool import *
from UI.UIElements.Button import *

def close():
    global running
    running = False

running = True

WIDTH = 1000
HEIGHT = 700

FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

simulation = Simulation()

visualisator = Visualisator(simulation)
visualisator.change_view_point((0, 0))
visualisator.change_scale(1)

canvas = Canvas(0, HEIGHT // 10, WIDTH, HEIGHT - HEIGHT // 10, "Canvas", visualisator)
controller = Controller(canvas.rect, simulation, visualisator)

tools = [
    ClickTool(
        canvas.rect, "change_color",
        lambda mouse_pos: controller.add_body(
            (mouse_pos[0], mouse_pos[1]),
            (mouse_pos[0], mouse_pos[1])
        )
    ),
    StrikeTool(
        controller,
        canvas.rect
    )
]

ui_system = UISystem(WIDTH, HEIGHT, controller, visualisator)

base_font = pygame.font.SysFont('arial', 14)

ui_system.add_element(canvas)
ui_system.add_element(ToolBar(0, 0, WIDTH, HEIGHT // 10, canvas, tools, create_empty_icon(), (128, 128, 128)))
ui_system.add_element(Button(WIDTH // 100, HEIGHT // 20, 40, 20, base_font, "Quit", create_empty_icon(), close))

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
