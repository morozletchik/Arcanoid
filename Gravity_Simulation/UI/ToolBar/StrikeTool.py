

from pygame.rect import Rect
from Gravity_Simulation.Controller.Controller import Controller
from Gravity_Simulation.UI.ToolBar.Tool import DragTool


class StrikeTool(DragTool):

    def __init__(self, controller: Controller, action_rect: Rect):

        def on_mouse_up_action(start_mouse_pos, cur_mouse_pos):
            controller.strike(
                (start_mouse_pos[0] - action_rect.x, start_mouse_pos[1] - action_rect.y),
                (cur_mouse_pos[0] - action_rect.x, cur_mouse_pos[1] - action_rect.y)
            )

        super().__init__(
            action_rect,
            "strike_tool",
            lambda a, b: None,
            on_mouse_up_action
        )
        self._controller = controller

