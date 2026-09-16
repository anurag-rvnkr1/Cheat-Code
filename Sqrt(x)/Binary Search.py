'''
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in C++ or x ** 0.5 in Python.

Example 1:
    Input: x = 4
    Output: 2
    Explanation:
    The square root of 4 is 2, so we return 2.

Example 2:
    Input: x = 8
    Output: 2
    Explanation:
    The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
    0 <= x <= 2^31 - 1
'''

# Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


# Example usage
solution = Solution()

print(solution.mySqrt(4))  # Output: 2
print(solution.mySqrt(8))  # Output: 2
print(solution.mySqrt(0))  # Output: 0
print(solution.mySqrt(1))  # Output: 1
print(solution.mySqrt(16))  # Output: 4
print(solution.mySqrt(27))  # Output: 5
