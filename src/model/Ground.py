import pygame

from src.controller.AssetController import load_base_ground


class Ground(pygame.sprite.Sprite):
    game_speed = 10

    def __init__(self, screen_size, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.GROUND_WIDTH = 2 * screen_size[0]
        self.GROUND_HEIGTH = 100

        self.image = load_base_ground((self.GROUND_WIDTH, self.GROUND_HEIGTH))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos - 20
        self.rect[1] = screen_size[1] - self.GROUND_HEIGTH

    def update(self):
        self.rect[0] -= self.game_speed
