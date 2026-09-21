'''
208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings.

Implement the Trie class:

    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns True if the string word is in the trie.
    - boolean startsWith(String prefix) Returns True if there is a previously
      inserted string word that has the prefix prefix.

Example 1:
    Input:
        ["Trie","insert","search","search","startsWith","insert","search"]
        [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

    Output:
        [null,null,true,false,true,null,true]

Explanation:
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");      // True
    trie.search("app");        // False
    trie.startsWith("app");    // True
    trie.insert("app");
    trie.search("app");        // True

Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 10^4 calls will be made to insert, search, and startsWith.
'''

# Trie (Prefix Tree)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


# Example usage
trie = Trie()

# Example 1
trie.insert("apple")

print(trie.search("apple"))       # Output: True
print(trie.search("app"))         # Output: False
print(trie.startsWith("app"))     # Output: True

trie.insert("app")
print(trie.search("app"))         # Output: True

# Example 2
trie.insert("banana")

print(trie.search("banana"))      # Output: True
print(trie.startsWith("ban"))     # Output: True
print(trie.startsWith("bat"))     # Output: False

# Example 3
print(trie.search("applepie"))    # Output: False
