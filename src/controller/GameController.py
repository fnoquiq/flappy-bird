import pygame
from pygame.locals import *


class GameController:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 800

    def init(self):
        pygame.init()
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            pygame.display.update()
