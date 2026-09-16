'''
65. Valid Number

Given a string s, return whether s is a valid number.

For example, all the following are valid numbers:
"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"

The following are not valid numbers:
"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"

Formally, a valid number is defined using one of the following definitions:

1. An integer number followed by an optional exponent.
2. A decimal number followed by an optional exponent.

An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
1. Digits followed by a dot '.'.
2. Digits followed by a dot '.' followed by digits.
3. A dot '.' followed by digits.

An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

Example 1:
    Input: s = "0"
    Output: True

Example 2:
    Input: s = "e"
    Output: False

Example 3:
    Input: s = "."
    Output: False

Constraints:
    1 <= s.length <= 20
    s consists of only English letters (both uppercase and lowercase), digits (0-9), '+', '-', or '.'
'''

# Finite State Validation
class Solution:
    def isNumber(self, s: str) -> bool:

        seen_digit = False
        seen_dot = False
        seen_exponent = False
        digit_after_exponent = True

        for i, ch in enumerate(s):

            # Digit
            if ch.isdigit():
                seen_digit = True

                if seen_exponent:
                    digit_after_exponent = True

            # Decimal point
            elif ch == '.':
                # Dot is not allowed after an exponent
                if seen_dot or seen_exponent:
                    return False

                seen_dot = True

            # Exponent
            elif ch == 'e' or ch == 'E':
                # Exponent requires digits before it
                # and there can only be one exponent
                if seen_exponent or not seen_digit:
                    return False

                seen_exponent = True
                digit_after_exponent = False

            # Sign
            elif ch == '+' or ch == '-':
                # Sign is allowed only at the beginning
                # or immediately after e/E
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            # Anything else is invalid
            else:
                return False

        return seen_digit and digit_after_exponent


# Example usage
solution = Solution()

print(solution.isNumber("0"))  # Output: True
print(solution.isNumber("e"))  # Output: False
print(solution.isNumber("."))  # Output: False
print(solution.isNumber("-0.1"))  # Output: True
print(solution.isNumber("53.5e93"))  # Output: True
print(solution.isNumber("99e2.5"))  # Output: False
