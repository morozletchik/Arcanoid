

import pygame
from pygame.surface import Surface

from UI.UIObject import UIObject


class Canvas(UIObject):

    def __init__(self, x: int, y: int, width: int, height: int, caption: str):
        super().__init__(x, y, width, height, caption, None, (0, 0, 0))
        self._surface = Surface((width, height))

        # for test
        self._color = (0, 0, 255)

    def draw(self, surface: Surface):
        #TODO: связать canvas с визуализатором

        self._surface.fill(self._color)

        surface.blit(self._surface, (self._x, self._y))

    # тестовый метод
    def change_color(self):
        if self._color == (0, 0, 255):
            self._color = (0, 0, 0)
        else:
            self._color = (0, 0, 255)

    # тестовый метод
    def change_color_with_mouse(self, new_color):
        self._color = (
            new_color[0],
            new_color[1],
            self._color[2]
        )
        print(self._color)

    def event_handler(self, event):
        pass

    def on_mouse_hover(self):
        pass

    def on_mouse_up(self):
        pass

    def on_mouse_down(self):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_leave(self):
        pass

    def on_mouse_click(self):
        pass

