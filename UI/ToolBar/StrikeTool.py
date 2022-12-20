

from pygame.rect import Rect
from Controller.Controller import Controller
from UI.ToolBar.Tool import DragTool
from UI.UIsystem import UISystem
from UI.UIElements.Mark import Mark


class StrikeTool(DragTool):

    def __init__(self, controller: Controller, ui_system: UISystem, action_rect: Rect):
        self._mark = None

        def on_mouse_down_action(start_mouse_pos, cur_mouse_pos):
            if not self._mark:
                self._mark = Mark(start_mouse_pos[0], start_mouse_pos[1], 10)
                ui_system.add_element(self._mark)

        def on_mouse_up_action(start_mouse_pos, cur_mouse_pos):
            controller.strike(
                (start_mouse_pos[0] - action_rect.x, start_mouse_pos[1] - action_rect.y),
                (cur_mouse_pos[0] - action_rect.x, cur_mouse_pos[1] - action_rect.y)
            )
            ui_system.remove_element(self._mark)
            self._mark = None

        super().__init__(
            action_rect,
            "strike_tool",
            on_mouse_down_action,
            on_mouse_up_action
        )
        self._controller = controller

