

from pygame.surface import Surface
from abc import ABC
from abc import abstractmethod
from pygame.rect import Rect


class UIObject(ABC):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon, color: Any):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.caption = caption
        self.icon = icon
        self.color = color

    @property
    def rect(self):
        return Rect(self.x, self.y, self.width, self.height)

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

    @abstractmethod
    def on_mouse_click(self):
        pass

    @abstractmethod
    def draw(self, surface: Surface):
        pass
