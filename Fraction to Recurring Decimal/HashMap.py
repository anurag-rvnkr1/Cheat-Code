'''
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is recurring, enclose the recurring part in parentheses.

If multiple answers are possible, return any of them.

Example 1:
    Input: numerator = 1, denominator = 2
    Output: "0.5"

Example 2:
    Input: numerator = 2, denominator = 1
    Output: "2"

Example 3:
    Input: numerator = 4, denominator = 333
    Output: "0.(012)"

Constraints:
    -2^31 <= numerator, denominator <= 2^31 - 1
    denominator != 0
'''

# HashMap (Remainder Tracking)


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle negative numbers.
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part.
        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")

        # Store remainder positions.
        remainder_map = {}

        while remainder:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)


# Example usage
solution = Solution()

# Example 1
print(solution.fractionToDecimal(1, 2))  # Output: "0.5"

# Example 2
print(solution.fractionToDecimal(2, 1))  # Output: "2"

# Example 3
print(solution.fractionToDecimal(4, 333))  # Output: "0.(012)"

# Example 4
print(solution.fractionToDecimal(1, 6))  # Output: "0.1(6)"

# Example 5
print(solution.fractionToDecimal(-50, 8))  # Output: "-6.25"
