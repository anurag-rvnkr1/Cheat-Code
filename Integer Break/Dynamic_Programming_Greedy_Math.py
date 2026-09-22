'''
343. Integer Break

Given an integer n, break it into the sum of k positive integers,
where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:
    Input:
        n = 2

    Output:
        1

Explanation:
        2 = 1 + 1
        Product = 1

Example 2:
    Input:
        n = 10

    Output:
        36

Explanation:
        10 = 3 + 3 + 4
        Product = 36

Constraints:
    2 <= n <= 58
'''

# Dynamic Programming + Greedy Math

class Solution:
    def integerBreak(self, n: int) -> int:
        # Base cases
        if n == 2:
            return 1
        if n == 3:
            return 2

        product = 1

        # Break into as many 3's as possible.
        while n > 4:
            product *= 3
            n -= 3

        return product * n


# Example usage
solution = Solution()

# Example 1
n1 = 2
print(solution.integerBreak(n1))
# Output: 1

# Example 2
n2 = 10
print(solution.integerBreak(n2))
# Output: 36

# Example 3
n3 = 5
print(solution.integerBreak(n3))
# Output: 6

# Example 4
n4 = 8
print(solution.integerBreak(n4))
# Output: 18

# Example 5
n5 = 15
print(solution.integerBreak(n5))
# Output: 243

# Example 6
n6 = 20
print(solution.integerBreak(n6))
# Output: 1458
