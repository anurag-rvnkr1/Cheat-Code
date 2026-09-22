'''
393. UTF-8 Validation

Given an integer array data representing bytes, return True if it is
a valid UTF-8 encoding, otherwise return False.

A character in UTF-8 can be from 1 to 4 bytes long.

UTF-8 Rules:
    1-byte character:
        0xxxxxxx

    2-byte character:
        110xxxxx 10xxxxxx

    3-byte character:
        1110xxxx 10xxxxxx 10xxxxxx

    4-byte character:
        11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Example 1:
    Input:
        data = [197,130,1]

    Output:
        True

Example 2:
    Input:
        data = [235,140,4]

    Output:
        False

Constraints:
    1 <= data.length <= 2 * 10^4
    0 <= data[i] <= 255
'''

# Bit Manipulation

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining_bytes = 0

        for byte in data:
            if remaining_bytes == 0:
                if byte >> 7 == 0:
                    continue

                elif byte >> 5 == 0b110:
                    remaining_bytes = 1

                elif byte >> 4 == 0b1110:
                    remaining_bytes = 2

                elif byte >> 3 == 0b11110:
                    remaining_bytes = 3

                else:
                    return False

            else:
                if byte >> 6 != 0b10:
                    return False

                remaining_bytes -= 1

        return remaining_bytes == 0


# Example usage
solution = Solution()

# Example 1
data1 = [197,130,1]
print(solution.validUtf8(data1))
# Output: True

# Example 2
data2 = [235,140,4]
print(solution.validUtf8(data2))
# Output: False

# Example 3
data3 = [240,162,138,147]
print(solution.validUtf8(data3))
# Output: True

# Example 4
data4 = [255]
print(solution.validUtf8(data4))
# Output: False

# Example 5
data5 = [226,130,172]
print(solution.validUtf8(data5))
# Output: True

# Example 6
data6 = [145]
print(solution.validUtf8(data6))
# Output: False
