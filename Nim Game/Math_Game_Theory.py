'''
292. Nim Game

You are playing the Nim Game with the following rules:

    - There is a heap of n stones.
    - Players take turns removing 1, 2, or 3 stones.
    - The player who removes the last stone wins.

Assuming both players play optimally, return True if you can win the game,
otherwise return False.

Example 1:
    Input: n = 4
    Output: False

Explanation:
    Whatever move you make (remove 1, 2, or 3 stones),
    your opponent can always take the remaining stones and win.

Example 2:
    Input: n = 1
    Output: True

Example 3:
    Input: n = 2
    Output: True

Constraints:
    1 <= n <= 2^31 - 1
'''

# Math + Game Theory


class Solution:
    def canWinNim(self, n: int) -> bool:
        # Losing positions are multiples of 4.
        return n % 4 != 0


# Example usage
solution = Solution()

# Example 1
n1 = 4
print(solution.canWinNim(n1))
# Output: False

# Example 2
n2 = 1
print(solution.canWinNim(n2))
# Output: True

# Example 3
n3 = 2
print(solution.canWinNim(n3))
# Output: True

# Example 4
n4 = 7
print(solution.canWinNim(n4))
# Output: True

# Example 5
n5 = 8
print(solution.canWinNim(n5))
# Output: False

# Example 6
n6 = 15
print(solution.canWinNim(n6))
# Output: True

# Example 7
n7 = 16
print(solution.canWinNim(n7))
# Output: False
