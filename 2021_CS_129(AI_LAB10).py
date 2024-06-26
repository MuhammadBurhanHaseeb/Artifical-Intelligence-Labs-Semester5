class ConnectFour:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-' * (self.cols * 2 - 1))

def is_valid_move(board, col):
    return board[0][col] == ' '

def make_move(board, col, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            break

def evaluate_state(board, player):
    # Simple heuristic: count the number of connected pieces for the given player
    score = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                # Check horizontally
                if col + 3 < len(board[0]) and all(board[row][col + i] == player for i in range(4)):
                    score += 1
                # Check vertically
                if row + 3 < len(board) and all(board[row + i][col] == player for i in range(4)):
                    score += 1
                # Check diagonally (top-left to bottom-right)
                if row + 3 < len(board) and col + 3 < len(board[0]) and all(
                    board[row + i][col + i] == player for i in range(4)
                ):
                    score += 1
                # Check diagonally (bottom-left to top-right)
                if row - 3 >= 0 and col + 3 < len(board[0]) and all(
                    board[row - i][col + i] == player for i in range(4)
                ):
                    score += 1
    return score

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def is_winner(board, player):
    return evaluate_state(board, player) > 0

def get_empty_columns(board):
    return [col for col in range(len(board[0])) if board[0][col] == ' ']

def minimax(board, depth, maximizing_player):
    if depth == 0 or is_winner(board, 'X') or is_winner(board, 'O') or is_full(board):
        return evaluate_state(board, 'O') - evaluate_state(board, 'X')

    if maximizing_player:
        max_eval = float('-inf')
        for col in get_empty_columns(board):
            new_board = [row.copy() for row in board]
            make_move(new_board, col, 'O')
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for col in get_empty_columns(board):
            new_board = [row.copy() for row in board]
            make_move(new_board, col, 'X')
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for col in get_empty_columns(board):
        new_board = [row.copy() for row in board]
        make_move(new_board, col, 'O')
        eval = minimax(new_board, 4, False)
        if eval > best_eval:
            best_eval = eval
            best_move = col
    return best_move

# Example usage
if __name__ == "__main__":
    game = ConnectFour(6, 7)

    while True:
        game.display_board()

        # Human move
        human_col = int(input("Enter your move (column): "))
        while not is_valid_move(game.board, human_col):
            print("Invalid move. Try again.")
            human_col = int(input("Enter your move (column): "))
        make_move(game.board, human_col, 'X')

        if is_winner(game.board, 'X'):
            game.display_board()
            print("Congratulations! You win!")
            break
        elif is_full(game.board):
            game.display_board()
            print("It's a draw!")
            break

        # AI move
        ai_col = get_best_move(game.board)
        make_move(game.board, ai_col, 'O')

        if is_winner(game.board, 'O'):
            game.display_board()
            print("AI wins! Better luck next time.")
            break
        elif is_full(game.board):
            game.display_board()
            print("It's a draw!")
            break
