import sys
import os
from abc import ABC
import pygame
from pygame import Surface
from UI.UIsystem import UISystem
from UI.UIElements.UICanvas import Canvas
from UI.UIObject import create_empty_icon
from Simulation.Simulation import Simulation
from Controller.Controller import Controller
from Visualisator.Visualisator import Visualisator
from pygame.rect import Rect
from UI.ToolBar.Tool import ClickTool
from UI.ToolBar.ToolBar import ToolBar
from UI.ToolBar.StrikeTool import StrikeTool
from UI.UIElements.Button import Button
from UI.UIElements.TextBox import TextBox
from UI.UIElements.DialogBox import DialogBox

from pygame.event import Event

from screeninfo import get_monitors

GRAY = (128, 128, 128)

pygame.init()
pygame.font.init()


class Module(ABC):
    def __init__(self, width, height):
        pass

    def draw(self, screen: Surface):
        pass

    def update(self, delta_time: float):
        pass

    def event_handler(self, event: Event):
        pass

    def on_setup(self):
        pass

class MainMenuModule(Module):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.ui_system = UISystem(WIDTH, HEIGHT)
        base_font = pygame.font.SysFont('arial', 48)

        header_font = pygame.font.Font(os.path.join("UI", "Assets", "Multiround Pro", "MultiroundPro.otf"), 160)
        if not header_font:
            header_font = pygame.font.get_default_font()

        self.ui_system.add_element(
            TextBox(
                WIDTH // 2 - 450, HEIGHT // 5,
                header_font, "Arcanoid", (230, 0, 0)
            )
        )

        button_block_position = 200
        button_width = 400
        button_height = 100

        self.ui_system.add_element(
            Button(
                WIDTH // 2 - button_width // 2, HEIGHT // 3 + button_block_position,
                button_width, button_height,
                base_font, "Начать игру",
                create_empty_icon(),
                change_module
            )
        )
        self.ui_system.add_element(
            Button(
                WIDTH // 2 - button_width // 2, HEIGHT // 3 + button_block_position + button_height + 50,
                button_width, button_height,
                base_font, "Выход",
                create_empty_icon(),
                close
            )
        )

    def draw(self, surface: Surface):
        surface.fill((0, 0, 150))
        self.ui_system.draw(surface)

    def update(self, delta_time: float):
        pass

    def on_setup(self):
        pygame.mouse.set_visible(True)

    def event_handler(self, event: Event):
        self.ui_system.event_handler(event)


class MainGameModule(Module):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.simulation = Simulation(WIDTH, HEIGHT)
        self.simulation.setup()

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

        base_font = pygame.font.SysFont('arial', 28)
        header_font = pygame.font.SysFont('arial', 128)
        game_over_font = pygame.font.SysFont('arial', 256)

        self.game_over_text = TextBox(
                    WIDTH // 2 - 500, HEIGHT // 2 - 200,
                    game_over_font, "Game Over", (255, 0, 0)
                )

        self.dialog_box = DialogBox(
            width // 2 - 300, height // 2 - 300,
            600, 600,
            header_font, "Пауза",
            GRAY,
            [
                Button(
                    0, 0, 200, 100,
                    base_font, "Продолжить",
                    create_empty_icon(), lambda: self.ui_system.remove_element(self.dialog_box)
                ),
                Button(
                    0, 0, 200, 100,
                    base_font, "В главное меню",
                    create_empty_icon(), change_module
                )
            ], 20
        )

        self.ui_system.add_element(canvas)

    def on_setup(self):
        pygame.mouse.set_visible(False)

    def update(self, delta_time: float):
        for i in range(10):
            self.simulation.update(delta_time)
        if self.simulation.is_game_over():
            self.ui_system.add_element(
                self.game_over_text
            )

    def draw(self, screen: Surface):
        self.ui_system.draw(screen)

    def event_handler(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.ui_system.have_element(self.dialog_box):
                    self.ui_system.remove_element(self.dialog_box)
                    pygame.mouse.set_visible(False)
                    self.controller.continue_simulation()
                else:
                    self.ui_system.add_element(self.dialog_box)
                    pygame.mouse.set_visible(True)
                    self.controller.pause_simulation()

        self.ui_system.event_handler(event)
        self.controller.event_handler(event)


def close():
    global running
    running = False


def change_module():
    global module

    if type(module) == MainGameModule:
        module = MainMenuModule(WIDTH, HEIGHT)

    else:
        module = MainGameModule(WIDTH, HEIGHT)
    module.on_setup()


running = True

WIDTH = get_monitors()[0].width - 50
HEIGHT = get_monitors()[0].height - 50

FPS = 30


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT), pygame.FULLSCREEN
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
