from pygame.surface import Surface

from UI.UIObject import UIObject, create_empty_icon

class DialogBox(UIObject):

    def __init__(self, x, y, width, height, font, caption, color, buttons):
        super().__init__(x, y, width, height, font, caption, create_empty_icon(), color, buttons)
        self.buttons = buttons



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
        pass