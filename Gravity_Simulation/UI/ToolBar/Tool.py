from abc import ABC

from UI.UIObject import UIObject
from typing import Callable

from pygame.surface import Surface
import pygame.transform
from pygame.rect import Rect


class BaseTool(UIObject, ABC):
    def __init__(self, action_rect: Rect, caption: str):
        super().__init__(action_rect.x, action_rect.y, action_rect.width, action_rect.height, caption, None, (0, 0, 0, 0))
        self._mouse_is_pressed = False

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.on_mouse_up()
            self._mouse_is_pressed = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_in_rect():
                self.on_mouse_down()
                self._mouse_is_pressed = True

        if self._mouse_is_pressed:
            self.on_mouse_pressed()

    def on_mouse_pressed(self):
        pass

    def on_mouse_hover(self):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_leave(self):
        pass

    def draw(self, surface: Surface):
        pass


class ClickTool(BaseTool):
    """Класс инструмента, требующий одного нажатия"""

    def __init__(self, action_rect: Rect, caption: str, action: Callable[[(int, int)], None]):
        super().__init__(action_rect, caption)
        self._action = action

    def on_mouse_down(self):
        self._action(pygame.mouse.get_pos())

    def on_mouse_up(self):
        pass


class DragTool(BaseTool):
    """Класс инструмента, действующий при зажатой кнопке мыши и действующий при движении мыши"""

    def __init__(
            self,
            action_rect: Rect,
            caption: str,
            on_mouse_down_action: Callable[[(int, int), (int, int)], None],
            on_mouse_up_action: Callable[[(int, int), (int, int)], None]
    ):
        super().__init__(action_rect, caption)
        self._on_mouse_down_action = on_mouse_down_action
        self._on_mouse_up_action = on_mouse_up_action
        self._start_pos = None

    def on_mouse_down(self):
        if not self._mouse_is_pressed:
            self._mouse_is_pressed = True
            self._start_pos = pygame.mouse.get_pos()

    def on_mouse_pressed(self):
        cur_pos = pygame.mouse.get_pos()
        self._on_mouse_down_action(self._start_pos, cur_pos)

    def on_mouse_up(self):
        if self._mouse_is_pressed:
            self._on_mouse_up_action(self._start_pos, pygame.mouse.get_pos())
            self._start_pos = None
            self._mouse_is_pressed = False



