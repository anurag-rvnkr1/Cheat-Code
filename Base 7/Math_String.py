'''
504. Base 7

Given an integer num, return its base-7 representation as a string.

Example 1:
    Input:
        num = 100

    Output:
        "202"

Example 2:
    Input:
        num = -7

    Output:
        "-10"

Constraints:
    -10^7 <= num <= 10^7
'''

# Math + String

class Solution:
    def convertToBase7(self, num: int) -> str:
        # Special case for zero.
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)

        digits = []

        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        base7 = "".join(reversed(digits))

        if is_negative:
            return "-" + base7

        return base7


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.convertToBase7(100))
# Output: "202"

# Example 2
print(solution.convertToBase7(-7))
# Output: "-10"

# Example 3
print(solution.convertToBase7(0))
# Output: "0"

# Example 4
print(solution.convertToBase7(49))
# Output: "100"

# Example 5
print(solution.convertToBase7(-100))
# Output: "-202"

# Example 6
print(solution.convertToBase7(343))
# Output: "1000"
