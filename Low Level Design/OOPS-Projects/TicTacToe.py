class Board:
    def __init__(self):
        self.board = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
        ]

    def print_board(self):
        for i in range(3):
            print(self.board[i])

    def check_winner(self):
        # check rows
        if (self.board[0][0] == self.board[0][1]) and (
            self.board[0][1] == self.board[0][2]
        ):
            return True
        elif (self.board[1][0] == self.board[1][1]) and (
            self.board[1][1] == self.board[1][2]
        ):
            return True
        elif (self.board[2][0] == self.board[2][1]) and (
            self.board[2][1] == self.board[2][2]
        ):
            return True
        # check columns
        elif (self.board[0][0] == self.board[1][0]) and (
            self.board[1][0] == self.board[2][0]
        ):
            return True
        elif (self.board[0][1] == self.board[1][1]) and (
            self.board[1][1] == self.board[2][1]
        ):
            return True
        elif (self.board[0][2] == self.board[1][2]) and (
            self.board[1][2] == self.board[2][2]
        ):
            return True
        # check diagonal
        elif (self.board[0][0] == self.board[1][1]) and (
            self.board[1][1] == self.board[2][2]
        ):
            return True
        # check reverse diagonal
        elif (self.board[0][2] == self.board[1][1]) and (
            self.board[1][1] == self.board[2][0]
        ):
            return True
        else:
            return False

    def take_input(self, player, row, col):
        self.board[row][col] = player
        win = self.check_winner()
        if win:
            return True
        return False


def play():
    [player, row, col] = input("player, row and col(space separated): ").split(" ")
    win = board1.take_input(player, int(row), int(col))
    if win:
        return True


if __name__ == "__main__":
    board1 = Board()
    board1.print_board()
    while True:
        win = play()
        if win:
            board1.print_board()
            break
