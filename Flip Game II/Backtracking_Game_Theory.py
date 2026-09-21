'''
294. Flip Game II

You are playing the Flip Game against another player.

Rules:
    - You are given a string currentState consisting of '+' and '-'.
    - Players take turns flipping any occurrence of "++" into "--".
    - The player who cannot make a move loses.

Return True if the starting player can guarantee a win assuming both players
play optimally.

Example 1:
    Input: currentState = "++++"
    Output: True

Explanation:
    The starting player can force a winning sequence.

Example 2:
    Input: currentState = "+"
    Output: False

Constraints:
    1 <= currentState.length <= 60
    currentState[i] is either '+' or '-'.
'''

# Backtracking + Game Theory + Memoization


class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}

        def dfs(state: str) -> bool:
            if state in memo:
                return memo[state]

            # Try every possible move.
            for i in range(len(state) - 1):
                if state[i:i + 2] == "++":
                    next_state = (
                        state[:i] +
                        "--" +
                        state[i + 2:]
                    )

                    # If opponent loses, current player wins.
                    if not dfs(next_state):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return dfs(currentState)


# Example usage
solution = Solution()

# Example 1
state1 = "++++"
print(solution.canWin(state1))
# Output: True

# Example 2
state2 = "+"
print(solution.canWin(state2))
# Output: False

# Example 3
state3 = "++"
print(solution.canWin(state3))
# Output: True

# Example 4
state4 = "+++++"
print(solution.canWin(state4))
# Output: False

# Example 5
state5 = "++++++"
print(solution.canWin(state5))
# Output: True
