import pygame.draw

import pygame
from pygame.surface import Surface
from UI_object import UIObject


class Button(UIObject):
    def __init__(self, x: int, y: int, width: int, height: int, caption: str, icon, action):
        super().__init__(x, y, width, height, caption, icon, (128, 128, 128))

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def on_mouse_hover(self):
        pass

    def on_mouse_down(self):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_leave(self):
        pass

    def on_mouse_click(self):
        pass
