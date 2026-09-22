'''
441. Arranging Coins

You have n coins and want to build a staircase.

The staircase consists of k rows where:
    Row 1 has 1 coin.
    Row 2 has 2 coins.
    ...
    Row k has k coins.

The last row may be incomplete.

Return the total number of complete rows that can be formed.

Example 1:
    Input:
        n = 5

    Output:
        2

Explanation:
        Row 1 -> 1 coin
        Row 2 -> 2 coins
        Remaining -> 2 coins (cannot complete Row 3)

Example 2:
    Input:
        n = 8

    Output:
        3

Explanation:
        Row 1 -> 1
        Row 2 -> 2
        Row 3 -> 3
        Remaining -> 2

Constraints:
    1 <= n <= 2^31 - 1
'''

# Binary Search + Math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            middle = left + (right - left) // 2

            coins_needed = middle * (middle + 1) // 2

            if coins_needed == n:
                return middle

            if coins_needed < n:
                left = middle + 1
            else:
                right = middle - 1

        return right


# Example usage
solution = Solution()

# Example 1
n1 = 5
print(solution.arrangeCoins(n1))
# Output: 2

# Example 2
n2 = 8
print(solution.arrangeCoins(n2))
# Output: 3

# Example 3
n3 = 1
print(solution.arrangeCoins(n3))
# Output: 1

# Example 4
n4 = 3
print(solution.arrangeCoins(n4))
# Output: 2

# Example 5
n5 = 10
print(solution.arrangeCoins(n5))
# Output: 4

# Example 6
n6 = 1804289383
print(solution.arrangeCoins(n6))
# Output: 60070
