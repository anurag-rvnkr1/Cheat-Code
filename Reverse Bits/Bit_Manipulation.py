'''
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Note:
    In some languages such as Java, there is no unsigned integer type.
    In this case, both input and output will be given as a signed integer type,
    but the binary representation remains the same.

Example 1:
    Input: n = 00000010100101000001111010011100
    Output: 964176192

Explanation:
    Input Binary  = 00000010100101000001111010011100
    Output Binary = 00111001011110000010100101000000

Example 2:
    Input: n = 11111111111111111111111111111101
    Output: 3221225471

Explanation:
    Input Binary  = 11111111111111111111111111111101
    Output Binary = 10111111111111111111111111111111

Constraints:
    The input must be a binary string of length 32.
'''

# Bit Manipulation


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # Shift result to make room for the next bit.
            result <<= 1

            # Add the least significant bit of n.
            result |= (n & 1)

            # Shift n to process the next bit.
            n >>= 1

        return result


# Example usage
solution = Solution()

# Example 1
n1 = int("00000010100101000001111010011100", 2)
print(solution.reverseBits(n1))  # Output: 964176192

# Example 2
n2 = int("11111111111111111111111111111101", 2)
print(solution.reverseBits(n2))  # Output: 3221225471

# Example 3
n3 = 43261596
print(solution.reverseBits(n3))  # Output: 964176192

# Example 4
n4 = 4294967293
print(solution.reverseBits(n4))  # Output: 3221225471
