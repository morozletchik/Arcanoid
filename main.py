

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

from pygame.event import Event

from screeninfo import get_monitors


class Module(ABC):
    def __init__(self, width, height):
        pass

    def draw(self, screen: Surface):
        pass

    def update(self, delta_time: float):
        pass

    def event_handler(self, event: Event):
        pass


class MainMenuModule(Module):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.ui_system = UISystem(WIDTH, HEIGHT)
        base_font = pygame.font.SysFont('arial', 36)

        self.ui_system.add_element(
            Button(
                WIDTH // 2 - 30, HEIGHT // 3,
                200, 100,
                base_font, "Начать игру",
                create_empty_icon(),
                change_module
            )
        )
        self.ui_system.add_element(
            Button(
                WIDTH // 2 - 30, HEIGHT // 3 + 150,
                200, 100,
                base_font, "Выход",
                create_empty_icon(),
                close
            )
        )

    def draw(self, surface: Surface):
        surface.fill((255, 255, 255))
        self.ui_system.draw(surface)

    def update(self, delta_time: float):
        pass

    def event_handler(self, event: Event):
        self.ui_system.event_handler(event)


class MainGameModule(Module):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.simulation = Simulation()
        self.simulation.add_wall(-WIDTH / 2, 0, 20, HEIGHT)
        self.simulation.add_wall(WIDTH / 2, 0, 20, HEIGHT)
        self.simulation.add_wall(0, HEIGHT / 2, WIDTH, 20)
        self.simulation.add_wall(0, -HEIGHT / 2, WIDTH, 20)

        self.

        self.ui_system = UISystem(WIDTH, HEIGHT)

        self.visualisator = Visualisator(self.simulation)
        self.visualisator.change_view_point((0, 0))
        self.visualisator.change_scale(0.75)

        canvas = Canvas(0, HEIGHT // 10, WIDTH, HEIGHT - HEIGHT // 10, "Canvas", self.visualisator)
        self.controller = Controller(canvas.rect, self.simulation, self.visualisator)

        tools = [
            ClickTool(
                canvas.rect, "change_color",
                lambda mouse_pos: self.controller.add_body(
                    (mouse_pos[0], mouse_pos[1]),
                    (mouse_pos[0], mouse_pos[1])
                )
            ),
            StrikeTool(
                self.controller,
                self.ui_system,
                canvas.rect
            )
        ]

        base_font = pygame.font.SysFont('arial', 14)

        toolbar = ToolBar(
            0, 0,
            WIDTH, HEIGHT // 10,
            canvas, tools, create_empty_icon(), (128, 128, 128)
        )

        toolbar.add_element(
            Button(
                width - 100 - 20, height // 10 // 2 - 30,
                100, 60,
                base_font, "Главное меню",
                create_empty_icon(), change_module
            )
        )

        self.ui_system.add_element(canvas)
        self.ui_system.add_element(
            toolbar
        )

    def update(self, delta_time: float):
        for i in range(10):
            self.simulation.update(delta_time)

    def draw(self, screen: Surface):
        self.ui_system.draw(screen)

    def event_handler(self, event: Event):
        self.ui_system.event_handler(event)


def close():
    global running
    running = False


def change_module():
    global module

    if type(module) == MainGameModule:
        module = MainMenuModule(WIDTH, HEIGHT)

    else:
        module = MainGameModule(WIDTH, HEIGHT)

running = True

WIDTH = get_monitors()[0].width - 50
HEIGHT = get_monitors()[0].height - 50

FPS = 30

pygame.init()
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)
clock = pygame.time.Clock()

module = MainMenuModule(WIDTH, HEIGHT)

while running:
    dt = clock.tick(FPS) / 1000

    module.update(dt)

    screen.fill((0, 0, 0))
    module.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():

        module.event_handler(event)

        if event.type == pygame.QUIT:
            running = False

sys.exit()
