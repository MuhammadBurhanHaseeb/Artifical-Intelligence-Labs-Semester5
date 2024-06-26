import random

class TicTacToe:
    def _init_(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if not self.game_over and 1 <= position <= 9 and self.board[position - 1] == ' ':
            self.board[position - 1] = self.current_player
            self.switch_player()
            self.check_winner()
            if ' ' not in self.board or self.winner:
                self.game_over = True

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                self.winner = self.board[a]

    def get_game_state(self):
        return {
            "board": self.board,
            "current_player": self.current_player,
            "winner": self.winner,
            "game_over": self.game_over,
        }

class MCRLEnvironment:
    def _init_(self):
        self.game = TicTacToe()
        self.state_history = []

    def reset(self):
        self.game = TicTacToe()
        self.state_history = []

    def play_game(self, agent1, agent2):
        while not self.game.game_over:
            current_state = self.game.get_game_state()
            self.state_history.append(current_state)

            if self.game.current_player == 'X':
                move = agent1.choose_move(self.game)
            else:
                move = agent2.choose_move(self.game)

            self.game.make_move(move)

        self.update_agents()

    def update_agents(self):
        winner = self.game.winner

        for i, state in enumerate(self.state_history):
            state_copy = state.copy()
            if state_copy["winner"] == winner:
                state_copy["reward"] = 1
            elif state_copy["winner"] is None:
                state_copy["reward"] = 0
            else:
                state_copy["reward"] = -1

            if i == 0:
                agent1.learn_from_experience(state_copy)
            elif i % 2 == 0:
                agent1.learn_from_experience(state_copy)
            else:
                agent2.learn_from_experience(state_copy)

class MCRLEAgent:
    def _init_(self):
        self.value_function = {}  # State -> Value mapping
        self.epsilon = 0.1  # Exploration rate

    def choose_move(self, game):
        # Epsilon-greedy strategy: Choose the best move with probability (1-epsilon) or explore with probability epsilon
        if random.random() < self.epsilon:
            valid_moves = [i + 1 for i in range(9) if game.board[i] == ' ']
            return random.choice(valid_moves)
        else:
            return self.get_best_move(game)

    def get_best_move(self, game):
        # Choose the move with the highest expected value
        valid_moves = [i + 1 for i in range(9) if game.board[i] == ' ']
        best_move = None
        best_value = -float('inf')

        for move in valid_moves:
            game_copy = game.get_game_state().copy()
            game_copy['board'][move - 1] = game.current_player
            state = tuple(game_copy['board'])

            if state in self.value_function and self.value_function[state] > best_value:
                best_move = move
                best_value = self.value_function[state]

        if best_move is None:
            # If no values are available (initial state), choose a random valid move
            return random.choice(valid_moves)
        else:
            return best_move

    def learn_from_experience(self, state):
        state_copy = state.copy()
        state_copy['board'] = tuple(state_copy['board'])
        state_copy['reward'] = float(state_copy['reward'])

        if state_copy['board'] not in self.value_function:
            self.value_function[state_copy['board']] = 0

        self.value_function[state_copy['board']] += 0.1 * (state_copy['reward'] - self.value_function[state_copy['board']])

def main():
    env = MCRLEnvironment()
    agent1 = MCRLEAgent()
    agent2 = MCRLEAgent()

    for episode in range(10000):  # Training episodes
        env.play_game(agent1, agent2)
        env.reset()

    # Test the agent's performance against different opponents here

if _name_ == "_main_":
main()