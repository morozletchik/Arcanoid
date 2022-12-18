

from .UIObject import UIObject


class UISystem(UIObject):
    def __init__(self, width, height):
        super().__init__(0, 0, width, height, None, "", None, (0, 0, 0, 0))
        self.elements = []

    def event_handler(self, event):
        for el in self.elements:
            el.event_handler(event)

    def draw(self, surface):
        for el in self.elements:
            el.draw(surface)

    def on_mouse_hover(self):
        for el in self.elements:
            el.on_mouse_hover()

    def on_mouse_down(self):
        for el in self.elements:
            el.on_mouse_down()

    def on_mouse_enter(self):
        for el in self.elements:
            el.on_mouse_enter()

    def on_mouse_leave(self):
        for el in self.elements:
            el.on_mouse_leave()

    def on_mouse_up(self):
        for el in self.elements:
            el.on_mouse_up()

    def add_element(self, obj: UIObject):
        self.elements.append(obj)

    def del_element(self, obj: UIObject):
        self.elements.remove(obj)

