'''
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that:

    - Only numbers from 1 to 9 are used.
    - Each number is used at most once.
    - Return all possible valid combinations.

The solution set must not contain duplicate combinations.

Example 1:
    Input: k = 3, n = 7
    Output: [[1,2,4]]

Example 2:
    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]

Example 3:
    Input: k = 4, n = 1
    Output: []

Constraints:
    2 <= k <= 9
    1 <= n <= 60
'''

# Backtracking

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(start: int, remaining: int):
            # Valid combination found.
            if len(combination) == k and remaining == 0:
                result.append(combination[:])
                return

            # Stop exploring invalid paths.
            if len(combination) == k or remaining < 0:
                return

            for num in range(start, 10):
                combination.append(num)
                backtrack(num + 1, remaining - num)
                combination.pop()

        backtrack(1, n)
        return result


# Example usage
solution = Solution()

# Example 1
k1 = 3
n1 = 7
print(solution.combinationSum3(k1, n1))
# Output: [[1, 2, 4]]

# Example 2
k2 = 3
n2 = 9
print(solution.combinationSum3(k2, n2))
# Output: [[1,2,6],[1,3,5],[2,3,4]]

# Example 3
k3 = 4
n3 = 1
print(solution.combinationSum3(k3, n3))
# Output: []

# Example 4
k4 = 3
n4 = 15
print(solution.combinationSum3(k4, n4))
# Output: [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
