'''
323. Number of Connected Components in an Undirected Graph

You are given an undirected graph with n nodes labeled from 0 to n - 1
and a list of edges.

Return the number of connected components in the graph.

Example 1:
    Input:
        n = 5
        edges = [[0,1],[1,2],[3,4]]

    Output:
        2

Explanation:
        Component 1: 0 - 1 - 2
        Component 2: 3 - 4

Example 2:
    Input:
        n = 5
        edges = [[0,1],[1,2],[2,3],[3,4]]

    Output:
        1

Constraints:
    1 <= n <= 2000
    1 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    There are no repeated edges.
'''

# Union Find (Disjoint Set Union)

from typing import List


class UnionFind:

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, node1: int, node2: int) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return

        # Union by Rank
        if self.rank[root1] < self.rank[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1

        if self.rank[root1] == self.rank[root2]:
            self.rank[root1] += 1

        self.components -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)

        for node1, node2 in edges:
            union_find.union(node1, node2)

        return union_find.components


# Example usage
solution = Solution()

# Example 1
n1 = 5
edges1 = [
    [0,1],
    [1,2],
    [3,4]
]

print(solution.countComponents(n1, edges1))
# Output: 2

# Example 2
n2 = 5
edges2 = [
    [0,1],
    [1,2],
    [2,3],
    [3,4]
]

print(solution.countComponents(n2, edges2))
# Output: 1

# Example 3
n3 = 6
edges3 = [
    [0,1],
    [2,3],
    [4,5]
]

print(solution.countComponents(n3, edges3))
# Output: 3

# Example 4
n4 = 4
edges4 = []

print(solution.countComponents(n4, edges4))
# Output: 4

# Example 5
n5 = 7
edges5 = [
    [0,1],
    [1,2],
    [2,0],
    [3,4],
    [5,6]
]

print(solution.countComponents(n5, edges5))
# Output: 3
