'''
319. Bulb Switcher

There are n bulbs that are initially off.

You perform n rounds of toggling:

    Round 1:
        Toggle every bulb.

    Round 2:
        Toggle every 2nd bulb.

    Round 3:
        Toggle every 3rd bulb.

    ...

    Round n:
        Toggle only the nth bulb.

Return the number of bulbs that remain on after n rounds.

Example 1:
    Input: n = 3
    Output: 1

Explanation:
    Round 1 -> [ON, ON, ON]
    Round 2 -> [ON, OFF, ON]
    Round 3 -> [ON, OFF, OFF]

    Only bulb 1 remains ON.

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 1

Constraints:
    0 <= n <= 10^9
'''

# Math + Number Theory

import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Only perfect squares remain ON.
        return math.isqrt(n)


# Example usage
solution = Solution()

# Example 1
n1 = 3
print(solution.bulbSwitch(n1))
# Output: 1

# Example 2
n2 = 0
print(solution.bulbSwitch(n2))
# Output: 0

# Example 3
n3 = 1
print(solution.bulbSwitch(n3))
# Output: 1

# Example 4
n4 = 10
print(solution.bulbSwitch(n4))
# Output: 3
# Bulbs ON: 1,4,9

# Example 5
n5 = 25
print(solution.bulbSwitch(n5))
# Output: 5
# Bulbs ON: 1,4,9,16,25

# Example 6
n6 = 100
print(solution.bulbSwitch(n6))
# Output: 10
