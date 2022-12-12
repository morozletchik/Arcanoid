import pygame.draw

import pygame
from pygame.surface import Surface
from UI.UIObject import UIObject
from UI.UIObject import MouseState
import pygame.mouse as mouse
import pygame.image

from typing import Callable


class Button(UIObject):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon, action: Callable[[], None]):
        super().__init__(x, y, width, height, caption, icon, (200, 200, 200))

        new_size = min(self._width, self._height)
        self._icon = pygame.transform.scale(self._icon, (new_size, )*2)

        # FIXME: сделать так, чтобы иконка была по центру

        self._action = action

    def event_handler(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.change_hover_or_focus_state()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_mouse_down()

        if event.type == pygame.MOUSEBUTTONUP:
            self.on_mouse_up()

        self.state_handler()

    def state_handler(self):
        if self._state == MouseState.HOVER:
            self.on_mouse_hover()
        elif self._state == MouseState.FREE:
            self.on_mouse_free()

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, self._color, self.rect, border_radius=4)
        icon_rect = self._icon.get_rect()
        icon_rect = icon_rect.move(self._x + self._width // 2 - icon_rect.width // 2, self._y + self._height // 2 - icon_rect.height // 2)
        surface.blit(self._icon, icon_rect)

    def on_mouse_hover(self):
        self._color = (190, 190, 190)

    def on_mouse_free(self):
        self._color = (200, 200, 200)

    def on_mouse_down(self):
        if self._state == MouseState.HOVER:
            self._state = MouseState.FOCUS
            self._action()

    def on_mouse_up(self):
        self.change_hover_or_focus_state()

    def on_mouse_enter(self):
        self._state = MouseState.HOVER

    def on_mouse_leave(self):
        self._state = MouseState.FREE

    def on_mouse_click(self):
        pass


