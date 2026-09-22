'''
488. Zuma Game

You are playing Zuma.

Board consists of colored balls:
    R, Y, B, G, W

Hand contains extra balls.

In one move:
    Insert one ball from hand anywhere on the board.

Whenever three or more consecutive balls have the same color,
they disappear. Chain reactions continue until no removal is possible.

Return the minimum number of balls needed to clear the board.
Return -1 if impossible.

Example 1:
    Input:
        board = "WRRBBW"
        hand = "RB"

    Output:
        -1

Example 2:
    Input:
        board = "WWRRBBWW"
        hand = "WRBRW"

    Output:
        2

Example 3:
    Input:
        board = "G"
        hand = "GGGGG"

    Output:
        2

Constraints:
    1 <= board.length <= 16
    1 <= hand.length <= 5
    board and hand contain only 'R','Y','B','G','W'.
'''

# DFS + Backtracking + Memoization

from functools import lru_cache
from collections import Counter


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_counter = Counter(hand)

        # Remove groups of >= 3 balls repeatedly.
        def shrink(current_board: str) -> str:
            changed = True

            while changed:
                changed = False
                index = 0
                new_board = ""

                while index < len(current_board):
                    end = index

                    while (
                        end < len(current_board)
                        and current_board[end] == current_board[index]
                    ):
                        end += 1

                    if end - index >= 3:
                        changed = True
                    else:
                        new_board += current_board[index:end]

                    index = end

                current_board = new_board

            return current_board

        @lru_cache(None)
        def dfs(current_board: str, hand_state: tuple) -> int:
            current_board = shrink(current_board)

            if not current_board:
                return 0

            current_hand = Counter(dict(hand_state))
            minimum_steps = float("inf")

            index = 0

            while index < len(current_board):
                end = index

                while (
                    end < len(current_board)
                    and current_board[end] == current_board[index]
                ):
                    end += 1

                color = current_board[index]
                balls_needed = 3 - (end - index)

                if current_hand[color] >= balls_needed > 0:
                    current_hand[color] -= balls_needed

                    next_board = current_board[:index] + current_board[end:]

                    result = dfs(
                        next_board,
                        tuple(sorted(current_hand.items()))
                    )

                    if result != float("inf"):
                        minimum_steps = min(
                            minimum_steps,
                            result + balls_needed
                        )

                    current_hand[color] += balls_needed

                index = end

            return minimum_steps

        answer = dfs(board, tuple(sorted(hand_counter.items())))

        return -1 if answer == float("inf") else answer


# Example usage
solution = Solution()

# Example 1
board1 = "WRRBBW"
hand1 = "RB"
print(solution.findMinStep(board1, hand1))
# Output: -1

# Example 2
board2 = "WWRRBBWW"
hand2 = "WRBRW"
print(solution.findMinStep(board2, hand2))
# Output: 2

# Example 3
board3 = "G"
hand3 = "GGGGG"
print(solution.findMinStep(board3, hand3))
# Output: 2

# Example 4
board4 = "RBYYBBRRB"
hand4 = "YRBGB"
print(solution.findMinStep(board4, hand4))
# Output: 3

# Example 5
board5 = "RRWWRRBBRR"
hand5 = "WB"
print(solution.findMinStep(board5, hand5))
# Output: 2

# Example 6
board6 = "BBBWW"
hand6 = "BW"
print(solution.findMinStep(board6, hand6))
# Output: 1
