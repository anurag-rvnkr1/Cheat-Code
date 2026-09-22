'''
481. Magical String

A magical string s consists only of '1' and '2' and satisfies:

    The groups of consecutive characters generate the string itself.

Beginning of the magical string:
    "1221121221221121122..."

Given an integer n, return the number of '1's in the first n characters.

Example 1:
    Input:
        n = 6

    Output:
        3

Explanation:
        First 6 characters = "122112"
        Number of '1's = 3

Example 2:
    Input:
        n = 1

    Output:
        1

Constraints:
    1 <= n <= 10^5
'''

# Simulation + Two Pointers


class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0

        if n <= 3:
            return 1

        magical = [1, 2, 2]

        read_pointer = 2
        next_digit = 1
        count_ones = 1

        while len(magical) < n:
            repeat = magical[read_pointer]

            for _ in range(repeat):
                magical.append(next_digit)

                if next_digit == 1 and len(magical) <= n:
                    count_ones += 1

            next_digit = 3 - next_digit
            read_pointer += 1

        return count_ones


# Example usage
solution = Solution()

# Example 1
n1 = 6
print(solution.magicalString(n1))
# Output: 3

# Example 2
n2 = 1
print(solution.magicalString(n2))
# Output: 1

# Example 3
n3 = 10
print(solution.magicalString(n3))
# Output: 5

# Example 4
n4 = 15
print(solution.magicalString(n4))
# Output: 7

# Example 5
n5 = 20
print(solution.magicalString(n5))
# Output: 10

# Example 6
n6 = 25
print(solution.magicalString(n6))
# Output: 13
