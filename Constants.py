import pygame
from typing import List

pygame.font.init()

TILESIZE = 40
ROWS = COLS = 15
HEIGHT = TILESIZE * ROWS
WIDTH = TILESIZE * (COLS + 6)
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGTH_RED = (255, 128, 128)
LIGTH_BLUE = (128, 128, 255)
LIGTH_YELLOW = (255, 255, 158)
LIGTH_GREEN = (128, 255, 128)
LIGHT_GRAY = (192, 192, 192)
CREAM = (255, 255, 204)

BOARD_MAP = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2],
             [1, 5, 5, 5, 5, 1, 0, 2, 2, 2, 5, 5, 5, 5, 2],
             [1, 5, 5, 5, 5, 1, 0, 2, 0, 2, 5, 5, 5, 5, 2],
             [1, 5, 5, 5, 5, 1, 0, 2, 0, 2, 5, 5, 5, 5, 2],
             [1, 5, 5, 5, 5, 1, 0, 2, 0, 2, 5, 5, 5, 5, 2],
             [1, 1, 1, 1, 1, 1, 0, 2, 0, 2, 2, 2, 2, 2, 2],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 3, 3, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
             [4, 4, 4, 4, 4, 4, 0, 4, 0, 3, 3, 3, 3, 3, 3],
             [4, 5, 5, 5, 5, 4, 0, 4, 0, 3, 5, 5, 5, 5, 3],
             [4, 5, 5, 5, 5, 4, 0, 4, 0, 3, 5, 5, 5, 5, 3],
             [4, 5, 5, 5, 5, 4, 0, 4, 0, 3, 5, 5, 5, 5, 3],
             [4, 5, 5, 5, 5, 4, 4, 4, 0, 3, 5, 5, 5, 5, 3],
             [4, 4, 4, 4, 4, 4, 0, 0, 0, 3, 3, 3, 3, 3, 3]]

def drawText(screen, text, size, color, x, y):
    font = pygame.font.SysFont("Arial", size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
