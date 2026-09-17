'''
91. Decode Ways

You have intercepted a secret message encoded as a string of numbers.

The message is decoded using the following mapping:

    "1"  -> 'A'
    "2"  -> 'B'
    ...
    "25" -> 'Y'
    "26" -> 'Z'

A message can have multiple valid decodings because some codes are contained within other codes.

Return the number of ways to decode the string. If the entire string cannot be decoded in any valid way, return 0.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation:
    "12" can be decoded as:
    - "AB" (1,2)
    - "L" (12)

Example 2:
    Input: s = "226"
    Output: 3
    Explanation:
    "226" can be decoded as:
    - "BZ" (2,26)
    - "VF" (22,6)
    - "BBF" (2,2,6)

Example 3:
    Input: s = "06"
    Output: 0
    Explanation:
    "06" is not a valid encoding because leading zeros are not allowed.

Constraints:
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).
'''

# Dynamic Programming (Space Optimized)
class Solution:
    def numDecodings(self, s: str) -> int:

        prev2, prev1 = 1, 1

        for i in range(1, len(s) + 1):
            curr = 0

            # One digit: 1-9
            if s[i - 1] != '0':
                curr += prev1

            # Two digits: 10-26
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1


# Example usage
solution = Solution()

print(solution.numDecodings("12"))     # Output: 2
print(solution.numDecodings("226"))    # Output: 3
print(solution.numDecodings("06"))     # Output: 0
print(solution.numDecodings("11106"))  # Output: 2
