import os
import pygame

__ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_background(screen_size):
    asset_background = pygame.image.load(os.path.join(__ROOT_DIR, '..', '..', 'assets', 'background-day.png'))
    return pygame.transform.scale(asset_background, screen_size)


def load_bluebird_downflap():
    return pygame.image.load(os.path.join(__ROOT_DIR, '..', '..', 'assets', 'bluebird-downflap.png')).convert_alpha()


def load_bluebird_midflap():
    return pygame.image.load(os.path.join(__ROOT_DIR, '..', '..', 'assets', 'bluebird-midflap.png')).convert_alpha()


def load_bluebird_upflap():
    return pygame.image.load(os.path.join(__ROOT_DIR, '..', '..', 'assets', 'bluebird-upflap.png')).convert_alpha()


def load_base_ground(screen_size):
    asset_base_ground = pygame.image.load(os.path.join(__ROOT_DIR, '..', '..', 'assets', 'base.png')).convert_alpha()
    return pygame.transform.scale(asset_base_ground, screen_size)


def load_pipe(screen_size):
    asset_pipe = pygame.image.load(os.path.join(__ROOT_DIR, '..', '..', 'assets', 'pipe-red.png')).convert_alpha()
    return pygame.transform.scale(asset_pipe, screen_size)
