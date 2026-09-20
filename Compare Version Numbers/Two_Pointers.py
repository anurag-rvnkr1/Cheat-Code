'''
165. Compare Version Numbers

Given two version strings, version1 and version2, compare them.

Version strings consist of one or more revisions joined by a dot '.'.
Each revision consists of digits and may contain leading zeros.

Compare revision by revision from left to right:

    - Return 1 if version1 > version2.
    - Return -1 if version1 < version2.
    - Return 0 if both versions are equal.

Leading zeros should be ignored.

Example 1:
    Input: version1 = "1.2", version2 = "1.10"
    Output: -1

Example 2:
    Input: version1 = "1.01", version2 = "1.001"
    Output: 0

Example 3:
    Input: version1 = "1.0", version2 = "1.0.0.0"
    Output: 0

Constraints:
    1 <= version1.length, version2.length <= 500
    version1 and version2 contain only digits and '.'.
    Both version strings are valid.
'''

# Two Pointers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        n = max(len(v1), len(v2))

        for i in range(n):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

        return 0


# Example usage
solution = Solution()

# Example 1
version1 = "1.2"
version2 = "1.10"
print(solution.compareVersion(version1, version2))  # Output: -1

# Example 2
version1 = "1.01"
version2 = "1.001"
print(solution.compareVersion(version1, version2))  # Output: 0

# Example 3
version1 = "1.0"
version2 = "1.0.0.0"
print(solution.compareVersion(version1, version2))  # Output: 0

# Example 4
version1 = "2.0"
version2 = "1.9.9"
print(solution.compareVersion(version1, version2))  # Output: 1
