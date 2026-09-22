'''
326. Power of Three

Given an integer n, return True if it is a power of three.
Otherwise, return False.

An integer n is a power of three if there exists an integer x such that:

    n = 3^x

Example 1:
    Input: n = 27
    Output: True

Example 2:
    Input: n = 0
    Output: False

Example 3:
    Input: n = -1
    Output: False

Example 4:
    Input: n = 9
    Output: True

Constraints:
    -2^31 <= n <= 2^31 - 1

Follow-up:
    Could you solve it without loops or recursion?
'''

# Math + Number Theory

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Powers of three must be positive.
        if n <= 0:
            return False

        # Largest power of 3 within signed 32-bit integer.
        MAX_POWER_OF_THREE = 1162261467   # 3^19

        return MAX_POWER_OF_THREE % n == 0


# Example usage
solution = Solution()

# Example 1
print(solution.isPowerOfThree(27))
# Output: True

# Example 2
print(solution.isPowerOfThree(0))
# Output: False

# Example 3
print(solution.isPowerOfThree(-1))
# Output: False

# Example 4
print(solution.isPowerOfThree(9))
# Output: True

# Example 5
print(solution.isPowerOfThree(45))
# Output: False

# Example 6
print(solution.isPowerOfThree(243))
# Output: True
