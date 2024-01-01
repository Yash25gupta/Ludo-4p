from Constants import *
from Game import Game
import time

r = [(6,4), (6,5), (6,6), (6,7), (6,8), (5,9), (4,9), (3,9), (2,9), (1,9), (0,9), (0,10), (0,11), (1,11), (2,11),
     (3,11), (4,11), (5,11), (6,12), (6,13), (6,14), (6,15), (6,16), (6,17), (7,17), (8,17), (8,16), (8,15), (8,14),
     (8,13), (8,12), (9,11), (10,11), (11,11), (12,11), (13,11), (14,11), (14,10), (14,9), (13,9), (12,9), (11,9),
     (10,9), (9,9), (8,8), (8,7), (8,6), (8,5), (8,4), (8,3), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9)]
b = r[13:-6] + [(6,3)] + r[:12] + [(1,10), (2,10), (3,10), (4,10), (5,10), (6,10)]
g = b[13:-6] + [(0,11)] + b[:12] + [(7,16), (7,15), (7,14), (7,13), (7,12), (7,11)]
y = g[13:-6] + [(8,17)] + g[:12] + [(13,10), (12,10), (11,10), (10,10), (9,10), (8,10)]

path = {
    RED: r,
    BLUE: b,
    YELLOW: y,
    GREEN: g
}

class Token:
    imunePos = [(6,4), (8,5), (2,9), (1,11), (6,15), (8,16), (12,11), (13,9)]

    def __init__(self, game: Game, color, o_pos):
        self.game = game
        self.color = color
        self.path = [o_pos] + path[color]
        self.pos = self.path[0]
        self.moved = False
        self.highlight = False
        self.closed = True
        self.imune = False
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pos == (event.pos[1] // TILESIZE, event.pos[0] // TILESIZE):
                self.move(self.game.roll)
        if event.type == pygame.MOUSEMOTION:
            self.highlight = (self.pos == (event.pos[1] // TILESIZE, event.pos[0] // TILESIZE))

    def draw(self, screen, scale=0.7):
        circle_center = (self.pos[1] * TILESIZE + TILESIZE // 2, self.pos[0] * TILESIZE + TILESIZE // 2)
        pygame.draw.circle(screen, self.color, circle_center, TILESIZE // 2 * scale)
        if self.highlight:
            pygame.draw.circle(screen, BLACK, circle_center, TILESIZE // 2 * scale, 5)
        if self.imune:
            pygame.draw.circle(screen, BLACK, circle_center, TILESIZE // 2 * scale, 3)

    def animate_move(self, start_pos, end_pos, duration=0.1):
        start_time = time.time()
        while time.time() - start_time < duration:
            t = (time.time() - start_time) / duration
            self.pos = (start_pos[0] * (1 - t) + end_pos[0] * t, start_pos[1] * (1 - t) + end_pos[1] * t)
            self.game.draw()
            pygame.time.delay(10)

    def move(self, count):
        if count == 0 : return
        if self.closed and count == 6:
            self.closed = False
            self.pos = self.path[1]
        else:
            for _ in range(count):
                start_pos = self.path[self.path.index(self.pos)]
                end_pos = self.path[self.path.index(self.pos) + 1]
                self.animate_move(start_pos, end_pos)
                self.pos = end_pos
            # self.pos = self.path[self.path.index(self.pos) + count]
            if not self.killed_a_token():
                self.game.turn = (self.game.turn + (count != 6)) % 4
            self.moved = True
        self.highlight = False
        self.imune = self.pos in Token.imunePos
        self.game.roll = 0

    def killed_a_token(self):
        for token in self.game.tokens:
            if token.color != self.color and token.pos == self.pos and not token.imune:
                current_index = token.path.index(token.pos)
                for i in range(current_index, 0, -1):
                    start_pos = token.path[i]
                    end_pos = token.path[i - 1]
                    token.animate_move(start_pos, end_pos, 0.03)
                    token.pos = end_pos
                token.closed = True
                return True
        return False
