
import os

from UI.UIObject import UIObject

from pygame.surface import Surface
import pygame.transform
from pygame.draw import rect
from pygame import image

from UI.UIElements.Radio import Radio
from UI.ToolBar.Tool import *
from UI.UIElements.UICanvas import Canvas


class ToolBar(UIObject):
    def __init__(
            self,
            x: int, y: int,
            width: int, height: int,
            canvas: Canvas,
            caption: str,
            color: (int, int, int)
    ):
        super().__init__(x, y, width, height, caption, None, color)

        button1_icon = image.load(os.path.join("UI", "Assets", "pointer.png"))
        button1_icon.convert()

        empty_icon = pygame.surface.Surface((900, 900), pygame.SRCALPHA, 32)
        empty_icon = empty_icon.convert_alpha()

        self._tools = [
            ClickTool(canvas.rect, "change_color", lambda mouse_pos: canvas.change_color()),
            DragTool(
                canvas.rect,
                "change_color_with_mouse",
                lambda mouse_pos_start, mouse_pos:
                    canvas.change_color_with_mouse(
                        (
                            min(int(((mouse_pos[0] - mouse_pos_start[0]) / canvas.rect.width) * 256), 255),
                            min(int(((mouse_pos[1] - mouse_pos_start[1]) / canvas.rect.height) * 256), 255)
                        )
                    ),
                lambda a, b: None
            ),
            None
        ]

        self._radio = Radio(
            x + width // 100 + 40 + 20,
            y + height // 2 - 5,
            width // 5,
            height // 2,
            "ToolButtons",
            empty_icon,
            (128, 128, 128),
            len(self._tools)
        )

    @property
    def active_tool(self) -> BaseTool:
        index = self._radio.get_active_button_index
        if index == -1:
            return None
        return self._tools[index]

    def event_handler(self, event):
        self._radio.event_handler(event)
        if self.active_tool:
            self.active_tool.event_handler(event)

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
        rect(surface, self._color, self.rect)
        self._radio.draw(surface)


