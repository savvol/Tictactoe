class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.players = [Player("X"), Player("O")]
        self.current_player = self.players[0]

    def print_board(self):
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player.symbol
            self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
        else:
            print("Invalid move! The position is already taken. Try again.")

    def check_win(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True

        return False

    def is_full(self):
        return " " not in self.board

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while True:
            try:
                position = int(input(f"Player {self.current_player.symbol}, enter your move (1-9): ")) - 1
                if 0 <= position <= 8:
                    self.make_move(position)
                    self.print_board()

                    if self.check_win():
                        print(f"Player {self.current_player.symbol} wins! Congratulations!")
                        break
                    elif self.is_full():
                        print("It's a tie! The board is full.")
                        break
                else:
                    print("Invalid input! Enter a number between 1 and 9.")

            except ValueError:
                print("Invalid input! Enter a valid number.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
