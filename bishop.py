from figure import Figure
import pygame
from directions import get_directions_line


class Bishop(Figure):
    """Chess figure rook"""

    def __init__(self, position, color):
        Figure.__init__(self, position, color)
        self.color = color
        self.type = "bishop"
        if self.color == "white":
            self.image = pygame.image.load('figures/bishop_white.png')
        else:
            self.image = pygame.image.load('figures/bishop_black.png')

    def get_image(self):
        return self.image

    def get_type(self):
        return self.type

    def get_moves(self, board):
        directions = [(1, -1), (-1, 1), (-1, -1), (1, 1)]

        moves = get_directions_line(directions, self.position, self.get_color(), board)

        return moves
