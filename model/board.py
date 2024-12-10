class Board:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [[" " for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.grid:
            print("|".join(row))
            print("-" * (2 * self.cols - 1))

    def is_valid_move(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == " "

    def make_move(self, row: int, col: int, symbol: str) -> bool:
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol: str) -> bool:
        # Check rows, columns, and diagonals for winning condition
        for i in range(self.rows):
            if all(self.grid[i][j] == symbol for j in range(self.cols)):
                return True
        for j in range(self.cols):
            if all(self.grid[i][j] == symbol for i in range(self.rows)):
                return True
        if all(self.grid[i][i] == symbol for i in range(min(self.rows, self.cols))) or \
           all(self.grid[i][self.cols - i - 1] == symbol for i in range(min(self.rows, self.cols))):
            return True
        return False

    def is_full(self) -> bool:
        return all(cell != " " for row in self.grid for cell in row)
