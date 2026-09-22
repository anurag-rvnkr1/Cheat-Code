'''
461. Hamming Distance

The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:
    Input:
        x = 1
        y = 4

    Output:
        2

Explanation:
        1  -> 0001
        4  -> 0100
        XOR -> 0101 (2 set bits)

Example 2:
    Input:
        x = 3
        y = 1

    Output:
        1

Constraints:
    0 <= x, y <= 2^31 - 1
'''

# Bit Manipulation (Brian Kernighan's Algorithm)


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_value = x ^ y
        distance = 0

        while xor_value:
            xor_value &= xor_value - 1
            distance += 1

        return distance


# Example usage
solution = Solution()

# Example 1
x1 = 1
y1 = 4
print(solution.hammingDistance(x1, y1))
# Output: 2

# Example 2
x2 = 3
y2 = 1
print(solution.hammingDistance(x2, y2))
# Output: 1

# Example 3
x3 = 0
y3 = 0
print(solution.hammingDistance(x3, y3))
# Output: 0

# Example 4
x4 = 15
y4 = 0
print(solution.hammingDistance(x4, y4))
# Output: 4

# Example 5
x5 = 25
y5 = 30
print(solution.hammingDistance(x5, y5))
# Output: 3

# Example 6
x6 = 1023
y6 = 511
print(solution.hammingDistance(x6, y6))
# Output: 1
