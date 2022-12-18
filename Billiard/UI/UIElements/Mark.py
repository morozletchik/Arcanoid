from pygame.surface import Surface

from Billiard.UI.UIObject import *


class Mark(UIObject):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius, create_standard_font(), "", create_empty_icon(), (255, 0, 0))

    def event_handler(self, event):
        pass

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
        pygame.draw.circle(surface, self._color, (self._x, self._y), self._width, self._width // 3)

