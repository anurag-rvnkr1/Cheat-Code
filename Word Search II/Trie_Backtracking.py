'''
212. Word Search II

Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example 1:
    Input:
        board = [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ]
        words = ["oath","pea","eat","rain"]

    Output:
        ["eat","oath"]

Example 2:
    Input:
        board = [["a","b"],["c","d"]]
        words = ["abcb"]

    Output:
        []

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 10^4
    1 <= words[i].length <= 10
    All strings of words are unique.
'''

# Trie + Backtracking

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build Trie
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r: int, c: int, node: TrieNode):
            char = board[r][c]

            if char not in node.children:
                return

            next_node = node.children[char]

            # Found a complete word.
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"
                ):
                    dfs(nr, nc, next_node)

            board[r][c] = char

            # Optimization: remove leaf Trie nodes.
            if not next_node.children:
                node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


# Example usage
solution = Solution()

# Example 1
board1 = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]

words1 = ["oath", "pea", "eat", "rain"]

print(sorted(solution.findWords(board1, words1)))
# Output: ['eat', 'oath']

# Example 2
board2 = [
    ["a", "b"],
    ["c", "d"]
]

words2 = ["abcb"]

print(solution.findWords(board2, words2))
# Output: []

# Example 3
board3 = [
    ["a", "b"],
    ["a", "a"]
]

words3 = ["aba", "baa", "bab", "aaab"]

print(sorted(solution.findWords(board3, words3)))
# Output: ['aba', 'baa']
