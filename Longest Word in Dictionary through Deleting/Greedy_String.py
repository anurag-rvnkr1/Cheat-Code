"""
524. Longest Word in Dictionary through Deleting

Given a string s and a string array dictionary, return the longest
string in dictionary that can be formed by deleting some characters
of s.

If there are multiple possible results, return the longest word with
the smallest lexicographical order.

If no possible result exists, return an empty string.

Examples:
1. Input: s = "abpcplea", dictionary = ["ale", "apple", "monkey", "plea"]
   Output: "apple"

2. Input: s = "abpcplea", dictionary = ["a", "b", "c"]
   Output: "a"

3. Input: s = "bab", dictionary = ["ba", "ab", "a", "b"]
   Output: "ab"

4. Input: s = "abce", dictionary = ["abe", "abc"]
   Output: "abc"

5. Input: s = "abc", dictionary = ["xyz", "pqr"]
   Output: ""

6. Input: s = "aaaa", dictionary = ["a", "aa", "aaa", "aaaa"]
   Output: "aaaa"
"""


class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:

        def is_subsequence(word: str) -> bool:
            i = 0

            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1

            return i == len(word)

        answer = ""

        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(answer):
                    answer = word
                elif len(word) == len(answer) and word < answer:
                    answer = word

        return answer


# Example 1
s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
print(Solution().findLongestWord(s, dictionary))  # "apple"

# Example 2
s = "abpcplea"
dictionary = ["a", "b", "c"]
print(Solution().findLongestWord(s, dictionary))  # "a"

# Example 3
s = "bab"
dictionary = ["ba", "ab", "a", "b"]
print(Solution().findLongestWord(s, dictionary))  # "ab"

# Example 4
s = "abce"
dictionary = ["abe", "abc"]
print(Solution().findLongestWord(s, dictionary))  # "abc"

# Example 5
s = "abc"
dictionary = ["xyz", "pqr"]
print(Solution().findLongestWord(s, dictionary))  # ""

# Example 6
s = "aaaa"
dictionary = ["a", "aa", "aaa", "aaaa"]
print(Solution().findLongestWord(s, dictionary))  # "aaaa"


# Time Complexity: O(n × m)
# Space Complexity: O(1)
