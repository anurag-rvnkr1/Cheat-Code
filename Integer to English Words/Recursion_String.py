'''
273. Integer to English Words

Convert a non-negative integer num to its English words representation.

Example 1:
    Input: num = 123
    Output: "One Hundred Twenty Three"

Example 2:
    Input: num = 12345
    Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
    Input: num = 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
    Input: num = 1234567891
    Output:
    "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand
     Eight Hundred Ninety One"

Constraints:
    0 <= num <= 2^31 - 1
'''

# Recursion + String


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_twenty = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        thousands = ["", "Thousand", "Million", "Billion"]

        def convert(number: int) -> str:
            if number == 0:
                return ""

            elif number < 20:
                return below_twenty[number] + " "

            elif number < 100:
                return tens[number // 10] + " " + convert(number % 10)

            else:
                return (
                    below_twenty[number // 100]
                    + " Hundred "
                    + convert(number % 100)
                )

        result = ""
        group = 0

        while num > 0:
            if num % 1000 != 0:
                result = (
                    convert(num % 1000)
                    + thousands[group]
                    + " "
                    + result
                )

            num //= 1000
            group += 1

        return result.strip()


# Example usage
solution = Solution()

# Example 1
num1 = 123
print(solution.numberToWords(num1))
# Output: One Hundred Twenty Three

# Example 2
num2 = 12345
print(solution.numberToWords(num2))
# Output: Twelve Thousand Three Hundred Forty Five

# Example 3
num3 = 1234567
print(solution.numberToWords(num3))
# Output: One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven

# Example 4
num4 = 1234567891
print(solution.numberToWords(num4))
# Output:
# One Billion Two Hundred Thirty Four Million
# Five Hundred Sixty Seven Thousand Eight Hundred Ninety One

# Example 5
num5 = 0
print(solution.numberToWords(num5))
# Output: Zero

# Example 6
num6 = 1000010
print(solution.numberToWords(num6))
# Output: One Million Ten
