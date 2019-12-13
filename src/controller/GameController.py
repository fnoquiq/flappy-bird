import pygame
import random
import time

from pygame.locals import *

from src.controller.AssetController import load_background
from src.model.Pipe import Pipe
from src.model.Ground import Ground
from src.model.Bird import Bird


class GameController:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 800

    GROUND_WIDTH = 2 * SCREEN_WIDTH
    GROUND_HEIGTH = 100

    PIPE_WIDTH = 80
    PIPE_HEIGTH = 500
    PIPE_GAP = 200

    birds_group = None
    grounds_group = None
    pipes_group = None

    BACKGROUND = None

    clock = None
    screen = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.get_screen_size())

        self.BACKGROUND = load_background(self.get_screen_size())

        self.__init_birds()
        self.__init_grounds()
        self.__init_pipes()

    def __init_grounds(self):
        self.grounds_group = pygame.sprite.Group()
        for i in range(2):
            ground = Ground(self.get_screen_size(), (self.GROUND_WIDTH, self.GROUND_HEIGTH), self.GROUND_WIDTH * i)
            self.grounds_group.add(ground)

        self.pipes_group = pygame.sprite.Group()

    def __init_birds(self):
        self.birds_group = pygame.sprite.Group()
        bird = Bird(self.get_screen_size())
        self.birds_group.add(bird)

    def __init_pipes(self):
        for i in range(2):
            pipes = self.__get_random_pipes(self.SCREEN_WIDTH * i + 800)
            self.pipes_group.add(pipes[0])
            self.pipes_group.add(pipes[1])

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

            self.__check_off_screen_sprites()
            self.__update_sprites()
            pygame.display.update()
            self.__check_collides()

    def __check_off_screen_sprites(self):
        if self.__is_off_screen(self.grounds_group.sprites()[0]):
            self.grounds_group.remove(self.grounds_group.sprites()[0])

            new_ground = Ground(self.get_screen_size(), (self.GROUND_WIDTH, self.GROUND_HEIGTH),
                                self.GROUND_WIDTH - 20)
            self.grounds_group.add(new_ground)

        if self.__is_off_screen(self.pipes_group.sprites()[0]):
            self.pipes_group.remove(self.pipes_group.sprites()[0])
            self.pipes_group.remove(self.pipes_group.sprites()[0])

            pipes = self.__get_random_pipes(self.SCREEN_WIDTH * 2)

            self.pipes_group.add(pipes[0])
            self.pipes_group.add(pipes[1])

    def __update_sprites(self):
        self.birds_group.update()
        self.pipes_group.update()
        self.grounds_group.update()

        self.birds_group.draw(self.screen)
        self.pipes_group.draw(self.screen)
        self.grounds_group.draw(self.screen)

    def __check_collides(self):
        if pygame.sprite.groupcollide(
                self.birds_group,
                self.grounds_group,
                False,
                False,
                pygame.sprite.collide_mask
        ) or \
                pygame.sprite.groupcollide(
                    self.birds_group,
                    self.pipes_group,
                    False,
                    False,
                    pygame.sprite.collide_mask
                ):
            self.game_over()

    def __is_off_screen(self, sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    def get_screen_size(self):
        return self.SCREEN_WIDTH, self.SCREEN_HEIGHT

    def game_over(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), [50, 50, 300, 40])
        self.screen.blit(text, [132, 55])
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        exit()

    def __get_random_pipes(self, xpos):
        size = random.randint(100, 300)
        pipe = Pipe(self.get_screen_size(), (self.PIPE_WIDTH, self.PIPE_HEIGTH), (xpos, size), False, )
        pipe_inverted = Pipe(self.get_screen_size(), (self.PIPE_WIDTH, self.PIPE_HEIGTH),
                             (xpos, self.SCREEN_HEIGHT - size - self.PIPE_GAP), True)
        return pipe, pipe_inverted
