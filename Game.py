from random import randint
from Constants import *
from Tile import *
from Token import *


players = {
    0 : (RED, 1, 2),
    1 : (BLUE, 19, 2),
    2 : (GREEN, 19, 11),
    3 : (YELLOW, 1, 11)
}

class Game:
    def __init__(self):
        # pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = True

    def run(self):
        self.tiles: List[List[Tile]] = self.create_board()
        self.tokens: List[Token] = self.create_tokens()
        self.turn = 0
        self.roll = 0
        self.validTokens = []
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def create_board(self):
        tiles = []
        for row in range(ROWS):
            tiles.append([])
            for col in range(COLS):
                if ((row < 6 and col < 6)or (row == 7 and 0 < col < 6)or ((row, col) == (6, 1))):
                    color = LIGTH_RED
                elif ( (row < 6 and col > 8) or (0 < row < 6 and col == 7) or ((row, col) == (1, 8))):
                    color = LIGTH_BLUE
                elif ((row > 8 and col < 6) or (8 < row < 14 and col == 7) or ((row, col) == (13, 6))):
                    color = LIGTH_YELLOW
                elif ((row > 8 and col > 8) or (row == 7 and 8 < col < 14) or ((row, col) == (8, 13))):
                    color = LIGTH_GREEN
                elif (5 < row < 9 and 5 < col < 9 or ((row, col) in ((2, 6), (6, 12), (8, 2), (12, 8)))):
                    color = GREY
                else:
                    color = WHITE
                tiles[row].append(Tile(row, col+3, color))
        return tiles
    
    def create_tokens(self):
        token_positions = [
            [(RED, (2, 5)), (RED, (2, 6)), (RED, (3, 5)), (RED, (3, 6))],
            [(BLUE, (2, 14)), (BLUE, (2, 15)), (BLUE, (3, 14)), (BLUE, (3, 15))],
            [(YELLOW, (11, 5)), (YELLOW, (11, 6)), (YELLOW, (12, 5)), (YELLOW, (12, 6))],
            [(GREEN, (11, 14)), (GREEN, (11, 15)), (GREEN, (12, 14)), (GREEN, (12, 15))]
        ]
        return [Token(self, color, pos) for positions in token_positions for color, pos in positions]

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_r:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.diceRect.collidepoint(event.pos) and self.roll == 0:
                    self.roll = randint(1, 6)
            for token in self.validTokens:
                token.moved = False
                token.handle_event(event)
                if token.moved: break
    
    def update(self):
        self.diceRect = pygame.Rect(TILESIZE*players[self.turn][1], TILESIZE*players[self.turn][2], TILESIZE, TILESIZE)
        self.validTokens = [token for token in self.tokens if token.color == players[self.turn][0]]
        if self.roll != 6:
            self.validTokens = [token for token in self.validTokens if not token.closed]
        if len(self.validTokens) == 0 and self.roll != 0:
            self.turn = (self.turn + 1) % 4
            self.roll = 0
        if len(self.validTokens) == 1 and self.roll != 0:
            self.validTokens[0].move(self.roll)

    def draw(self):
        self.screen.fill(GREY)
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)
        pygame.draw.rect(self.screen, CREAM, (TILESIZE * 4+1, TILESIZE * 1+1, TILESIZE * 4-2, TILESIZE * 4-2))
        pygame.draw.rect(self.screen, CREAM, (TILESIZE * 13+1, TILESIZE * 1+1, TILESIZE * 4-2, TILESIZE * 4-2))
        pygame.draw.rect(self.screen, CREAM, (TILESIZE * 4+1, TILESIZE * 10+1, TILESIZE * 4-2, TILESIZE * 4-2))
        pygame.draw.rect(self.screen, CREAM, (TILESIZE * 13+1, TILESIZE * 10+1, TILESIZE * 4-2, TILESIZE * 4-2))
        pygame.draw.rect(self.screen, CREAM, self.diceRect)
        if self.roll: 
            drawText(self.screen, f'{self.roll}', int(TILESIZE*.9), BLACK, self.diceRect.centerx, self.diceRect.centery)
        for token in self.tokens:
            if token in self.validTokens:
                token.draw(self.screen, 0.9)
            else:
                token.draw(self.screen)
        pygame.display.update()
    
    def quit(self):
        self.playing = False
        self.running = False


if __name__ == "__main__":
    game = Game()
    while game.playing:
        game.run()
    pygame.quit()
