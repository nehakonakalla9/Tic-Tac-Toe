from model.board import Board
from model.player import Player
from model.piecetype import PieceType

class Game:
    def __init__(self, rows: int, cols: int, players: list[Player]):
        self.board = Board(rows, cols)
        self.players = players
        self.current_turn = 0

    def start(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.board.display()
            current_player = self.players[self.current_turn]
            print(f"{current_player.name}'s Turn ({current_player.piece}):")
            
            try:
                row, col = map(int, input("Enter row and column (0-based index): ").split())
            except ValueError:
                print("Invalid input! Enter two numbers separated by a space.")
                continue
            
            if not self.board.make_move(row, col, current_player.piece):
                print("Invalid move! Try again.")
                continue

            if self.board.check_winner(current_player.piece):
                self.board.display()
                print(f"Congratulations {current_player.name}, you win!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            self.current_turn = (self.current_turn + 1) % len(self.players)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    num_players = int(input("Enter number of players: "))
    
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ")
        symbol = input(f"Enter symbol for Player {i + 1} (e.g., X, O): ")
        players.append(Player(name, symbol))
    
    game = Game(rows, cols, players)
    game.start()
