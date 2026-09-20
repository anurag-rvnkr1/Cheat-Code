'''
157. Read N Characters Given read4

Given a file and assume that you can only read the file using a predefined
function read4(buf4), implement a function to read n characters into buf.

The read4 API:
    read4(buf4) reads up to 4 consecutive characters from the file into buf4
    and returns the number of characters actually read.

Your function:
    read(buf, n) reads up to n characters into buf and returns the number
    of characters actually read.

Example 1:
    Input:
        file = "abc"
        n = 4
    Output:
        3

Example 2:
    Input:
        file = "abcde"
        n = 5
    Output:
        5

Example 3:
    Input:
        file = "abcdABCD1234"
        n = 12
    Output:
        12

Constraints:
    1 <= n <= 1000
'''

# Simulation

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
    def read(self, buf: List[str], n: int) -> int:
        total_read = 0
        buf4 = [""] * 4

        while total_read < n:
            chars_read = read4(buf4)

            if chars_read == 0:
                break

            for i in range(chars_read):
                if total_read == n:
                    break

                buf[total_read] = buf4[i]
                total_read += 1

        return total_read


# Example usage
solution = Solution()

# Example 1
FILE_CONTENT = "abc"
FILE_POINTER = 0

buf = [""] * 4
count = solution.read(buf, 4)

print(count)                 # Output: 3
print("".join(buf[:count]))  # Output: abc

# Example 2
FILE_CONTENT = "abcde"
FILE_POINTER = 0

buf = [""] * 5
count = solution.read(buf, 5)

print(count)                 # Output: 5
print("".join(buf[:count]))  # Output: abcde

# Example 3
FILE_CONTENT = "abcdABCD1234"
FILE_POINTER = 0

buf = [""] * 12
count = solution.read(buf, 12)

print(count)                 # Output: 12
print("".join(buf[:count]))  # Output: abcdABCD1234
