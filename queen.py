from figure import Figure
import pygame
from directions import get_directions_line


class Queen(Figure):
    """Chess figure rook"""

    def __init__(self, position, color):
        Figure.__init__(self, position, color)
        self.color = color
        self.type = "queen"
        if self.color == "white":
            self.image = pygame.image.load('figures/queen_white.png')
        else:
            self.image = pygame.image.load('figures/queen_black.png')

    def get_image(self):
        return self.image

    def get_type(self):
        return self.type

    def get_moves(self, board):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]

        moves = get_directions_line(directions, self.position, self.get_color(), board)

        return moves
