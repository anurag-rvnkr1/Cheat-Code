'''
288. Unique Word Abbreviation

The abbreviation of a word is formed by:

    - First character.
    - Number of characters between first and last character.
    - Last character.

Examples:
    "dog"      -> "d1g"
    "internationalization" -> "i18n"
    "it"       -> "it" (length <= 2)

Implement the ValidWordAbbr class:

    - ValidWordAbbr(dictionary) Initializes the object with a dictionary of words.
    - isUnique(word) Returns True if the abbreviation of word is unique in the
      dictionary.

A word's abbreviation is unique if:
    - No other word in the dictionary has the same abbreviation.
    - Or the only word with that abbreviation is the word itself.

Example 1:
    Input:
        dictionary = ["deer","door","cake","card"]

        isUnique("dear")
        isUnique("cart")
        isUnique("cane")
        isUnique("make")

    Output:
        False
        True
        False
        True

Constraints:
    1 <= dictionary.length <= 3 * 10^4
    1 <= dictionary[i].length <= 20
    dictionary[i] consists of lowercase English letters.
    word consists of lowercase English letters.
'''

# HashMap + Design

from typing import List
from collections import defaultdict


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        # abbreviation -> set(words)
        self.abbreviations = defaultdict(set)

        for word in dictionary:
            self.abbreviations[self._abbreviate(word)].add(word)

    def _abbreviate(self, word: str) -> str:
        if len(word) <= 2:
            return word

        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbreviation = self._abbreviate(word)

        if abbreviation not in self.abbreviations:
            return True

        words = self.abbreviations[abbreviation]

        return len(words) == 1 and word in words


# Example usage

dictionary = ["deer", "door", "cake", "card"]
abbr = ValidWordAbbr(dictionary)

# Example 1
print(abbr.isUnique("dear"))
# Output: False

# Example 2
print(abbr.isUnique("cart"))
# Output: True

# Example 3
print(abbr.isUnique("cane"))
# Output: False

# Example 4
print(abbr.isUnique("make"))
# Output: True

# Example 5
dictionary2 = ["hello", "world"]
abbr2 = ValidWordAbbr(dictionary2)

print(abbr2.isUnique("hello"))
# Output: True

print(abbr2.isUnique("house"))
# Output: True

# Example 6
dictionary3 = ["it", "is", "in"]
abbr3 = ValidWordAbbr(dictionary3)

print(abbr3.isUnique("it"))
# Output: True

print(abbr3.isUnique("is"))
# Output: True
