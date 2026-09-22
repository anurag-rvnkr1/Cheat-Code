'''
423. Reconstruct Original Digits from English

Given a string s containing an out-of-order English representation of digits
from zero to nine, reconstruct the original digits in ascending order.

Each letter belongs to exactly one digit in the final answer.

Example 1:
    Input:
        s = "owoztneoer"

    Output:
        "012"

Explanation:
        The string contains "zero", "one", and "two".

Example 2:
    Input:
        s = "fviefuro"

    Output:
        "45"

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
'''

# HashMap + Frequency Counting

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        frequency = Counter(s)
        digits = [0] * 10

        # Unique identifying letters.
        digits[0] = frequency["z"]  # zero
        digits[2] = frequency["w"]  # two
        digits[4] = frequency["u"]  # four
        digits[6] = frequency["x"]  # six
        digits[8] = frequency["g"]  # eight

        # Derived digits.
        digits[3] = frequency["h"] - digits[8]            # three
        digits[5] = frequency["f"] - digits[4]            # five
        digits[7] = frequency["s"] - digits[6]            # seven
        digits[1] = frequency["o"] - digits[0] - digits[2] - digits[4]
        digits[9] = (
            frequency["i"] -
            digits[5] -
            digits[6] -
            digits[8]
        )

        result = []

        for digit in range(10):
            result.append(str(digit) * digits[digit])

        return "".join(result)


# Example usage
solution = Solution()

# Example 1
s1 = "owoztneoer"
print(solution.originalDigits(s1))
# Output: "012"

# Example 2
s2 = "fviefuro"
print(solution.originalDigits(s2))
# Output: "45"

# Example 3
s3 = "zerozero"
print(solution.originalDigits(s3))
# Output: "00"

# Example 4
s4 = "nnei"
print(solution.originalDigits(s4))
# Output: "9"

# Example 5
s5 = "ereht"
print(solution.originalDigits(s5))
# Output: "3"

# Example 6
s6 = "xsiowtneo"
print(solution.originalDigits(s6))
# Output: "026"
