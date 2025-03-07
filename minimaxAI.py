from position import Coordinates
from figure import Figure
from moves import filter_moves
import math


# todo pawn in higher ranks is better, checkmate - score 999
def get_score(board, color) -> int:
    value = {"king": 100,
             "queen": 8,
             "rook": 5,
             "bishop": 3,
             "knight": 3,
             "pawn": 1
             }

    score_white = 0
    score_black = 0

    for x in range(8):
        for y in range(8):
            figure = board[x][y].get_type()
            figure_color = board[x][y].get_color()

            add = 0
            if figure == "pawn":
                position = board[x][y].position
                if figure_color == "white":
                    add = 6 - position.x
                else:
                    add = position.x - 1

            if figure == "knight":
                position = board[x][y].position
                if 2 <= position.x <= 5 and 2 <= position.y <= 5:
                    add = 0.5

            if figure == "queen":
                position = board[x][y].position
                if 2 <= position.x <= 5 and 2 <= position.y <= 5:
                    add = 0.5

            if figure in value:
                if figure_color == "white":
                    score_white += value[figure]
                    score_white += add*0.2
                elif figure_color == "black":
                    score_black += value[figure]
                    score_black += add*0.2

    if color == "white":
        score = score_white - score_black
    else:
        score = score_black - score_white

    return round(score, 2)


def minimax(board, color, depth, alpha, beta, maximize):
    # with fewer figures depth should be higher todo
    best_fig = Figure()
    best_move = (Coordinates(-1, -1), False)

    # if reached the selected depth, blacks score will be returned
    if depth == 0:
        return get_score(board, "black"), (best_fig, best_move)

    if color == "white":
        opponent_color = "black"
    else:
        opponent_color = "white"

    if maximize:
        best_score = -math.inf
    else:
        best_score = math.inf

    for x in range(8):
        for y in range(8):
            if board[x][y].get_type() != "figure" and board[x][y].get_color() == color:
                # figure has eligible moves that can be played
                moves = board[x][y].get_moves(board)
                figure = board[x][y]
                moves = filter_moves(moves, board, figure)

                for move in moves:
                    result = figure.move(move, board, True)
                    score = minimax(board, opponent_color, depth - 1, alpha, beta, not maximize)[0]
                    figure.unmake_move(board, result)

                    if maximize:
                        if score > best_score:
                            best_score = score
                            best_move = move
                            best_fig = figure

                        if alpha <= score:
                            alpha = score

                        if alpha >= beta:
                            return best_score, (best_fig, best_move)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = move
                            best_fig = figure

                        if beta >= score:
                            beta = score
                        if alpha >= beta:
                            return best_score, (best_fig, best_move)

    return best_score, (best_fig, best_move)
