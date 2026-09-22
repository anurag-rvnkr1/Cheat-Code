'''
372. Super Pow

Your task is to calculate:

    a^b mod 1337

where b is given as an array of digits.

Example 1:
    Input:
        a = 2
        b = [3]

    Output:
        8

Example 2:
    Input:
        a = 2
        b = [1,0]

    Output:
        1024 % 1337 = 1024

Example 3:
    Input:
        a = 1
        b = [4,3,3,8,5,2]

    Output:
        1

Constraints:
    1 <= a <= 2^31 - 1
    1 <= b.length <= 2000
    0 <= b[i] <= 9
'''

# Math + Modular Exponentiation

from typing import List


class Solution:
    MOD = 1337

    def superPow(self, a: int, b: List[int]) -> int:
        def mod_pow(base: int, exponent: int) -> int:
            result = 1
            base %= self.MOD

            while exponent > 0:
                if exponent & 1:
                    result = (result * base) % self.MOD

                base = (base * base) % self.MOD
                exponent >>= 1

            return result

        result = 1

        for digit in b:
            result = (
                mod_pow(result, 10) *
                mod_pow(a, digit)
            ) % self.MOD

        return result


# Example usage
solution = Solution()

# Example 1
a1 = 2
b1 = [3]
print(solution.superPow(a1, b1))
# Output: 8

# Example 2
a2 = 2
b2 = [1,0]
print(solution.superPow(a2, b2))
# Output: 1024

# Example 3
a3 = 1
b3 = [4,3,3,8,5,2]
print(solution.superPow(a3, b3))
# Output: 1

# Example 4
a4 = 2147483647
b4 = [2,0]
print(solution.superPow(a4, b4))
# Output: 1198

# Example 5
a5 = 3
b5 = [1,0,0]
print(solution.superPow(a5, b5))
# Output: 816

# Example 6
a6 = 5
b6 = [9,9,9]
print(solution.superPow(a6, b6))
# Output: 1181
