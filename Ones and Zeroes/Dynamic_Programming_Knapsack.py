'''
474. Ones and Zeroes

You are given an array of binary strings strs and two integers m and n.

    m -> maximum number of zeros available.
    n -> maximum number of ones available.

Return the maximum number of strings you can form using at most m zeros
and n ones.

Each 0 and 1 can be used only once.

Example 1:
    Input:
        strs = ["10","0001","111001","1","0"]
        m = 5
        n = 3

    Output:
        4

Explanation:
        One optimal subset is ["10","0001","1","0"].

Example 2:
    Input:
        strs = ["10","0","1"]
        m = 1
        n = 1

    Output:
        2

Constraints:
    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] consists only of '0' and '1'.
    1 <= m, n <= 100
'''

# Dynamic Programming + 0/1 Knapsack

from typing import List


class Solution:
    def findMaxForm(
        self,
        strs: List[str],
        m: int,
        n: int
    ) -> int:

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for binary_string in strs:
            zeros = binary_string.count("0")
            ones = binary_string.count("1")

            # Traverse backwards for 0/1 Knapsack.
            for zero_count in range(m, zeros - 1, -1):
                for one_count in range(n, ones - 1, -1):
                    dp[zero_count][one_count] = max(
                        dp[zero_count][one_count],
                        dp[zero_count - zeros][one_count - ones] + 1
                    )

        return dp[m][n]


# Example usage
solution = Solution()

# Example 1
strs1 = ["10","0001","111001","1","0"]
print(solution.findMaxForm(strs1, 5, 3))
# Output: 4

# Example 2
strs2 = ["10","0","1"]
print(solution.findMaxForm(strs2, 1, 1))
# Output: 2

# Example 3
strs3 = ["10","000","111","01","001"]
print(solution.findMaxForm(strs3, 4, 4))
# Output: 3

# Example 4
strs4 = ["0","0","1","1"]
print(solution.findMaxForm(strs4, 2, 2))
# Output: 4

# Example 5
strs5 = ["10","10","10","10"]
print(solution.findMaxForm(strs5, 2, 2))
# Output: 2

# Example 6
strs6 = ["111","1000","1000","1000"]
print(solution.findMaxForm(strs6, 9, 3))
# Output: 3
