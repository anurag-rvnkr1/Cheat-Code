"""
522. Longest Uncommon Subsequence II

Given an array of strings strs, return the length of the longest
uncommon subsequence among them.

A subsequence is a sequence that can be derived from a string by
deleting some or no characters without changing the order of the
remaining characters.

An uncommon subsequence is a subsequence that is not a subsequence of
any other string in the array.

If there is no uncommon subsequence, return -1.

Examples:
1. Input: strs = ["aba", "cdc", "eae"]
   Output: 3

2. Input: strs = ["aaa", "aaa", "aa"]
   Output: -1

3. Input: strs = ["aabbcc", "aabbcc", "cb"]
   Output: 2

4. Input: strs = ["abc", "abc", "abcd"]
   Output: 4

5. Input: strs = ["a", "b", "c"]
   Output: 1

6. Input: strs = ["abcdef", "abc", "abcd"]
   Output: 6
"""


class Solution:
    def findLUSlength(self, strs: list[str]) -> int:

        def is_subsequence(s: str, t: str) -> bool:
            i = 0

            for char in t:
                if i < len(s) and s[i] == char:
                    i += 1

            return i == len(s)

        answer = -1

        for i in range(len(strs)):
            uncommon = True

            for j in range(len(strs)):
                if i == j:
                    continue

                if is_subsequence(strs[i], strs[j]):
                    uncommon = False
                    break

            if uncommon:
                answer = max(answer, len(strs[i]))

        return answer


# Example 1
strs = ["aba", "cdc", "eae"]
print(Solution().findLUSlength(strs))  # 3

# Example 2
strs = ["aaa", "aaa", "aa"]
print(Solution().findLUSlength(strs))  # -1

# Example 3
strs = ["aabbcc", "aabbcc", "cb"]
print(Solution().findLUSlength(strs))  # 2

# Example 4
strs = ["abc", "abc", "abcd"]
print(Solution().findLUSlength(strs))  # 4

# Example 5
strs = ["a", "b", "c"]
print(Solution().findLUSlength(strs))  # 1

# Example 6
strs = ["abcdef", "abc", "abcd"]
print(Solution().findLUSlength(strs))  # 6


# Time Complexity: O(n² × L)
# Space Complexity: O(1)
