'''
464. Can I Win

Two players take turns choosing integers from 1 to maxChoosableInteger.

Rules:
    - Each number can be chosen only once.
    - The chosen number is added to a running total.
    - The player who reaches or exceeds desiredTotal first wins.

Assuming both players play optimally, return True if the first player can force a win.

Example 1:
    Input:
        maxChoosableInteger = 10
        desiredTotal = 11

    Output:
        False

Example 2:
    Input:
        maxChoosableInteger = 10
        desiredTotal = 0

    Output:
        True

Example 3:
    Input:
        maxChoosableInteger = 10
        desiredTotal = 1

    Output:
        True

Constraints:
    1 <= maxChoosableInteger <= 20
    0 <= desiredTotal <= 300
'''

# Dynamic Programming + Bitmask + Memoization

from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Immediate win.
        if desiredTotal <= 0:
            return True

        # Impossible to reach desiredTotal.
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total_sum < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(used_mask: int, remaining: int) -> bool:
            for number in range(1, maxChoosableInteger + 1):
                bit = 1 << (number - 1)

                if used_mask & bit:
                    continue

                # Current player wins immediately.
                if number >= remaining:
                    return True

                # Opponent loses.
                if not dfs(used_mask | bit, remaining - number):
                    return True

            return False

        return dfs(0, desiredTotal)


# Example usage
solution = Solution()

# Example 1
print(solution.canIWin(10, 11))
# Output: False

# Example 2
print(solution.canIWin(10, 0))
# Output: True

# Example 3
print(solution.canIWin(10, 1))
# Output: True

# Example 4
print(solution.canIWin(5, 6))
# Output: False

# Example 5
print(solution.canIWin(20, 210))
# Output: False

# Example 6
print(solution.canIWin(18, 79))
# Output: True
