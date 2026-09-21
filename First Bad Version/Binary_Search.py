'''
278. First Bad Version

You are a product manager and currently leading a team to develop a new product.

Unfortunately, the latest version of your product fails the quality check.

Since each version is developed based on the previous version, all versions after
a bad version are also bad.

You are given an API:

    isBadVersion(version)

Return the first bad version.

You should minimize the number of calls to the API.

Example 1:
    Input:
        n = 5
        bad = 4

    Output:
        4

Explanation:
        Versions: [1,2,3,4,5]
        First bad version is 4.

Example 2:
    Input:
        n = 1
        bad = 1

    Output:
        1

Constraints:
    1 <= bad <= n <= 2^31 - 1
'''

# Binary Search

# ------------------------------------------------------------------
# LeetCode provides this API.
# This mock implementation is only for local testing.
# ------------------------------------------------------------------
BAD_VERSION = 1


def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


# Example usage
solution = Solution()

# Example 1
BAD_VERSION = 4
print(solution.firstBadVersion(5))
# Output: 4

# Example 2
BAD_VERSION = 1
print(solution.firstBadVersion(1))
# Output: 1

# Example 3
BAD_VERSION = 6
print(solution.firstBadVersion(10))
# Output: 6

# Example 4
BAD_VERSION = 9
print(solution.firstBadVersion(15))
# Output: 9

# Example 5
BAD_VERSION = 2
print(solution.firstBadVersion(2))
# Output: 2
