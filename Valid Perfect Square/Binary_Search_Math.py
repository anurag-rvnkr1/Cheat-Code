'''
367. Valid Perfect Square

Given a positive integer num, return True if num is a perfect square,
otherwise return False.

Do not use any built-in library function such as sqrt().

Example 1:
    Input:
        num = 16

    Output:
        True

Example 2:
    Input:
        num = 14

    Output:
        False

Constraints:
    1 <= num <= 2^31 - 1
'''

# Binary Search + Math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 1
        right = num

        while left <= right:
            middle = left + (right - left) // 2
            square = middle * middle

            if square == num:
                return True

            if square < num:
                left = middle + 1
            else:
                right = middle - 1

        return False


# Example usage
solution = Solution()

# Example 1
print(solution.isPerfectSquare(16))
# Output: True

# Example 2
print(solution.isPerfectSquare(14))
# Output: False

# Example 3
print(solution.isPerfectSquare(1))
# Output: True

# Example 4
print(solution.isPerfectSquare(25))
# Output: True

# Example 5
print(solution.isPerfectSquare(2147395600))
# Output: True

# Example 6
print(solution.isPerfectSquare(2147483647))
# Output: False
