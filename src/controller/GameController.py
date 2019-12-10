import pygame

from pygame.locals import *

from src.controller.AssetController import load_background
from src.model.Bird import Bird


class GameController:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 800

    birds_group = None

    BACKGROUND = None

    clock = None
    screen = None

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.get_screen_size())

        self.BACKGROUND = load_background(self.get_screen_size())
        self.birds_group = pygame.sprite.Group()

        bird = Bird(self.get_screen_size())
        self.birds_group.add(bird)

    def start(self):

        while True:

            self.clock.tick(20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        for bird in self.birds_group:
                            bird.bump()

            self.screen.blit(self.BACKGROUND, (0, 0))

            self.birds_group.update()
            self.birds_group.draw(self.screen)

            pygame.display.update()

    def get_screen_size(self):
        return self.SCREEN_WIDTH, self.SCREEN_HEIGHT
