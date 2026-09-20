'''
158. Read N Characters Given read4 II - Call Multiple Times

Given a file and assume that you can only read the file using a predefined
function read4(buf4), implement a function that can be called multiple times.

The read(buf, n) function reads up to n characters into buf and returns the
number of characters actually read.

Note:
    The read function may be called multiple times.

Example 1:
    Input:
        file = "abc"
        read(1)
        read(2)
    Output:
        1, 2

Example 2:
    Input:
        file = "abcde"
        read(3)
        read(2)
    Output:
        3, 2

Example 3:
    Input:
        file = "abcdABCD1234"
        read(5)
        read(3)
        read(4)
    Output:
        5, 3, 4

Constraints:
    1 <= n <= 1000
'''

# Simulation with Internal Buffer

from typing import List

# ------------------------------------------------------------------
# Mock read4 API for local testing.
# LeetCode provides this API automatically.
# ------------------------------------------------------------------
FILE_CONTENT = ""
FILE_POINTER = 0


def read4(buf4: List[str]) -> int:
    global FILE_POINTER

    count = 0

    while count < 4 and FILE_POINTER < len(FILE_CONTENT):
        buf4[count] = FILE_CONTENT[FILE_POINTER]
        FILE_POINTER += 1
        count += 1

    return count


class Solution:
    def __init__(self):
        self.buffer4 = [""] * 4
        self.buffer_pointer = 0
        self.buffer_count = 0

    def read(self, buf: List[str], n: int) -> int:
        total_read = 0

        while total_read < n:

            # Fill internal buffer when empty.
            if self.buffer_pointer == self.buffer_count:
                self.buffer_count = read4(self.buffer4)
                self.buffer_pointer = 0

                if self.buffer_count == 0:
                    break

            # Copy characters from internal buffer.
            while total_read < n and self.buffer_pointer < self.buffer_count:
                buf[total_read] = self.buffer4[self.buffer_pointer]
                total_read += 1
                self.buffer_pointer += 1

        return total_read


# Example usage
FILE_CONTENT = "abcdABCD1234"
FILE_POINTER = 0

reader = Solution()

# Example 1
buf1 = [""] * 5
count1 = reader.read(buf1, 5)

print(count1)                  # Output: 5
print("".join(buf1[:count1]))  # Output: abcdA

# Example 2
buf2 = [""] * 3
count2 = reader.read(buf2, 3)

print(count2)                  # Output: 3
print("".join(buf2[:count2]))  # Output: BCD

# Example 3
buf3 = [""] * 4
count3 = reader.read(buf3, 4)

print(count3)                  # Output: 4
print("".join(buf3[:count3]))  # Output: 1234
