'''
388. Longest Absolute File Path

Suppose we have a file system represented as a string.

The string uses:
    '\\n' for a new directory/file.
    '\\t' for the depth (level).

Return the length of the longest absolute path to a file.

A file contains at least one '.' in its name.

Example 1:
    Input:
        input = "dir\\n\\tsubdir1\\n\\tsubdir2\\n\\t\\tfile.ext"

    Output:
        20

Explanation:
        Longest path:
        "dir/subdir2/file.ext"

Example 2:
    Input:
        input = "dir\\n\\tsubdir1\\n\\tsubdir2\\n\\t\\tfile.ext\\n\\t\\tsubsubdir"

    Output:
        20

Example 3:
    Input:
        input = "a"

    Output:
        0

Constraints:
    1 <= input.length <= 10^4
    input consists of English letters, digits, '.', '\\n', and '\\t'.
'''

# Stack + String Parsing

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # stack[level] = total path length up to this depth.
        stack = {0: 0}
        longest = 0

        for entry in input.split("\n"):

            depth = entry.count("\t")
            name = entry.lstrip("\t")

            current_length = stack[depth] + len(name)

            if "." in name:
                longest = max(longest, current_length)
            else:
                stack[depth + 1] = current_length + 1
                # +1 accounts for '/'

        return longest


# Example usage
solution = Solution()

# Example 1
input1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(solution.lengthLongestPath(input1))
# Output: 20

# Example 2
input2 = (
    "dir\n"
    "\tsubdir1\n"
    "\tsubdir2\n"
    "\t\tfile.ext\n"
    "\t\tsubsubdir"
)
print(solution.lengthLongestPath(input2))
# Output: 20

# Example 3
input3 = "a"
print(solution.lengthLongestPath(input3))
# Output: 0

# Example 4
input4 = "file1.txt\nfile2.txt\nlongfile.txt"
print(solution.lengthLongestPath(input4))
# Output: 12

# Example 5
input5 = (
    "dir\n"
    "\tsubdir1\n"
    "\t\tfile1.ext\n"
    "\t\tsubsubdir1\n"
    "\tsubdir2\n"
    "\t\tsubsubdir2\n"
    "\t\t\tfile2.ext"
)
print(solution.lengthLongestPath(input5))
# Output: 32

# Example 6
input6 = (
    "root\n"
    "\ta\n"
    "\t\tb\n"
    "\t\t\tc.txt\n"
    "\td\n"
    "\t\te.txt"
)
print(solution.lengthLongestPath(input6))
# Output: 16
