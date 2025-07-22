import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_winner = None  # Track the winner

    def print_board(self):
        # Display the current board
        print('\n')
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Show which numbers correspond to which spots
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_idx = square // 3
        row = self.board[row_idx * 3: (row_idx + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_idx = square % 3
        column = [self.board[col_idx + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Top-left to bottom-right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Top-right to bottom-left
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter

    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')  # Empty line

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'  # Switch player

    if print_game:
        print('It\'s a tie!')
    return None


class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            try:
                square = int(input(f'{self.letter}\'s turn. Input move (0-8): '))
                if square not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return square


class ComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # Random first move
        else:
            # Basic AI: first check for winning moves, then blocking moves
            # If neither is available, choose randomly
            if self.letter == 'O':
                opponent_letter = 'X'
            else:
                opponent_letter = 'O'

            # Check for winning move
            for possible_move in game.available_moves():
                # Make copy of board and check if this move wins
                board_copy = game.board.copy()
                board_copy[possible_move] = self.letter
                temp_game = TicTacToe()
                temp_game.board = board_copy
                if temp_game.winner(possible_move, self.letter):
                    return possible_move

            # Check for blocking move
            for possible_move in game.available_moves():
                board_copy = game.board.copy()
                board_copy[possible_move] = opponent_letter
                temp_game = TicTacToe()
                temp_game.board = board_copy
                if temp_game.winner(possible_move, opponent_letter):
                    return possible_move

            # Pick random corner
            corners = [0, 2, 6, 8]
            available_corners = [c for c in corners if c in game.available_moves()]
            if available_corners:
                square = random.choice(available_corners)
                return square

            # Pick center if available
            if 4 in game.available_moves():
                return 4

            # Default to random move
            square = random.choice(game.available_moves())

        return square


if __name__ == '__main__':
    print('Welcome to Tic Tac Toe against the computer!')
    print('Positions are numbered as follows:')

    while True:
        game = TicTacToe()
        human = HumanPlayer('X')
        computer = ComputerPlayer('O')
        play(game, human, computer)

        # Ask for rematch
        rematch = input('Play again? (y/n): ').lower()
        if rematch != 'y':
            break

