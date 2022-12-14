import pygame

import os

from Simulation.Simulation import *
from pygame.surface import Surface
from pygame.draw import circle, rect
from pygame.rect import Rect
from pygame.font import Font


def stretch(surface, width, height):
    '''
    stretches an image
    :param width: width of the screen
    :param height: height of the screen
    '''
    surface = pygame.transform.scale(surface, (width, height))
    return surface

class Visualisator(object):

    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self._view_point = (0, 0)
        self._scale = 1
        self._font = Font(os.path.join("Assets", "Multiround Pro", "MultiroundPro.otf"), 50)
        self.background_image = pygame.image.load(os.path.join("Assets", "background.jpg"))
        self.heart_image = pygame.image.load(os.path.join("Assets", "heart.png"))

    def from_screen_to_world_coordinates(self, position, rect: Rect):
        '''
        converts screen usual coord into coord with (0,0) in the centre
        :param position: pos in usual screen coord
        :param rect: rect which coord are converted
        :return: position x, position y
        '''
        return (
            (position[0] - rect.width / 2) / self.scale + self.view_point[0],
            (position[1] - rect.height / 2) / self.scale + self.view_point[1]
        )

    def from_world_to_screen_coordinates(self, position, rect: Rect):
        '''
        converts coord with (0,0) in the centre into screen usual coord
        :param position: pos in coord with (0,0) in the centre
        :param rect: rect which coord are converted
        :return: x, y - screen coord
        '''
        x = (position[0] - self._view_point[0]) * self._scale + rect.width // 2
        y = (position[1] - self._view_point[1]) * self._scale + rect.height // 2

        return x, y

    def visualize(self, width, height) -> Surface:
        '''
        visualises the game: background, lives and all the game objects
        :param width: game window width
        :param height: game window height
        :return: surface with images and objects on it
        '''
        self.background_image = stretch(self.background_image, width, height)
        self.heart_image = stretch(self.heart_image, height // 20, height // 20)
        surface = Surface((width, height), flags=pygame.SRCALPHA)
        surface.blit(self.background_image, (0, 0), Rect(0, 0, width, height))
        for obj in self.simulation.objects:
            if type(obj) == Ball:
                (x, y) = self.from_world_to_screen_coordinates((obj.x, obj.y), Rect(0, 0, width, height))
                radius = obj.r * self._scale
                circle(surface, obj.color, (x, y), radius)
            if type(obj) in [Rectangle, Brick, AcceleratingWall, Paddle]:
                (x, y) = self.from_world_to_screen_coordinates((obj.x, obj.y), Rect(0, 0, width, height))
                scaled_width = int(obj.width * self._scale)
                scaled_height = int(obj.height * self._scale)
                rect(surface, obj.color, Rect(
                    x - scaled_width // 2, y - scaled_height // 2,
                    scaled_width, scaled_height)
                )

        text_score = self._font.render(f"{self.simulation.score}", True, (255, 255, 255))
        surface.blit(text_score, (width//2 - 10, 10))

        for i in range(self.simulation.lives):
            surface.blit(self.heart_image, (width // 200 + i * self.heart_image.get_width(), height // 200))

        return surface

    def change_view_point(self, new_view_point):
        self._view_point = new_view_point

    @property
    def view_point(self):
        return self._view_point

    def change_scale(self, new_scale):
        self._scale = new_scale

    @property
    def scale(self):
        return self._scale
