import pygame

from src.controller.AssetController import load_bluebird_downflap, load_bluebird_midflap, load_bluebird_upflap


class Bird(pygame.sprite.Sprite):
    __current_image = 0
    initial_speed = 10
    current_speed = 10
    gravity_speed = 1.5

    def __init__(self, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.images = [load_bluebird_upflap(), load_bluebird_midflap(), load_bluebird_downflap()]

        self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = screen_size[0] / 2
        self.rect[1] = screen_size[1] / 2

    def update(self):
        self.__current_image = (self.__current_image + 1) % 3
        self.image = self.images[self.__current_image]

        self.current_speed += self.gravity_speed
        self.rect[1] += self.current_speed

    def bump(self):
        self.current_speed = -self.initial_speed
