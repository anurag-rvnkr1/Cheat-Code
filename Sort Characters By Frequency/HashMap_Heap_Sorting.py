'''
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of characters.

Return any valid answer where characters with higher frequency appear first.

Example 1:
    Input:
        s = "tree"

    Output:
        "eert"

Example 2:
    Input:
        s = "cccaaa"

    Output:
        "aaaccc"

Example 3:
    Input:
        s = "Aabb"

    Output:
        "bbAa"

Constraints:
    1 <= s.length <= 5 * 10^5
    s consists of uppercase and lowercase English letters and digits.
'''

# HashMap + Bucket Sort

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)

        buckets = [[] for _ in range(len(s) + 1)]

        for character, count in frequency.items():
            buckets[count].append(character)

        result = []

        for count in range(len(s), 0, -1):
            for character in buckets[count]:
                result.append(character * count)

        return "".join(result)


# Example usage
solution = Solution()

# Example 1
s1 = "tree"
print(solution.frequencySort(s1))
# Output: "eert"

# Example 2
s2 = "cccaaa"
print(solution.frequencySort(s2))
# Output: "cccaaa" or "aaaccc"

# Example 3
s3 = "Aabb"
print(solution.frequencySort(s3))
# Output: "bbAa"

# Example 4
s4 = "leetcode"
print(solution.frequencySort(s4))
# Output: "eeelotcd" (or any valid frequency-sorted string)

# Example 5
s5 = "1112233"
print(solution.frequencySort(s5))
# Output: "1112233"

# Example 6
s6 = "Programming123"
print(solution.frequencySort(s6))
# Output: Characters sorted by decreasing frequency.
