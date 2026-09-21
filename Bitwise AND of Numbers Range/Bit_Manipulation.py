'''
201. Bitwise AND of Numbers Range

Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.

Example 1:
    Input: left = 5, right = 7
    Output: 4

Explanation:
    5 = 101
    6 = 110
    7 = 111

    101
  & 110
  & 111
  -----
    100 = 4

Example 2:
    Input: left = 0, right = 0
    Output: 0

Example 3:
    Input: left = 1, right = 2147483647
    Output: 0

Constraints:
    0 <= left <= right <= 2^31 - 1
'''

# Bit Manipulation (Common Prefix)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        # Remove different suffix bits until both numbers become equal.
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Restore the common prefix.
        return left << shift


# Example usage
solution = Solution()

# Example 1
left1 = 5
right1 = 7
print(solution.rangeBitwiseAnd(left1, right1))  # Output: 4

# Example 2
left2 = 0
right2 = 0
print(solution.rangeBitwiseAnd(left2, right2))  # Output: 0

# Example 3
left3 = 1
right3 = 2147483647
print(solution.rangeBitwiseAnd(left3, right3))  # Output: 0

# Example 4
left4 = 12
right4 = 15
print(solution.rangeBitwiseAnd(left4, right4))  # Output: 12
