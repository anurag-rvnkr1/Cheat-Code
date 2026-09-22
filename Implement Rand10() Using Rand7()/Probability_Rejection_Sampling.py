'''
470. Implement Rand10() Using Rand7()

Given the API:

    rand7()

which returns a random integer in the range [1, 7].

Implement:

    rand10()

which returns a uniform random integer in the range [1, 10].

You may only call rand7().

Example 1:
    Input:
        rand10()

    Output:
        Random integer between 1 and 10.

Constraints:
    rand7() is predefined.
    Each outcome from rand10() must be equally likely.
'''

# Probability + Rejection Sampling

import random


# -------------------------------------------------------------------
# Mock rand7() implementation for local testing.
# On LeetCode, rand7() is already provided by the platform.
# -------------------------------------------------------------------
def rand7() -> int:
    return random.randint(1, 7)


class Solution:
    def rand10(self) -> int:
        while True:
            # Generate a number uniformly in [1, 49].
            row = rand7()
            col = rand7()

            number = (row - 1) * 7 + col

            # Accept only first 40 numbers.
            if number <= 40:
                return (number - 1) % 10 + 1


# Example usage
solution = Solution()

# Example 1
print(solution.rand10())
# Output: Random integer from 1 to 10.

# Example 2
print(solution.rand10())
# Output: Random integer from 1 to 10.

# Example 3
print(solution.rand10())
# Output: Random integer from 1 to 10.

# Example 4
print(solution.rand10())
# Output: Random integer from 1 to 10.

# Example 5
print(solution.rand10())
# Output: Random integer from 1 to 10.

# Example 6
print(solution.rand10())
# Output: Random integer from 1 to 10.

# Sample frequency check (optional)
frequency = {i: 0 for i in range(1, 11)}

for _ in range(10000):
    frequency[solution.rand10()] += 1

print(frequency)
# Expected:
# Roughly equal frequencies for numbers 1 through 10.
