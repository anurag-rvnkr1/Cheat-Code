'''
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

The returned number should not contain leading zeros.

If the result is empty, return "0".

Example 1:
    Input:
        num = "1432219"
        k = 3

    Output:
        "1219"

Example 2:
    Input:
        num = "10200"
        k = 1

    Output:
        "200"

Example 3:
    Input:
        num = "10"
        k = 2

    Output:
        "0"

Constraints:
    1 <= k <= num.length <= 10^5
    num consists of digits only.
    num does not have leading zeros except for the number 0 itself.
'''

# Monotonic Stack + Greedy

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # Remove remaining digits from the end if needed.
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros.
        result = "".join(stack).lstrip("0")

        return result if result else "0"


# Example usage
solution = Solution()

# Example 1
num1 = "1432219"
k1 = 3
print(solution.removeKdigits(num1, k1))
# Output: "1219"

# Example 2
num2 = "10200"
k2 = 1
print(solution.removeKdigits(num2, k2))
# Output: "200"

# Example 3
num3 = "10"
k3 = 2
print(solution.removeKdigits(num3, k3))
# Output: "0"

# Example 4
num4 = "112"
k4 = 1
print(solution.removeKdigits(num4, k4))
# Output: "11"

# Example 5
num5 = "100200"
k5 = 1
print(solution.removeKdigits(num5, k5))
# Output: "200"

# Example 6
num6 = "5337"
k6 = 2
print(solution.removeKdigits(num6, k6))
# Output: "33"
