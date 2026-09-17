'''
93. Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example:
- "0.1.2.201" and "192.168.1.1" are valid IP addresses.
- "0.011.255.245", "192.168.1.312", and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s.

You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
    Input: s = "25525511135"
    Output: ["255.255.11.135","255.255.111.35"]

Example 2:
    Input: s = "0000"
    Output: ["0.0.0.0"]

Example 3:
    Input: s = "101023"
    Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
    1 <= s.length <= 20
    s consists of digits only.
'''

# Backtracking
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = []

        def backtrack(start, parts):

            # Four parts formed
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            # Try segments of length 1 to 3
            for end in range(start, min(start + 3, len(s))):
                part = s[start:end + 1]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == '0':
                    break

                # Value must be between 0 and 255
                if int(part) > 255:
                    break

                backtrack(end + 1, parts + [part])

        backtrack(0, [])

        return result


# Example usage
solution = Solution()

print(solution.restoreIpAddresses("25525511135"))
# Output: ['255.255.11.135', '255.255.111.35']

print(solution.restoreIpAddresses("0000"))
# Output: ['0.0.0.0']

print(solution.restoreIpAddresses("101023"))
# Output: ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']
