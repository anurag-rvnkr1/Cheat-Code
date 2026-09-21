'''
269. Alien Dictionary

There is a new alien language that uses the English lowercase alphabet,
but the order of the letters is unknown.

You are given a list of strings words from the alien dictionary, where
the strings are sorted lexicographically according to the rules of the
alien language.

Return a string containing the unique letters in the correct order.
If there are multiple valid orders, return any of them.
If the dictionary is invalid, return an empty string.

Example 1:
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

Example 2:
    Input: words = ["z","x"]
    Output: "zx"

Example 3:
    Input: words = ["z","x","z"]
    Output: ""

Explanation:
    The ordering creates a cycle (z -> x -> z).

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
'''

# Graph + Topological Sort (Kahn's Algorithm)

from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Create graph with every unique character.
        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}

        # Build graph from adjacent words.
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Invalid case: longer prefix before shorter word.
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # Topological Sort (BFS)
        queue = deque([char for char in indegree if indegree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detected.
        if len(order) != len(indegree):
            return ""

        return "".join(order)


# Example usage
solution = Solution()

# Example 1
words1 = ["wrt", "wrf", "er", "ett", "rftt"]
print(solution.alienOrder(words1))
# Output: "wertf"

# Example 2
words2 = ["z", "x"]
print(solution.alienOrder(words2))
# Output: "zx"

# Example 3
words3 = ["z", "x", "z"]
print(solution.alienOrder(words3))
# Output: ""

# Example 4
words4 = ["abc", "ab"]
print(solution.alienOrder(words4))
# Output: ""

# Example 5
words5 = ["baa", "abcd", "abca", "cab", "cad"]
print(solution.alienOrder(words5))
# Output: One valid order such as "bdac"
