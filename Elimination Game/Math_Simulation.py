'''
390. Elimination Game

You have the list:

    [1,2,3,...,n]

Starting from left to right, remove the first number and every other number.

Then reverse direction and remove the first number and every other number again.

Repeat until only one number remains.

Return the last remaining number.

Example 1:
    Input:
        n = 9

    Output:
        6

Explanation:
        [1,2,3,4,5,6,7,8,9]
        -> [2,4,6,8]
        -> [2,6]
        -> [6]

Example 2:
    Input:
        n = 1

    Output:
        1

Constraints:
    1 <= n <= 10^9
'''

# Math + Simulation

class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left_to_right = True
        remaining = n

        while remaining > 1:

            if left_to_right or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head


# Example usage
solution = Solution()

# Example 1
n1 = 9
print(solution.lastRemaining(n1))
# Output: 6

# Example 2
n2 = 1
print(solution.lastRemaining(n2))
# Output: 1

# Example 3
n3 = 10
print(solution.lastRemaining(n3))
# Output: 8

# Example 4
n4 = 20
print(solution.lastRemaining(n4))
# Output: 6

# Example 5
n5 = 50
print(solution.lastRemaining(n5))
# Output: 24

# Example 6
n6 = 100
print(solution.lastRemaining(n6))
# Output: 54
