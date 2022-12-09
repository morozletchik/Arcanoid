
from UI.UIObject import UIObject
from typing import Callable

from pygame.surface import Surface
from pygame.draw import rect


class Tool(object):
    pass


class ToolBar(UIObject):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon, color):
        super().__init__(x, y, width, height, caption, icon, color)
        self.tools = []
        self.elements = {}

    def update(self):
        pass

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
        rect(surface, self._color, self.rect)

