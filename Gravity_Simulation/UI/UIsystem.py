

from Gravity_Simulation.UI.UIObject import UIObject
from Gravity_Simulation.UI.ToolBar.ToolBar import ToolBar
from Gravity_Simulation.UI.UIElements.UICanvas import Canvas


class UISystem(UIObject):
    def __init__(self, width, height, controller, visualisator):
        super().__init__(0, 0, width, height, "", None, (0, 0, 0, 0))

        self.__elements = {
            'Canvas': Canvas(0, height // 10, width, height - height // 10, "Canvas", visualisator),
        }

        self.__elements['ToolBar'] = ToolBar(
            0, 0,
            width, height // 10,
            self.__elements['Canvas'],
            controller,
            "ToolBar",
            (128, 128, 128)
        )

    def event_handler(self, event):
        for key, el in self.__elements.items():
            el.event_handler(event)

    def draw(self, surface):
        for key, el in self.__elements.items():
            el.draw(surface)

    def on_mouse_hover(self):
        for key, el in self.__elements.items():
            el.on_mouse_hover()

    def on_mouse_down(self):
        for key, el in self.__elements.items():
            el.on_mouse_down()

    def on_mouse_enter(self):
        for key, el in self.__elements.items():
            el.on_mouse_enter()

    def on_mouse_leave(self):
        for key, el in self.__elements.items():
            el.on_mouse_leave()

    def on_mouse_up(self):
        for key, el in self.__elements.items():
            el.on_mouse_up()

