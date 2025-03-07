from figure import Figure
from position import Coordinates
from directions import in_bounds
import pygame


class Pawn(Figure):
    """Chess figure rook"""

    def __init__(self, start_position, color):
        Figure.__init__(self, start_position, color)
        self.color = color
        self.type = "pawn"
        if self.color == "white":
            self.image = pygame.image.load('figures/pawn_white.png')
        else:
            self.image = pygame.image.load('figures/pawn_black.png')

    def get_image(self):
        return self.image

    def get_type(self):
        return self.type

    def get_moves(self, board):
        moves = []
        direction = 1
        if self.color == "white":
            direction = -1

        # moves up for white player nad down for black player
        if direction == -1:
            if self.position.x - 1 >= 0 and board[self.position.x + direction][self.position.y].get_type() == "figure":
                moves.append((Coordinates(self.position.x + direction, self.position.y), False))
                if self.position.x - 1 >= 1 and board[self.position.x + 2 * direction][self.position.y].get_type() == "figure" and not self.moved:
                    moves.append((Coordinates(self.position.x + 2 * direction, self.position.y), False))
        else:
            if self.position.x + 1 < 8 and board[self.position.x + direction][self.position.y].get_type() == "figure":
                moves.append((Coordinates(self.position.x + direction, self.position.y), False))
                if self.position.x + 1 < 7 and board[self.position.x + 2*direction][self.position.y].get_type() == "figure" and not self.moved:
                    moves.append((Coordinates(self.position.x + 2*direction, self.position.y), False))

        # take moves (left and right), with check signal
        if in_bounds(self.position.y + 1) and in_bounds(self.position.x + direction) and board[self.position.x + direction][self.position.y + 1].get_type() != "figure" and board[self.position.x + direction][self.position.y + 1].get_color() != self.color:
            if board[self.position.x + direction][self.position.y + 1].get_type() == "king":
                moves.append((Coordinates(self.position.x + direction, self.position.y + 1), True))
            else:
                moves.append((Coordinates(self.position.x + direction, self.position.y + 1), False))
        if in_bounds(self.position.y - 1) and in_bounds(self.position.x + direction) and board[self.position.x + direction][self.position.y - 1].get_type() != "figure" and board[self.position.x + direction][self.position.y - 1].get_color() != self.color:
            if board[self.position.x + direction][self.position.y - 1].get_type() == "king":
                moves.append((Coordinates(self.position.x + direction, self.position.y - 1), True))
            else:
                moves.append((Coordinates(self.position.x + direction, self.position.y - 1), False))
        return moves
