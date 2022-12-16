

from UI.UIObject import UIObject
from pygame.surface import Surface
from UI.UIElements.Button import Button
from enum import Enum
import pygame


class RadioState(Enum):
    ACTIVE = 1
    INACTIVE = 2


class RadioButton(Button):
    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            caption: str,
            icon: Surface,
            radio
    ):
        super().__init__(x, y, width, height, caption, icon)
        self._radio_state = RadioState.INACTIVE
        self._radio = radio

    def event_handler(self, event):
        super(RadioButton, self).event_handler(event)

    def state_handler(self):
        super(RadioButton, self).state_handler()
        if self._radio_state == RadioState.ACTIVE:
            self.on_state_active()
        if self._radio_state == RadioState.INACTIVE:
            self.on_state_inactive()

    def on_state_active(self):
        self._color = (255, 255, 255)

    def on_state_inactive(self):
        self._color = (200, 200, 200)

    def on_mouse_down(self):
        super().on_mouse_down()
        self._radio_state = RadioState.ACTIVE
        self._radio.change_state(self)


class Radio(UIObject):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon: Surface, color, button_count):
        super().__init__(x, y, width, height, caption, icon, color)
        button_width = 40
        button_height = 20
        button_color = (200, 200, 200)
        indent_x = 10
        indent_y = 0
        icon = pygame.surface.Surface((width, height), pygame.SRCALPHA, 32)
        icon = icon.convert_alpha()
        self._buttons = [
            RadioButton(
                self._x + self._width // 2 - button_width // 2 + i * (button_width + indent_x),
                self._y + self._height // 2 - button_height // 2,
                button_width,
                button_height,
                "button1",
                icon,
                self
            ) for i in range(button_count)
        ]
        self._index_active_button = -1

    def change_state(self, radio_button: RadioButton):
        for i, b in enumerate(self._buttons):
            if b != radio_button:
                b._radio_state = RadioState.INACTIVE
            else:
                self._index_active_button = i

    @property
    def get_active_button(self):
        return self._buttons[self._index_active_button]

    @property
    def get_active_button_index(self):
        return self._index_active_button

    def event_handler(self, event):
        for b in self._buttons:
            b.event_handler(event)

    def draw(self, surface: Surface):
        for el in self._buttons:
            el.draw(surface)

    def on_mouse_up(self):
        pass

    def on_mouse_down(self):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_hover(self):
        pass

    def on_mouse_leave(self):
        pass

