from Constants import *


class Tile:
    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color
        self.next = None

    def draw(self, screen):
        ts = TILESIZE
        pygame.draw.rect(screen, self.color, (self.j * ts, self.i * ts, ts, ts))
        pygame.draw.rect(screen, BLACK, (self.j * ts, self.i * ts, ts, ts), 1)
        # drawText(screen, f'{self.i},{self.j}', 14, BLACK, self.j * ts + ts//2, self.i * ts + ts//2)
