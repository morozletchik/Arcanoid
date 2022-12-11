
import os

from UI.UIObject import UIObject
from typing import Callable

from UI.Button import Button

from pygame.surface import Surface
import pygame.transform
from pygame.draw import rect
from pygame import image


class Tool(object):
    def __init__(self, action: Callable):
        self._action = action


class ToolBar(UIObject):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon, color):
        super().__init__(x, y, width, height, caption, icon, color)
        self.tools = {

        }

        button1_icon = image.load(os.path.join("UI", "Assets", "pointer.png"))
        button1_icon.convert()

        self._elements = {
            "Button1": Button(
                x + width // 100 + 5,
                y + height//2 - 5,
                40,
                20,
                "Button1",
                button1_icon,
                lambda: print("Hello, world")
            )
        }

    def event_handler(self, event):
        for key, el in self._elements.items():
            el.event_handler(event)

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
        for key, el in self._elements.items():
            el.draw(surface)


