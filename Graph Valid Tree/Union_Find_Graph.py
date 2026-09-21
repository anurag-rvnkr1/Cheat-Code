'''
261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges,
write a function to check whether these edges make up a valid tree.

A valid tree is an undirected graph that is:
    - Fully connected.
    - Contains no cycles.

Example 1:
    Input:
        n = 5
        edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: True

Explanation:
    The graph is connected and contains no cycle.

Example 2:
    Input:
        n = 5
        edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: False

Explanation:
    There is a cycle between nodes 1, 2, and 3.

Constraints:
    1 <= n <= 2000
    0 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no duplicate edges.
'''

# Union Find (Disjoint Set Union)

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges.
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            # Cycle detected.
            if root1 == root2:
                return False

            # Union by rank.
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True


# Example usage
solution = Solution()

# Example 1
n1 = 5
edges1 = [[0,1],[0,2],[0,3],[1,4]]
print(solution.validTree(n1, edges1))
# Output: True

# Example 2
n2 = 5
edges2 = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print(solution.validTree(n2, edges2))
# Output: False

# Example 3
n3 = 4
edges3 = [[0,1],[2,3]]
print(solution.validTree(n3, edges3))
# Output: False

# Example 4
n4 = 1
edges4 = []
print(solution.validTree(n4, edges4))
# Output: True
