'''
468. Validate IP Address

Given a string queryIP, return:

    "IPv4" -> valid IPv4 address
    "IPv6" -> valid IPv6 address
    "Neither" -> invalid IP address

IPv4 Rules:
    - Four decimal numbers separated by '.'
    - Each number is between 0 and 255.
    - No leading zeros unless the number is exactly "0".

IPv6 Rules:
    - Eight hexadecimal groups separated by ':'.
    - Each group has 1 to 4 hexadecimal characters.
    - Characters may be digits or letters a-f / A-F.

Example 1:
    Input:
        queryIP = "172.16.254.1"

    Output:
        "IPv4"

Example 2:
    Input:
        queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"

    Output:
        "IPv6"

Example 3:
    Input:
        queryIP = "256.256.256.256"

    Output:
        "Neither"

Constraints:
    queryIP consists only of English letters, digits, '.' and ':'.
'''

# String Parsing

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count(".") == 3:
            return self.validate_ipv4(queryIP)

        if queryIP.count(":") == 7:
            return self.validate_ipv6(queryIP)

        return "Neither"

    def validate_ipv4(self, address: str) -> str:
        parts = address.split(".")

        if len(parts) != 4:
            return "Neither"

        for part in parts:
            if len(part) == 0:
                return "Neither"

            if not part.isdigit():
                return "Neither"

            if len(part) > 1 and part[0] == "0":
                return "Neither"

            number = int(part)

            if number < 0 or number > 255:
                return "Neither"

        return "IPv4"

    def validate_ipv6(self, address: str) -> str:
        parts = address.split(":")

        if len(parts) != 8:
            return "Neither"

        hexadecimal = "0123456789abcdefABCDEF"

        for part in parts:
            if len(part) == 0 or len(part) > 4:
                return "Neither"

            for character in part:
                if character not in hexadecimal:
                    return "Neither"

        return "IPv6"


# Example usage
solution = Solution()

# Example 1
ip1 = "172.16.254.1"
print(solution.validIPAddress(ip1))
# Output: IPv4

# Example 2
ip2 = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(solution.validIPAddress(ip2))
# Output: IPv6

# Example 3
ip3 = "256.256.256.256"
print(solution.validIPAddress(ip3))
# Output: Neither

# Example 4
ip4 = "192.168.01.1"
print(solution.validIPAddress(ip4))
# Output: Neither

# Example 5
ip5 = "2001:db8:85a3::8A2E:0370:7334"
print(solution.validIPAddress(ip5))
# Output: Neither

# Example 6
ip6 = "255.255.255.255"
print(solution.validIPAddress(ip6))
# Output: IPv4
