'''
233. Number of Digit One

Given an integer n, count the total number of digit '1' appearing in all
non-negative integers less than or equal to n.

Example 1:
    Input: n = 13
    Output: 6

Explanation:
    The digit '1' appears in:
    1, 10, 11, 12, 13
    Total occurrences = 6.

Example 2:
    Input: n = 0
    Output: 0

Constraints:
    0 <= n <= 10^9
'''

# Digit DP + Math


class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1

        while place <= n:
            higher = n // (place * 10)
            current = (n // place) % 10
            lower = n % place

            if current == 0:
                count += higher * place

            elif current == 1:
                count += higher * place + lower + 1

            else:
                count += (higher + 1) * place

            place *= 10

        return count


# Example usage
solution = Solution()

# Example 1
n1 = 13
print(solution.countDigitOne(n1))  # Output: 6

# Example 2
n2 = 0
print(solution.countDigitOne(n2))  # Output: 0

# Example 3
n3 = 100
print(solution.countDigitOne(n3))  # Output: 21

# Example 4
n4 = 999
print(solution.countDigitOne(n4))  # Output: 300

# Example 5
n5 = 824883294
print(solution.countDigitOne(n5))  # Output: 767944060
