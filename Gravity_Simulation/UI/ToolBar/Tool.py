
import os
from abc import ABC

from UI.UIObject import UIObject
from typing import Callable

from UI.Button import Button

from pygame.surface import Surface
import pygame.transform
from pygame.draw import rect
from pygame import image

from UI.Radio import Radio


class BaseTool(UIObject, ABC):
    def __init__(self, width: int, height: int, caption: str):
        super().__init__(0, 0, width, height, caption, None, (0, 0, 0, 0))

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.is_mouse_in_rect():
                self.on_mouse_up()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_in_rect():
                self.on_mouse_down()

    def draw(self, surface: Surface):
        pass


class OneClickTool(BaseTool):
    def on_mouse_hover(self):
        pass

    def on_mouse_down(self):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_leave(self):
        pass

    def on_mouse_up(self):
        self._action(pygame.mouse.get_pos())

    def __init__(self, width: int, height: int, caption: str, action: Callable[[(int, int)], None]):
        super(BaseTool).__init__(width, height, caption)
        self._action = action



