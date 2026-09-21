'''
310. Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly
one path.

You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates an undirected edge between ai and bi.

Return all roots of Minimum Height Trees (MHTs).

A Minimum Height Tree is a tree whose height is minimized when choosing its root.

Example 1:
    Input:
        n = 4
        edges = [[1,0],[1,2],[1,3]]

    Output:
        [1]

Explanation:
        Rooting the tree at node 1 gives minimum height.

Example 2:
    Input:
        n = 6
        edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

    Output:
        [3,4]

Constraints:
    1 <= n <= 2 * 10^4
    edges.length == n - 1
    0 <= ai, bi < n
    The input is guaranteed to be a tree.
'''

# Topological Sort + Graph (Leaf Trimming)

from typing import List
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[int]:

        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        # Build adjacency list and degree array.
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

            degree[u] += 1
            degree[v] += 1

        # Initialize queue with all leaves.
        leaves = deque()

        for node in range(n):
            if degree[node] == 1:
                leaves.append(node)

        remaining_nodes = n

        # Trim leaves layer by layer.
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)


# Example usage
solution = Solution()

# Example 1
n1 = 4
edges1 = [
    [1, 0],
    [1, 2],
    [1, 3]
]

print(solution.findMinHeightTrees(n1, edges1))
# Output: [1]

# Example 2
n2 = 6
edges2 = [
    [3, 0],
    [3, 1],
    [3, 2],
    [3, 4],
    [5, 4]
]

print(solution.findMinHeightTrees(n2, edges2))
# Output: [3, 4]

# Example 3
n3 = 1
edges3 = []

print(solution.findMinHeightTrees(n3, edges3))
# Output: [0]

# Example 4
n4 = 2
edges4 = [[0, 1]]

print(solution.findMinHeightTrees(n4, edges4))
# Output: [0, 1]

# Example 5
n5 = 7
edges5 = [
    [0, 1],
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 5],
    [4, 6]
]

print(solution.findMinHeightTrees(n5, edges5))
# Output: [2]
