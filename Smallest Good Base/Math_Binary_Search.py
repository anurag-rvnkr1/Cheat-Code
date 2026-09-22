'''
483. Smallest Good Base

For an integer n represented as a string, find the smallest good base k.

A good base satisfies:

    n = 1 + k + k² + ... + kᵐ

for some integer m >= 1.

Return the smallest good base as a string.

Example 1:
    Input:
        n = "13"

    Output:
        "3"

Explanation:
        13 = 1 + 3 + 9

Example 2:
    Input:
        n = "4681"

    Output:
        "8"

Explanation:
        4681 = 1 + 8 + 64 + 512 + 4096

Example 3:
    Input:
        n = "1000000000000000000"

    Output:
        "999999999999999999"

Constraints:
    n is in the range [3, 10¹⁸].
'''

# Math + Binary Search

import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        number = int(n)

        # Maximum possible exponent.
        max_power = int(math.log2(number))

        # Try longer representations first.
        for power in range(max_power, 1, -1):
            left = 2
            right = int(number ** (1 / power)) + 1

            while left <= right:
                base = (left + right) // 2

                total = 1
                current = 1

                # Compute geometric series.
                for _ in range(power):
                    current *= base
                    total += current

                    if total > number:
                        break

                if total == number:
                    return str(base)

                if total < number:
                    left = base + 1
                else:
                    right = base - 1

        # Always valid with power = 1.
        return str(number - 1)


# Example usage
solution = Solution()

# Example 1
n1 = "13"
print(solution.smallestGoodBase(n1))
# Output: "3"

# Example 2
n2 = "4681"
print(solution.smallestGoodBase(n2))
# Output: "8"

# Example 3
n3 = "1000000000000000000"
print(solution.smallestGoodBase(n3))
# Output: "999999999999999999"

# Example 4
n4 = "31"
print(solution.smallestGoodBase(n4))
# Output: "2"

# Example 5
n5 = "21"
print(solution.smallestGoodBase(n5))
# Output: "4"

# Example 6
n6 = "1099511627775"
print(solution.smallestGoodBase(n6))
# Output: "2"
