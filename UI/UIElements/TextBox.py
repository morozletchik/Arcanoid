from pygame.surface import Surface

from UI.UIObject import create_empty_icon
from UI.UIObject import UIObject

class TextBox(UIObject):

    def __init__(self, x, y, font, caption, color):
        super().__init__(x, y, 10, 10, font, caption, create_empty_icon(), color)

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
        text = self._font.render(self._caption, True, self._color)
        surface.blit(text, (self._x, self._y))


