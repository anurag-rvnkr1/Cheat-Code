'''
254. Factor Combinations

Numbers can be regarded as the product of their factors.

For example:
    8 = 2 × 2 × 2
    = 2 × 4

Given an integer n, return all possible combinations of its factors.

You may return the answer in any order.

Note:
    - Each combination's factors must be in non-decreasing order.
    - Do not include the number itself as a single factor.

Example 1:
    Input: n = 1
    Output: []

Example 2:
    Input: n = 12
    Output: [[2,6],[2,2,3],[3,4]]

Constraints:
    1 <= n <= 10^7
'''

# Backtracking + DFS

from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, target: int, path: List[int]):
            factor = start

            while factor * factor <= target:

                if target % factor == 0:
                    # Found a valid factor pair.
                    result.append(path + [factor, target // factor])

                    # Continue searching for more factors.
                    backtrack(
                        factor,
                        target // factor,
                        path + [factor]
                    )

                factor += 1

        backtrack(2, n, [])
        return result


# Example usage
solution = Solution()

# Example 1
n1 = 1
print(solution.getFactors(n1))
# Output: []

# Example 2
n2 = 12
print(solution.getFactors(n2))
# Output: [[2,6],[2,2,3],[3,4]]

# Example 3
n3 = 16
print(solution.getFactors(n3))
# Output:
# [[2,8],[2,2,4],[2,2,2,2],[4,4]]

# Example 4
n4 = 32
print(solution.getFactors(n4))
# Output:
# [[2,16],[2,2,8],[2,2,2,4],[2,2,2,2,2],[2,4,4],[4,8]]
