import pygame

from src.controller.AssetController import load_pipe


class Pipe(pygame.sprite.Sprite):
    GAME_SPEED = 10

    def __init__(self, screen_size, pipe_size, pipe_pos, inverted):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_pipe(pipe_size)

        self.rect = self.image.get_rect()
        self.rect[0] = pipe_pos[0]

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - pipe_pos[1])
        else:
            self.rect[1] = screen_size[1] - pipe_pos[1]

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= self.GAME_SPEED

