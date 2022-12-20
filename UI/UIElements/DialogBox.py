from pygame.surface import Surface

from UI.UIObject import UIObject, create_empty_icon

class DialogBox(UIObject):

    def __init__(self, x, y, width, height, font, caption, color, buttons, indent_y):
        super().__init__(x, y, width, height, font, caption, create_empty_icon(), color)
        self.buttons = buttons

        for i, button in enumerate(buttons):
            button.set_position(
                (x + width // 2 - button.rect.width // 2, y + height // 2 + (indent_y + button.rect.height) * i)
            )

    def event_handler(self, event):
        for button in self.buttons:
            button.event_handler(event)

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
        for button in self.buttons:
            button.draw(surface)