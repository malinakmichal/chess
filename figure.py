from position import Coordinates
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]


def convert(position):
    if len(position) == 0:
        return -1, -1
    index = -1
    for i, letter in enumerate(letters):
        if position[0] == letter:
            index = i

    return Coordinates(int(position[1]) - 1, index)


class Figure:
    """Abstract class for figures"""
    def __init__(self, position=Coordinates(-1, -1), color=""):
        self.color = color
        if isinstance(position, str):
            self.position = convert(position)
        else:
            self.position = position
        self.type = "figure"
        self.moved = False
        self.castling = False

    def get_color(self):
        """Gets the figure color"""
        return self.color

    def get_type(self):
        return self.type

    def get_moves(self, board):
        print("not")
        return []

    def move(self, move, board, premove):
        from queen import Queen

        last_move = move
        last_position = self.position

        deleted_figure = Figure()
        moved_figure = Figure()

        # if the move is to take a king than it is an end of the game
        if board[move[0].x][move[0].y].get_type() == "king" and not premove:
            return True, last_position, last_move, deleted_figure, moved_figure

        # figure is moved
        if self.get_type() == "king" and not self.moved and not board[move[0].x][move[0].y].moved and board[move[0].x][move[0].y].get_color() == self.color and board[move[0].x][move[0].y].get_type() == "rook":
            # castling
            figure = board[move[0].x][move[0].y]
            position_king = self.position

            if move[0].y == 7:
                board[move[0].x][move[0].y - 1] = board[self.position.x][self.position.y]
                board[move[0].x][move[0].y - 2] = board[move[0].x][move[0].y]
                board[move[0].x][move[0].y - 2].position = Coordinates(move[0].x, move[0].y - 2)
                position_king = Coordinates(move[0].x, move[0].y - 1)
                self.castling = True
            elif move[0].y == 0:
                board[move[0].x][move[0].y + 2] = board[self.position.x][self.position.y]
                board[move[0].x][move[0].y + 3] = board[move[0].x][move[0].y]
                board[move[0].x][move[0].y + 3].position = Coordinates(move[0].x, move[0].y + 3)
                position_king = Coordinates(move[0].x, move[0].y + 2)
                self.castling = True

            # the origin place from which the figure was moved is replaced by empty figure
            board[move[0].x][move[0].y] = Figure()
            board[self.position.x][self.position.y] = Figure()
            if not premove:
                figure.moved = True
                self.moved = True

            self.position = position_king

        else:
            # normal move
            deleted_figure = board[move[0].x][move[0].y]
            moved_figure = board[self.position.x][self.position.y]
            board[move[0].x][move[0].y] = board[self.position.x][self.position.y]

            # if the figure to be moved is pawn and the position is last rank then the pawn is replaced by a queen
            if self.get_type() == "pawn" and self.get_color() == "black" and move[0].x == 7:
                board[move[0].x][move[0].y] = Queen(move[0], "black")

            elif self.get_type() == "pawn" and self.get_color() == "white" and move[0].x == 0:
                board[move[0].x][move[0].y] = Queen(move[0], "white")

            # the origin place from which the figure was moved is replaced by empty figure
            board[self.position.x][self.position.y] = Figure()

            if not premove:
                self.moved = True

            self.position = move[0]
            self.castling = False
        return False, last_position, last_move, deleted_figure, moved_figure

    def unmake_move(self, board, result):
        end, last_position, last_move, deleted_figure, moved_figure = result
        if last_move[0].x == -1 or last_move[0].y == -1 or last_position.x == -1 or last_position.y == -1:
            self.castling = False
            return

        if self.castling:

            if last_move[0].y == 7:
                board[last_move[0].x][last_move[0].y] = board[last_move[0].x][5]
                board[last_move[0].x][4] = board[last_move[0].x][6]
                board[last_move[0].x][6] = Figure()
                board[last_move[0].x][5] = Figure()
                board[last_move[0].x][4].position = Coordinates(last_move[0].x, 4)
                board[last_move[0].x][last_move[0].y].position = last_move[0]

            elif last_move[0].y == 0:
                board[last_move[0].x][last_move[0].y] = board[last_move[0].x][3]
                board[last_move[0].x][4] = board[last_move[0].x][2]
                board[last_move[0].x][2] = Figure()
                board[last_move[0].x][3] = Figure()
                board[last_move[0].x][4].position = Coordinates(last_move[0].x, 4)
                board[last_move[0].x][last_move[0].y].position = last_move[0]

        else:
            board[last_position.x][last_position.y] = moved_figure
            board[last_position.x][last_position.y].position = last_position
            board[last_move[0].x][last_move[0].y] = deleted_figure
            board[last_move[0].x][last_move[0].y].position = last_move[0]

        self.castling = False

        return
