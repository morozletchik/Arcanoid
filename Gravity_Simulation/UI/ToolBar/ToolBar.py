
import os

from UI.UIObject import UIObject
from typing import Callable

from UI.Button import Button

from pygame.surface import Surface
import pygame.transform
from pygame.draw import rect
from pygame import image

from UI.Radio import Radio


class ToolBar(UIObject):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon, color):
        super().__init__(x, y, width, height, caption, icon, color)
        self.tools = {

        }

        button1_icon = image.load(os.path.join("UI", "Assets", "pointer.png"))
        button1_icon.convert()

        empty_icon = pygame.surface.Surface((900, 900), pygame.SRCALPHA, 32)
        empty_icon = empty_icon.convert_alpha()

        self._radio = Radio(
            x + width // 100 + 40 + 20,
            y + height // 2 - 5,
            width // 5,
            height // 2,
            "ToolButtons",
            empty_icon,
            (128, 128, 128)
        )

        self._tools = {

        }

    def event_handler(self, event):
        for key, tool in self._tools:
            tool.event_handler(event)
        self._radio.event_handler(event)

    def on_mouse_hover(self):
        pass

    def on_mouse_down(self):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_leave(self):
        pass

    def on_mouse_up(self):
        pass

    def draw(self, surface: Surface):
        rect(surface, self._color, self.rect)
        self._radio.draw(surface)


