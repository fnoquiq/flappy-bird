import pygame

from pygame.locals import *

from src.controller.AssetController import load_background
from src.model.Bird import Bird
from src.model.Ground import Ground


class GameController:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 800

    birds_group = None
    grounds_group = None

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

        self.grounds_group = pygame.sprite.Group()
        ground1 = Ground(self.get_screen_size(), 2 * self.get_screen_size()[0] * 0)
        ground2 = Ground(self.get_screen_size(), 2 * self.get_screen_size()[0] * 1)
        self.grounds_group.add(ground1, ground2)

    def start(self):

        while True:

            self.clock.tick(20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_over()
                    break

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        for bird in self.birds_group:
                            bird.bump()

            self.screen.blit(self.BACKGROUND, (0, 0))

            if self.is_off_screen(self.grounds_group.sprites()[0]):
                self.grounds_group.remove(self.grounds_group.sprites()[0])

                new_ground = Ground(self.get_screen_size(), 2 * self.get_screen_size()[0])
                self.grounds_group.add(new_ground)

            self.birds_group.update()
            self.grounds_group.update()

            self.birds_group.draw(self.screen)
            self.grounds_group.draw(self.screen)

            pygame.display.update()

            if pygame.sprite.groupcollide(self.birds_group, self.grounds_group, False, False, pygame.sprite.collide_mask):
                self.game_over()
                break

    def is_off_screen(self, sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    def get_screen_size(self):
        return self.SCREEN_WIDTH, self.SCREEN_HEIGHT

    def game_over(self):
        pygame.quit()