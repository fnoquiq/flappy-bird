import pygame

from pygame.locals import *


class MenuController:
    screen = None
    button_area = None

    def __init__(self, screen, BACKGROUND, gameController):
        self.gameController = gameController
        self.BACKGROUND = BACKGROUND
        self.screen = screen
        self.button_area = pygame.Rect(50, 300, 300, 40)
        self.menu()

    def draw_button_normal(self):
        font = pygame.font.Font('freesansbold.ttf', 36)
        text = font.render("Start Game", True, (255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), [50, 300, 300, 40])
        self.screen.blit(text, [107, 303])
        pygame.display.flip()

    def draw_button_over(self):
        font = pygame.font.Font('freesansbold.ttf', 36)
        text = font.render("Start Game", True, (255, 255, 255))
        pygame.draw.rect(self.screen, (255, 0, 0), [50, 300, 300, 40])
        self.screen.blit(text, [107, 303])
        pygame.display.flip()

    def menu(self):
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.exit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_area.collidepoint(event.pos):
                        self.start_game_click()

            if self.button_area.collidepoint(pygame.mouse.get_pos()):
                self.draw_button_over()
            else:
                self.draw_button_normal()

            self.screen.blit(self.BACKGROUND, (0, 0))
            pygame.display.update()

    def start_game_click(self):
        self.gameController.start()
