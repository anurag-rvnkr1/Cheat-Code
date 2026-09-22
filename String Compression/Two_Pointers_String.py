'''
443. String Compression

Given an array of characters chars, compress it in-place.

Compression Rules:
    - Consecutive repeating characters are replaced with the character
      followed by the count (if count > 1).
    - The compressed string must be written back into chars.
    - Return the new length after compression.

The algorithm must use only constant extra space.

Example 1:
    Input:
        chars = ["a","a","b","b","c","c","c"]

    Output:
        6

Explanation:
        chars becomes ["a","2","b","2","c","3"]

Example 2:
    Input:
        chars = ["a"]

    Output:
        1

Example 3:
    Input:
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    Output:
        4

Explanation:
        chars becomes ["a","b","1","2"]

Constraints:
    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter,
    digit, or symbol.
'''

# Two Pointers + String Compression

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            current_character = chars[read]
            count = 0

            while (
                read < len(chars) and
                chars[read] == current_character
            ):
                read += 1
                count += 1

            chars[write] = current_character
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


# Example usage
solution = Solution()

# Example 1
chars1 = ["a","a","b","b","c","c","c"]
length1 = solution.compress(chars1)
print(length1)
print(chars1[:length1])
# Output:
# 6
# ['a','2','b','2','c','3']

# Example 2
chars2 = ["a"]
length2 = solution.compress(chars2)
print(length2)
print(chars2[:length2])
# Output:
# 1
# ['a']

# Example 3
chars3 = [
    "a","b","b","b","b","b",
    "b","b","b","b","b","b","b"
]
length3 = solution.compress(chars3)
print(length3)
print(chars3[:length3])
# Output:
# 4
# ['a','b','1','2']

# Example 4
chars4 = ["a","a","a","a"]
length4 = solution.compress(chars4)
print(length4)
print(chars4[:length4])
# Output:
# 2
# ['a','4']

# Example 5
chars5 = ["a","b","c"]
length5 = solution.compress(chars5)
print(length5)
print(chars5[:length5])
# Output:
# 3
# ['a','b','c']

# Example 6
chars6 = ["z"] * 15
length6 = solution.compress(chars6)
print(length6)
print(chars6[:length6])
# Output:
# 3
# ['z','1','5']
