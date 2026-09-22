'''
348. Design Tic-Tac-Toe

Assume the following rules:

    - Two players take turns placing marks.
    - Player 1 uses X.
    - Player 2 uses O.
    - Marks cannot be placed on occupied cells.
    - The first player to fill an entire row, column, or diagonal wins.

Implement the TicTacToe class:

    TicTacToe(int n)
        Initializes the board.

    int move(int row, int col, int player)
        Makes a move and returns:

            0 -> No winner.
            1 -> Player 1 wins.
            2 -> Player 2 wins.

Example:
    Input:
        ["TicTacToe","move","move","move","move","move","move","move"]

        [[3],[0,0,1],[0,2,2],[2,2,1],
         [1,1,2],[2,0,1],[1,0,2],[2,1,1]]

    Output:
        [null,0,0,0,0,0,0,1]

Constraints:
    2 <= n <= 100
    player is either 1 or 2.
    At most n² calls are made to move().
'''

# O(1) Matrix Design

class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        value = 1 if player == 1 else -1

        self.rows[row] += value
        self.cols[col] += value

        if row == col:
            self.diagonal += value

        if row + col == self.size - 1:
            self.anti_diagonal += value

        if (
            abs(self.rows[row]) == self.size or
            abs(self.cols[col]) == self.size or
            abs(self.diagonal) == self.size or
            abs(self.anti_diagonal) == self.size
        ):
            return player

        return 0


# Example usage
game = TicTacToe(3)

print(game.move(0, 0, 1))
# Output: 0

print(game.move(0, 2, 2))
# Output: 0

print(game.move(2, 2, 1))
# Output: 0

print(game.move(1, 1, 2))
# Output: 0

print(game.move(2, 0, 1))
# Output: 0

print(game.move(1, 0, 2))
# Output: 0

print(game.move(2, 1, 1))
# Output: 1
