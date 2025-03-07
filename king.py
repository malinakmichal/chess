from figure import Figure
import pygame
from directions import get_directions_other
from position import Coordinates
from moves import is_check


class King(Figure):
    """Chess figure rook"""

    def __init__(self, position, color):
        Figure.__init__(self, position, color)
        self.color = color
        self.type = "king"
        self.castling = True
        if self.color == "white":
            self.image = pygame.image.load('figures/king_white.png')
        else:
            self.image = pygame.image.load('figures/king_black.png')

    def get_image(self):
        return self.image

    def get_type(self):
        return self.type

    def get_moves(self, board):
        directions = [(1, 1), (-1, -1), (-1, 1), (1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]

        moves = get_directions_other(directions, self.position, self.get_color(), board)

        # castling
        if not self.moved:
            if self.color == "white":
                if board[7][0].get_type() == "rook" and not board[7][0].moved and board[7][1].get_type() == "figure" and board[7][2].get_type() == "figure" and board[7][3].get_type() == "figure":
                    moves.append((Coordinates(7, 0), False))

                if board[7][7].get_type() == "rook" and not board[7][7].moved and board[7][6].get_type() == "figure" and board[7][5].get_type() == "figure":
                    moves.append((Coordinates(7, 7), False))

            if self.color == "black":
                if board[0][0].get_type() == "rook" and not board[0][0].moved and board[0][1].get_type() == "figure" and board[0][2].get_type() == "figure" and board[0][3].get_type() == "figure":
                    moves.append((Coordinates(0, 0), False))

                if board[0][7].get_type() == "rook" and not board[0][7].moved and board[0][6].get_type() == "figure" and board[0][5].get_type() == "figure":
                    moves.append((Coordinates(0, 7), False))

        return moves
