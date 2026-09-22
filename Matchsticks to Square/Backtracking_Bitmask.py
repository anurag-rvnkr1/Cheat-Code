'''
473. Matchsticks to Square

You are given an integer array matchsticks where matchsticks[i] is the length
of the ith matchstick.

Determine if you can use all matchsticks exactly once to form a square.

Rules:
    - Do not break any matchstick.
    - Every matchstick must be used exactly once.

Return True if a square can be formed; otherwise False.

Example 1:
    Input:
        matchsticks = [1,1,2,2,2]

    Output:
        True

Explanation:
        Each side of the square has length 2.

Example 2:
    Input:
        matchsticks = [3,3,3,3,4]

    Output:
        False

Constraints:
    1 <= matchsticks.length <= 15
    1 <= matchsticks[i] <= 10^8
'''

# Backtracking + Bitmask / DFS

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        total_length = sum(matchsticks)

        if total_length % 4 != 0:
            return False

        target_side = total_length // 4

        # Largest matchsticks first for better pruning.
        matchsticks.sort(reverse=True)

        if matchsticks[0] > target_side:
            return False

        sides = [0] * 4

        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return (
                    sides[0] == sides[1] ==
                    sides[2] == sides[3] == target_side
                )

            current_matchstick = matchsticks[index]

            for side in range(4):
                if sides[side] + current_matchstick > target_side:
                    continue

                sides[side] += current_matchstick

                if backtrack(index + 1):
                    return True

                sides[side] -= current_matchstick

                # Optimization: avoid identical empty sides.
                if sides[side] == 0:
                    break

            return False

        return backtrack(0)


# Example usage
solution = Solution()

# Example 1
matchsticks1 = [1,1,2,2,2]
print(solution.makesquare(matchsticks1))
# Output: True

# Example 2
matchsticks2 = [3,3,3,3,4]
print(solution.makesquare(matchsticks2))
# Output: False

# Example 3
matchsticks3 = [5,5,5,5,4,4,4,4,3,3,3,3]
print(solution.makesquare(matchsticks3))
# Output: True

# Example 4
matchsticks4 = [1,1,1,1]
print(solution.makesquare(matchsticks4))
# Output: True

# Example 5
matchsticks5 = [1,2,2,2]
print(solution.makesquare(matchsticks5))
# Output: False

# Example 6
matchsticks6 = [10,6,5,5,5,5,4,4,4,4]
print(solution.makesquare(matchsticks6))
# Output: True
