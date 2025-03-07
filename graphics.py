import pygame
from directions import in_bounds


class Window:
    """Window class for displaying the app"""
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess")

        self.background = pygame.image.load('figures/background.png')

        self.font_clicked = pygame.font.Font(None, 60)
        self.font_not_clicked = pygame.font.Font(None, 50)

    def draw(self, board, moves, show_move):
        """Displays figures on to the board"""
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

        position, move = show_move

        if in_bounds(move[0].x) and in_bounds(move[0].y) and in_bounds(position.x) and in_bounds(position.y):
            pygame.draw.rect(self.screen, (255, 160, 122), ((move[0].y * 63, move[0].x * 63), (61, 61)), 0)
            pygame.draw.rect(self.screen, (255, 160, 122), ((position.y * 63, position.x * 63), (61, 61)), 0)

        for x in range(8):
            for y in range(8):
                if board[x][y].get_type() != "figure":
                    self.screen.blit(board[x][y].get_image(), [y*63, x*63])

        for move in moves:
            pygame.draw.circle(self.screen, (160, 160, 160), (move[0].y * 63 + 30, move[0].x * 63 + 30), 10)

        pygame.display.update()
