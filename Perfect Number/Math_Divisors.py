'''
507. Perfect Number

A perfect number is a positive integer that is equal to the sum of its positive
divisors excluding itself.

Return True if num is a perfect number, otherwise False.

Example 1:
    Input:
        num = 28

    Output:
        True

Explanation:
        Divisors excluding 28 = [1,2,4,7,14]
        Sum = 28

Example 2:
    Input:
        num = 7

    Output:
        False

Constraints:
    1 <= num <= 10^8
'''

# Math + Divisors

import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 1 is not a perfect number.
        if num == 1:
            return False

        divisor_sum = 1

        limit = int(math.sqrt(num))

        for divisor in range(2, limit + 1):
            if num % divisor == 0:
                divisor_sum += divisor

                paired_divisor = num // divisor

                if paired_divisor != divisor:
                    divisor_sum += paired_divisor

        return divisor_sum == num


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.checkPerfectNumber(28))
# Output: True

# Example 2
print(solution.checkPerfectNumber(7))
# Output: False

# Example 3
print(solution.checkPerfectNumber(6))
# Output: True

# Example 4
print(solution.checkPerfectNumber(496))
# Output: True

# Example 5
print(solution.checkPerfectNumber(8128))
# Output: True

# Example 6
print(solution.checkPerfectNumber(33550336))
# Output: True
