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
from UI.UIElements.Button import Button
from UI.UIElements.TextBox import TextBox
from UI.UIElements.DialogBox import DialogBox
from Visualisator.Visualisator import stretch

from pygame.event import Event

from screeninfo import get_monitors

GRAY = (128, 128, 128)

pygame.init()
pygame.font.init()

# шрифты для главного меню
base_font1 = pygame.font.Font(os.path.join("Assets", "retro_font1.ttf"), 32)
header_font1 = pygame.font.Font(os.path.join("Assets", "retro_font.ttf"), 200)

# шрифты для основной игры
base_font2 = pygame.font.Font(os.path.join("Assets", "retro_font1.ttf"), 14)
header_font2 = pygame.font.Font(os.path.join("Assets", "retro_font1.ttf"), 64)
final_font = pygame.font.Font(os.path.join("Assets", "retro_font1.ttf"), 100)
hint_font = pygame.font.Font(os.path.join("Assets", "retro_font1.ttf"), 32)


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

        self.ui_system.add_element(
            TextBox(
                WIDTH // 2 - 600, HEIGHT // 5,
                header_font1, "Arcanoid", (230, 0, 0)
            )
        )

        button_block_position = 200
        button_width = 400
        button_height = 100

        self.ui_system.add_element(
            Button(
                WIDTH // 2 - button_width // 2, HEIGHT // 3 + button_block_position,
                button_width, button_height,
                base_font1, "Начать игру",
                create_empty_icon(),
                change_module
            )
        )
        self.ui_system.add_element(
            Button(
                WIDTH // 2 - button_width // 2, HEIGHT // 3 + button_block_position + button_height + 50,
                button_width, button_height,
                base_font1, "Выход",
                create_empty_icon(),
                close
            )
        )

    def draw(self, surface: Surface):
        '''
        draws menu background
        :param surface:
        '''
        menu_back = pygame.image.load(os.path.join("Assets", "menyu.png"))
        menu_back = stretch(menu_back, WIDTH, HEIGHT)
        surface.blit(menu_back, (0, 0), Rect(0, 0, WIDTH, HEIGHT))
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
        self.simulation.add_on_change_state_event(self.on_change_simulation_state)

        self.ui_system = UISystem(WIDTH, HEIGHT)

        self.visualisator = Visualisator(self.simulation)
        self.visualisator.change_view_point((0, 0))
        self.visualisator.change_scale(0.75)

        canvas = Canvas(0, 0, WIDTH, HEIGHT, "Canvas", self.visualisator)
        self.controller = Controller(canvas.rect, self.simulation, self.visualisator)

        self.hint_text1 = TextBox(
            WIDTH // 2 - 350, 7/12 * HEIGHT,
            hint_font, "Нажмите Esc, чтобы, \nперейти в главное меню", (255, 255, 255)
        )

        self.hint_text2 = TextBox(
            WIDTH // 2 - 350, HEIGHT // 2,
            hint_font, "Нажмите Space,чтобы начать", (255, 255, 255)
        )

        self.game_over_text = TextBox(
            WIDTH // 2 - 450, HEIGHT // 3,
            final_font, "Game Over", (255, 0, 0)
        )

        self.win_text = TextBox(
            WIDTH // 2 - 500, HEIGHT // 2 - 200,
            final_font, "Вы победили!", (0, 255, 0)
        )

        self.dialog_box = DialogBox(
            width // 2 - 300, height // 2 - 300,
            600, 600,
            header_font2, "Пауза",
            GRAY,
            [
                Button(
                    0, 0, 200, 100,
                    base_font2, "Продолжить",
                    create_empty_icon(), self.on_continue
                ),
                Button(
                    0, 0, 200, 100,
                    base_font2, "В главное меню",
                    create_empty_icon(), change_module
                )
            ], 20
        )

        self.ui_system.add_element(canvas)

    def on_continue(self):
        '''
        removes dial box and makes mouse invis
        when pause is finished
        :return:
        '''
        self.ui_system.remove_element(self.dialog_box)
        pygame.mouse.set_visible(False)
        self.simulation.continue_simulation()

    def on_setup(self):
        '''
        makes mouse invisible
        :return:
        '''
        pygame.mouse.set_visible(False)

    def on_change_simulation_state(self):
        '''
        changes windows: main menu, game, pause, go or victory
        :return:
        '''
        if self.ui_system.have_element(self.game_over_text):
            self.ui_system.remove_element(self.game_over_text)
        if self.ui_system.have_element(self.win_text):
            self.ui_system.remove_element(self.win_text)
        if self.ui_system.have_element(self.hint_text2):
            self.ui_system.remove_element(self.hint_text2)
        if self.ui_system.have_element(self.hint_text1):
            self.ui_system.remove_element(self.hint_text1)

        if self.simulation.is_game_over():
            self.ui_system.add_element(
                self.game_over_text
            )
        if self.simulation.is_win():
            self.ui_system.add_element(
                self.win_text
            )
        if self.simulation.is_ready():
            self.ui_system.add_element(
                self.hint_text2
            )

        if self.simulation.is_win() or self.simulation.is_game_over():
            self.ui_system.add_element(
                self.hint_text1
            )

    def update(self, delta_time: float):
        '''
        updates screen after small period of time
        :param delta_time: small period of time
        :return:
        '''
        self.simulation.update(delta_time)

    def draw(self, screen: Surface):
        '''
        draws screen
        :param screen:
        '''
        self.ui_system.draw(screen)

    def event_handler(self, event: Event):
        '''
        processes events such as mouse movement and pressing keys
        :param event:
        :return:
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not (self.simulation.is_win() or self.simulation.is_game_over()):
                    if self.ui_system.have_element(self.dialog_box):
                        self.ui_system.remove_element(self.dialog_box)
                        pygame.mouse.set_visible(False)
                        self.controller.continue_simulation()
                    else:
                        self.ui_system.add_element(self.dialog_box)
                        pygame.mouse.set_visible(True)
                        self.controller.pause_simulation()
                else:
                    change_module()

        self.ui_system.event_handler(event)
        self.controller.event_handler(event)


def close():
    '''
    closes the game window
    :return:
    '''
    global running
    running = False


def change_module():
    '''
    changes game module
    :return:
    '''
    global module

    if type(module) == MainGameModule:
        module = MainMenuModule(WIDTH, HEIGHT)

    else:
        module = MainGameModule(WIDTH, HEIGHT)
    module.on_setup()


running = True

WIDTH = get_monitors()[0].width
HEIGHT = get_monitors()[0].height

FPS = 60

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
