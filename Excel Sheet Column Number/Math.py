'''
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as it appears
in an Excel sheet, return its corresponding column number.

For example:
    A  -> 1
    B  -> 2
    Z  -> 26
    AA -> 27
    AB -> 28
    ZY -> 701

Example 1:
    Input: columnTitle = "A"
    Output: 1

Example 2:
    Input: columnTitle = "AB"
    Output: 28

Example 3:
    Input: columnTitle = "ZY"
    Output: 701

Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].
'''

# Math (Base-26 Conversion)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0

        for ch in columnTitle:
            column_number = column_number * 26 + (ord(ch) - ord("A") + 1)

        return column_number


# Example usage
solution = Solution()

# Example 1
columnTitle1 = "A"
print(solution.titleToNumber(columnTitle1))  # Output: 1

# Example 2
columnTitle2 = "AB"
print(solution.titleToNumber(columnTitle2))  # Output: 28

# Example 3
columnTitle3 = "ZY"
print(solution.titleToNumber(columnTitle3))  # Output: 701

# Example 4
columnTitle4 = "FXSHRXW"
print(solution.titleToNumber(columnTitle4))  # Output: 2147483647
