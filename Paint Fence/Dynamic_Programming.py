'''
276. Paint Fence

There is a fence with n posts, and each post can be painted with one of k colors.

You must paint all the posts such that no more than two adjacent fence posts
have the same color.

Return the total number of valid ways to paint the fence.

Example 1:
    Input: n = 3, k = 2
    Output: 6

Explanation:
    Valid ways:
    [1,1,2], [1,2,1], [1,2,2],
    [2,1,1], [2,1,2], [2,2,1]

Example 2:
    Input: n = 1, k = 1
    Output: 1

Example 3:
    Input: n = 7, k = 2
    Output: 42

Constraints:
    1 <= n <= 50
    1 <= k <= 10^5
'''

# Dynamic Programming


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k

        # same = last two posts have the same color.
        # different = last two posts have different colors.
        same = k
        different = k * (k - 1)

        for _ in range(3, n + 1):
            new_same = different
            new_different = (same + different) * (k - 1)

            same = new_same
            different = new_different

        return same + different


# Example usage
solution = Solution()

# Example 1
n1, k1 = 3, 2
print(solution.numWays(n1, k1))
# Output: 6

# Example 2
n2, k2 = 1, 1
print(solution.numWays(n2, k2))
# Output: 1

# Example 3
n3, k3 = 7, 2
print(solution.numWays(n3, k3))
# Output: 42

# Example 4
n4, k4 = 2, 3
print(solution.numWays(n4, k4))
# Output: 9

# Example 5
n5, k5 = 4, 3
print(solution.numWays(n5, k5))
# Output: 66
