'''
249. Group Shifted Strings

We can shift a string by shifting each of its letters to its successive letter.

For example:
    "abc" -> "bcd" -> ... -> "xyz"

Given an array of strings strings, group all shifted strings together.

Two strings belong to the same shifting sequence if one can be shifted some
number of times to become the other.

Return the groups in any order.

Example 1:
    Input:
        strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

    Output:
        [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
    Input:
        strings = ["a"]
    Output:
        [["a"]]

Constraints:
    1 <= strings.length <= 200
    1 <= strings[i].length <= 50
    strings[i] consists of lowercase English letters.
'''

# HashMap + String Normalization

from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        # Generate a unique pattern for each shifting sequence.
        def getPattern(word: str):
            if len(word) == 1:
                return ()

            pattern = []

            for i in range(1, len(word)):
                difference = (ord(word[i]) - ord(word[i - 1])) % 26
                pattern.append(difference)

            return tuple(pattern)

        for word in strings:
            groups[getPattern(word)].append(word)

        return list(groups.values())


# Example usage
solution = Solution()

# Example 1
strings1 = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(solution.groupStrings(strings1))
# Output (order may vary):
# [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]

# Example 2
strings2 = ["a"]
print(solution.groupStrings(strings2))
# Output: [['a']]

# Example 3
strings3 = ["ab", "bc", "cd", "yz", "za"]
print(solution.groupStrings(strings3))
# Output (order may vary):
# [['ab', 'bc', 'cd', 'yz', 'za']]

# Example 4
strings4 = ["aa", "bb", "cc", "az", "ba"]
print(solution.groupStrings(strings4))
# Output (order may vary):
# [['aa', 'bb', 'cc'], ['az', 'ba']]
