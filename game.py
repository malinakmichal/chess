from figure import Figure
from bishop import Bishop
from king import King
from knight import Knight
from queen import Queen
from rook import Rook
from pawn import Pawn
import pygame
from graphics import Window
import random
from minimaxAI import minimax
from moves import *
from directions import in_bounds
import math
from position import Coordinates


letters = ["A", "B", "C", "D", "E", "F", "G", "H"]


def no_moves(board, moves, color):
    opponent_color = "white"
    if color == "white":
        opponent_color = "black"

    if not moves:
        if is_check(board, color):
            # no moves to be played and under a check -> loss
            print("winner is", opponent_color)
        else:
            # no moves to be played and not under a check -> draw
            print("draw by stalemate")
        return True
    return False


def get_square(mouse):
    """Returns chess position from coordinates"""
    x_coord = mouse[0] // 63
    y_coord = mouse[1] // 63
    return y_coord, x_coord


class Game:
    """Class game"""
    def __init__(self):
        self.board = [[Figure() for _ in range(8)] for _ in range(8)]
        self.init_game()
        self.window = Window(500, 500)
        pygame.init()

    def init_game(self):
        """Game initialization"""

        # initializes all figures except pawns
        figures = [Rook("A1", "black"), Rook("H1", "black"), Rook("A8", "white"), Rook("H8", "white"),
                   Bishop("C8", "white"), Bishop("F8", "white"), Bishop("F1", "black"), Bishop("C1", "black"),
                   Knight("B1", "black"), Knight("G1", "black"), Knight("G8", "white"), Knight("B8", "white"),
                   Queen("D8", "white"), Queen("D1", "black"), King("E8", "white"), King("E1", "black")]

        # initializes pawns
        for letter in letters:
            position = letter + "2"
            figures.append(Pawn(position, "black"))
            position = letter + "7"
            figures.append(Pawn(position, "white"))

        # sets positions of the figures
        for x in range(8):
            for y in range(8):
                for figure in figures:
                    if figure.position.x == x and figure.position.y == y:
                        self.board[x][y] = figure

    def start(self):
        turn = 0
        moves = []
        show_move = [Coordinates(-1, -1), (Coordinates(-1, -1), False)]
        self.window.draw(self.board, moves, show_move)
        selected = False
        end = False
        figure = Figure()
        while True:
            pygame.time.Clock().tick(30)

            # if there is a check prevent the player from making moves and just show the final board until the QUIT
            # button is pressed
            if end:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                continue

            # black plays (AI)
            if turn % 2 == 1:
                # checks to see if there are moves for white to be played, end of the game
                figures_to_move = get_all_moves(self.board, "black")
                end = no_moves(self.board, figures_to_move, "black")
                if end:
                    continue

                # get best move using the minimax algorithm and alpha-beta pruning
                depth = 3
                score, (figure, move) = minimax(self.board, "black", depth, -math.inf, math.inf, True)

                # if the move is invalid, play random move with random figure
                if move[0].x == -1 or move[0].y == -1 or figure.get_type() == "figure":
                    # selects random figure
                    figure = random.choice(figures_to_move)
                    moves = figure.get_moves(self.board)
                    moves = filter_moves(moves, self.board, figure)
                    if not moves:
                        print("winner is white")
                        end = True
                        continue
                    # selects random move
                    move = random.choice(moves)

                show_move = [figure.position, move]

                # plays the move and checks if it is the end of teh game
                end = figure.move(move, self.board, False)[0]
                if end:
                    print("winner is black")
                    end = True
                    continue

                turn += 1
                moves = []

            # white plays (human player)
            else:
                # checks to see if there are moves for white to be played, end of the game
                figures_to_move = get_all_moves(self.board, "white")
                end = no_moves(self.board, figures_to_move, "white")
                if end:
                    continue

                # wait for input from the player
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        square_x, square_y = get_square(pygame.mouse.get_pos())

                        # checks if the clicked mouse position is in bounds of the chess board
                        if not in_bounds(square_x) or not in_bounds(square_y):
                            continue

                        # the board is showing moves for the selected figure
                        if selected:
                            # if clicked the selected figure, unselect it
                            if figure.position.x == square_x and figure.position.y == square_y:
                                selected = False
                                moves = []
                                continue

                            # checks if the selected tile is an eligible move that is shown on the board
                            for move in moves:
                                if move[0].x == square_x and move[0].y == square_y:
                                    if figure.get_type() != "figure":
                                        end = figure.move(move, self.board, False)[0]

                                    if end:
                                        print("winner is white")
                                        moves = []
                                        break

                                    turn += 1
                                    moves = []
                                    selected = False

                        # the board is not showing moves
                        else:
                            fig = self.board[square_x][square_y]

                            # if the clicked tile is a figure show valid moves
                            if fig.get_type() != "figure" and fig.get_color() == "white":
                                moves = self.board[square_x][square_y].get_moves(self.board)
                                figure = self.board[square_x][square_y]

                                # filters the moves that would lead to an immediate checkmate
                                moves = filter_moves(moves, self.board, figure)
                                selected = True

                                # if no moves, unselect the figure
                                if not moves:
                                    selected = False

            # draws the board
            self.window.draw(self.board, moves, show_move)
