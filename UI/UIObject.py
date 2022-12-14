
import pygame

from pygame.surface import Surface
from abc import ABC
from abc import abstractmethod
from pygame.rect import Rect
from enum import Enum
from pygame.font import Font
from pygame.font import SysFont
import pygame.mouse


def create_empty_icon():
    empty_icon = pygame.surface.Surface((900, 900), pygame.SRCALPHA, 32)
    empty_icon = empty_icon.convert_alpha()
    return empty_icon


def create_standard_font():
    return SysFont('arial', 12)


class MouseState(Enum):
    FREE = 1
    HOVER = 2
    FOCUS = 3


class UIObject(ABC):
    def __init__(
            self,
            x: int, y: int,
            width: int, height: int,
            font: Font, caption: str,
            icon: Surface, color
    ):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._font = font
        self._caption = caption
        self._icon = icon
        self._color = color
        self._mouse_state = MouseState.FREE

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

    @abstractmethod
    def on_mouse_up(self):
        pass

    @abstractmethod
    def draw(self, surface: Surface):
        pass

