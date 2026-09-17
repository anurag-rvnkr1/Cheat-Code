'''
96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which have exactly n nodes of unique values from 1 to n.

Example 1:
    Input: n = 3
    Output: 5

Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 19
'''

# Dynamic Programming (Catalan Number)
class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):

            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root

                dp[nodes] += dp[left] * dp[right]

        return dp[n]


# Example usage
solution = Solution()

print(solution.numTrees(3))  # Output: 5
print(solution.numTrees(1))  # Output: 1
print(solution.numTrees(2))  # Output: 2
print(solution.numTrees(5))  # Output: 42
