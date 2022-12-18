
import os

from Billiard.Controller.Controller import Controller

from Billiard.UI.UIObject import *

from pygame.surface import Surface
import pygame.transform
from pygame.draw import rect
from pygame import image

from Billiard.UI.UIElements.Radio import Radio
from Billiard.UI.ToolBar.Tool import *
from Billiard.UI.UIElements.UICanvas import Canvas

from Billiard.UI.ToolBar.StrikeTool import StrikeTool

class ToolBar(UIObject):

    def __init__(
            self,
            x: int, y: int,
            width: int, height: int,
            canvas: Canvas,
            tools: list[BaseTool],
            icon: Surface,
            color: (int, int, int)
    ):
        super().__init__(x, y, width, height, None, "", icon, color)

        self._tools = tools

        self._elements = [Radio(
            x + width // 100 + 40 + 20, y + height // 2 - 30,
            100, 60,
            create_standard_font(), "ToolButtons",
            icon,
            (128, 128, 128),
            len(tools)
        )]

    @property
    def _radio(self):
        return [i for i in self._elements if type(i) == Radio][0]

    @property
    def active_tool(self) -> BaseTool:
        index = self._radio.get_active_button_index
        if index == -1:
            return None
        return self._tools[index]

    def event_handler(self, event):
        for el in self._elements:
            el.event_handler(event)
        if self.active_tool:
            self.active_tool.event_handler(event)

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
        for el in self._elements:
            el.draw(surface)

    def add_element(self, obj: UIObject):
        self._elements.append(obj)


