'''
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:

    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure.
    - bool search(word) Returns True if there is any string in the data structure
      that matches word or False otherwise.

The search word may contain dots '.' where dots can be matched with any letter.

Example 1:
    Input:
        ["WordDictionary","addWord","addWord","addWord",
         "search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

    Output:
        [null,null,null,null,false,true,true,true]

Explanation:
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // False
    wordDictionary.search("bad"); // True
    wordDictionary.search(".ad"); // True
    wordDictionary.search("b.."); // True

Constraints:
    1 <= word.length <= 25
    word consists of lowercase English letters or '.'.
    There will be at most 2 dots in word for search queries.
    At most 10^4 calls will be made to addWord and search.
'''

# Trie + DFS


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(index: int, node: TrieNode) -> bool:
            current = node

            for i in range(index, len(word)):
                char = word[i]

                if char == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                if char not in current.children:
                    return False

                current = current.children[char]

            return current.isEnd

        return dfs(0, self.root)


# Example usage
wordDictionary = WordDictionary()

# Example 1
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

print(wordDictionary.search("pad"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search(".ad"))  # Output: True
print(wordDictionary.search("b.."))  # Output: True

# Example 2
wordDictionary.addWord("apple")

print(wordDictionary.search("apple"))  # Output: True
print(wordDictionary.search("app.e"))  # Output: True
print(wordDictionary.search("appl."))  # Output: True
print(wordDictionary.search("....."))  # Output: True
print(wordDictionary.search("a...."))  # Output: True

# Example 3
print(wordDictionary.search("cat"))  # Output: False
