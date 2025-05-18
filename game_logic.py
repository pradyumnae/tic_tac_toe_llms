class TicTacToe:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.is_game_over():
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = self.board + list(map(list, zip(*self.board))) + [
            [self.board[i][i] for i in range(3)],
            [self.board[i][2-i] for i in range(3)]
        ]
        return any(all(cell == self.current_player for cell in line) for line in lines)

    def is_game_over(self):
        return self.winner is not None or all(cell != "" for row in self.board for cell in row)