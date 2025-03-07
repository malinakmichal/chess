
def is_check(board, color):
    # checks if there is a check on the board checking the king of certain color
    for x in range(8):
        for y in range(8):
            if board[x][y].get_type() != "figure" and board[x][y].get_color() != color:
                moves = board[x][y].get_moves(board)
                for mov in moves:
                    if mov[1]:
                        return True
    return False


def filter_moves(moves, board, figure):
    # filters the moves that would lead to an immediate checkmate
    el_moves = []
    color = figure.get_color()

    for move in moves:
        # if there is a check, castling is no eligible
        if figure.get_type() == "king" and not figure.moved and move[0].y == 7 or move[0].y == 0:
            if is_check(board, color):
                continue

        # moves the figure to a tile and if it does not reveal check it is added as a move
        result = figure.move(move, board, True)
        if not is_check(board, color):
            el_moves.append(move)

        # returns the board to a previous state
        figure.unmake_move(board, result)
    return el_moves


def get_all_moves(board, color):
    all_moves = []
    # get figures of certain color that can be moved
    for x in range(8):
        for y in range(8):
            if board[x][y].get_type() != "figure" and board[x][y].get_color() == color:
                # figure has eligible moves that can be played
                moves = board[x][y].get_moves(board)
                figure = board[x][y]
                moves = filter_moves(moves, board, figure)

                if moves:
                    all_moves.append(board[x][y])

    return all_moves
