'''
191. Number of 1 Bits

Write a function that takes the binary representation of an unsigned integer
and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
    In some languages, such as Java, there is no unsigned integer type.
    In this case, the input will be given as a signed integer type,
    but its internal binary representation remains the same.

Example 1:
    Input: n = 00000000000000000000000000001011
    Output: 3

Explanation:
    The input binary string has a total of three '1' bits.

Example 2:
    Input: n = 00000000000000000000000010000000
    Output: 1

Example 3:
    Input: n = 11111111111111111111111111111101
    Output: 31

Constraints:
    The input must be a binary string of length 32.
'''

# Bit Manipulation (Brian Kernighan's Algorithm)


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= (n - 1)
            count += 1

        return count


# Example usage
solution = Solution()

# Example 1
n1 = int("00000000000000000000000000001011", 2)
print(solution.hammingWeight(n1))  # Output: 3

# Example 2
n2 = int("00000000000000000000000010000000", 2)
print(solution.hammingWeight(n2))  # Output: 1

# Example 3
n3 = int("11111111111111111111111111111101", 2)
print(solution.hammingWeight(n3))  # Output: 31

# Example 4
n4 = 0
print(solution.hammingWeight(n4))  # Output: 0
