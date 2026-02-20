'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
'''
#Compare With First String
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
#Example Usage
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
