

import pygame
from pygame.surface import Surface

from UIObject import UIObject


class Canvas(UIObject):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon: Surface):
        super().__init__(x, y, width, height, caption, icon, (0, 0, 0))

    def on_mouse_hover(self):
        pass

    def on_mouse_down(self):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_leave(self):
        pass

    def on_mouse_click(self):
        pass

    def draw(self, surface: Surface):
        #TODO: связать canvas с визуализатором
        pass

    def event_handler(self, event):
        pass
