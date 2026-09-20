'''
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears
in an Excel sheet.

For example:
    1  -> A
    2  -> B
    26 -> Z
    27 -> AA
    28 -> AB

Example 1:
    Input: columnNumber = 1
    Output: "A"

Example 2:
    Input: columnNumber = 28
    Output: "AB"

Example 3:
    Input: columnNumber = 701
    Output: "ZY"

Constraints:
    1 <= columnNumber <= 2^31 - 1
'''

# Math (Base-26 Conversion)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr((columnNumber % 26) + ord("A")))
            columnNumber //= 26

        return "".join(reversed(result))


# Example usage
solution = Solution()

# Example 1
columnNumber1 = 1
print(solution.convertToTitle(columnNumber1))  # Output: A

# Example 2
columnNumber2 = 28
print(solution.convertToTitle(columnNumber2))  # Output: AB

# Example 3
columnNumber3 = 701
print(solution.convertToTitle(columnNumber3))  # Output: ZY

# Example 4
columnNumber4 = 2147483647
print(solution.convertToTitle(columnNumber4))  # Output: FXSHRXW
