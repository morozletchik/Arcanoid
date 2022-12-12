
import pygame

from pygame.surface import Surface
from abc import ABC
from abc import abstractmethod
from pygame.rect import Rect
from enum import Enum
import pygame.mouse


class MouseState(Enum):
    FREE = 1
    HOVER = 2
    FOCUS = 3


class UIObject(ABC):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon: Surface, color):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._caption = caption
        self._icon = icon
        self._color = color
        self._state = MouseState.FREE

    @property
    def rect(self):
        return Rect(self._x, self._y, self._width, self._height)

    @abstractmethod
    def event_handler(self, event):
        pass

    def local2world(self, x, y):
        return x + self._x, y + self._y

    def world2local(self, x, y):
        return x - self._x, y - self._y

    @abstractmethod
    def on_mouse_hover(self):
        pass

    @abstractmethod
    def on_mouse_down(self):
        pass

    @abstractmethod
    def on_mouse_enter(self):
        pass

    @abstractmethod
    def on_mouse_leave(self):
        pass

    def is_mouse_in_rect(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(*mouse_pos)

    def change_hover_or_focus_state(self):
        if self.is_mouse_in_rect():
            self._state = MouseState.HOVER
        else:
            self._state = MouseState.FREE

    @abstractmethod
    def on_mouse_click(self):
        pass

    @abstractmethod
    def draw(self, surface: Surface):
        pass

