import pygame.draw

import pygame
from pygame.surface import Surface
from UI.UIObject import UIObject
from UI.UIObject import MouseState
import pygame.mouse as mouse
import pygame.image
from pygame.font import Font

from typing import Callable


class Button(UIObject):
    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            font: Font,
            caption: str,
            icon: Surface,
            action: Callable[[], None] = lambda: None
    ):
        super().__init__(x, y, width, height, font, caption, icon, (200, 200, 200))

        new_size = min(self._width, self._height)
        self._icon = pygame.transform.scale(self._icon, (new_size, )*2)
        self._font_surface = font.render(self._caption, True, (0, 0, 0))

        self._action = action

    def event_handler(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.change_hover_or_free_state()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._mouse_state == MouseState.HOVER:
                self.on_mouse_down()

        if event.type == pygame.MOUSEBUTTONUP:
            self.on_mouse_up()

        self.state_handler()

    def state_handler(self):
        if self._mouse_state == MouseState.HOVER:
            self.on_mouse_hover()
        elif self._mouse_state == MouseState.FREE:
            self.on_mouse_free()

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, self._color, self.rect, border_radius=4)

        icon_rect = self._icon.get_rect()
        icon_rect = icon_rect.move(
            self._x + self._width // 2 - icon_rect.width // 2,
            self._y + self._height // 2 - icon_rect.height // 2
        )

        font_rect = self._font_surface.get_rect()
        font_rect = font_rect.move(
            self._x + self._width // 2 - font_rect.width // 2,
            self._y + self._height // 2 - font_rect.height // 2
        )

        surface.blit(self._icon, icon_rect)
        surface.blit(self._font_surface, font_rect)

    def on_mouse_hover(self):
        self._color = (190, 190, 190)

    def on_mouse_free(self):
        self._color = (200, 200, 200)

    def on_mouse_down(self):
        self._mouse_state = MouseState.FOCUS
        self._action()

    def on_mouse_up(self):
        self.change_hover_or_free_state()

    def on_mouse_enter(self):
        self._mouse_state = MouseState.HOVER

    def on_mouse_leave(self):
        self._mouse_state = MouseState.FREE

    def on_mouse_click(self):
        pass

    def change_hover_or_free_state(self):
        if self.is_mouse_in_rect():
            self._mouse_state = MouseState.HOVER
        else:
            self._mouse_state = MouseState.FREE


