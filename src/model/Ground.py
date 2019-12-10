import pygame

from src.controller.AssetController import load_base_ground


class Ground(pygame.sprite.Sprite):
    game_speed = 10

    def __init__(self, screen_size, ground_size, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = load_base_ground(ground_size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos - 20
        self.rect[1] = screen_size[1] - ground_size[1]

    def update(self):
        self.rect[0] -= self.game_speed
