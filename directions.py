from position import Coordinates


# checks if the position is on the chess board
def in_bounds(position) -> bool:
    if 0 <= position <= 7:
        return True
    return False


def get_directions_line(directions, position, color, board):
    moves = []
    for direction in directions:
        position_x = position.x + direction[0]
        position_y = position.y + direction[1]
        while in_bounds(position_x) and in_bounds(position_y):
            if board[position_x][position_y].get_type() != "figure":
                if board[position_x][position_y].get_color() == color:
                    break
                else:
                    if board[position_x][position_y].get_type() == "king":
                        moves.append((Coordinates(position_x, position_y), True))
                    else:
                        moves.append((Coordinates(position_x, position_y), False))
                    break
            else:
                moves.append((Coordinates(position_x, position_y), False))
                position_x += direction[0]
                position_y += direction[1]
    return moves


def get_directions_other(directions, position, color, board):
    moves = []
    for direction in directions:
        position_x = position.x + direction[0]
        position_y = position.y + direction[1]
        if in_bounds(position_x) and in_bounds(position_y):
            if board[position_x][position_y].get_type() != "figure":
                if board[position_x][position_y].get_color() != color:
                    if board[position_x][position_y].get_type() == "king":
                        moves.append((Coordinates(position_x, position_y), True))
                    else:
                        moves.append((Coordinates(position_x, position_y), False))
            else:
                moves.append((Coordinates(position_x, position_y), False))
    return moves
