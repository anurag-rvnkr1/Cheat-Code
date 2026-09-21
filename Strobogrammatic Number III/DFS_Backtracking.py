'''
248. Strobogrammatic Number III

Given two strings low and high representing two integers low and high,
return the number of strobogrammatic numbers in the inclusive range [low, high].

A strobogrammatic number is a number that looks the same when rotated
180 degrees (looked at upside down).

Valid rotation pairs are:
    0 ↔ 0
    1 ↔ 1
    6 ↔ 9
    8 ↔ 8
    9 ↔ 6

Example 1:
    Input: low = "50", high = "100"
    Output: 3

Explanation:
    The strobogrammatic numbers between 50 and 100 are:
    69, 88, and 96.

Example 2:
    Input: low = "0", high = "0"
    Output: 1

Constraints:
    1 <= low.length <= high.length <= 15
    low and high consist of digits.
    low and high do not contain leading zeros (except "0").
    low <= high.
'''

# DFS + Backtracking

from typing import List


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = [
            ("0", "0"),
            ("1", "1"),
            ("6", "9"),
            ("8", "8"),
            ("9", "6")
        ]

        count = 0

        def build(length: int, total_length: int) -> List[str]:
            if length == 0:
                return [""]

            if length == 1:
                return ["0", "1", "8"]

            middle_strings = build(length - 2, total_length)
            result = []

            for middle in middle_strings:
                for left, right in pairs:
                    # No leading zero unless the number itself is "0".
                    if length == total_length and total_length > 1 and left == "0":
                        continue

                    result.append(left + middle + right)

            return result

        for length in range(len(low), len(high) + 1):
            for number in build(length, length):

                # Skip numbers outside the given range.
                if length == len(low) and number < low:
                    continue

                if length == len(high) and number > high:
                    continue

                count += 1

        return count


# Example usage
solution = Solution()

# Example 1
low1 = "50"
high1 = "100"
print(solution.strobogrammaticInRange(low1, high1))
# Output: 3

# Example 2
low2 = "0"
high2 = "0"
print(solution.strobogrammaticInRange(low2, high2))
# Output: 1

# Example 3
low3 = "0"
high3 = "10"
print(solution.strobogrammaticInRange(low3, high3))
# Output: 3

# Example 4
low4 = "100"
high4 = "1000"
print(solution.strobogrammaticInRange(low4, high4))
# Output: 12
