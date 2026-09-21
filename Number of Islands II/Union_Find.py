'''
305. Number of Islands II

You are given an empty m x n binary grid initialized with 0's (water).

You are also given an array positions where positions[i] = [ri, ci] is the
location where land is added.

Return an array answer where answer[i] is the number of islands after turning
the cell at positions[i] into land.

An island is formed by connecting adjacent lands horizontally or vertically.

Example 1:
    Input:
        m = 3
        n = 3
        positions = [[0,0],[0,1],[1,2],[2,1],[1,1]]

    Output:
        [1,1,2,3,1]

Explanation:
    Add (0,0) -> 1 island
    Add (0,1) -> Merge with previous island -> 1 island
    Add (1,2) -> New island -> 2 islands
    Add (2,1) -> New island -> 3 islands
    Add (1,1) -> Connects all three islands -> 1 island

Example 2:
    Input:
        m = 1
        n = 1
        positions = [[0,0]]

    Output:
        [1]

Constraints:
    1 <= m, n <= 10^4
    1 <= positions.length <= 10^4
    0 <= ri < m
    0 <= ci < n

Follow-up:
    Can you solve it in nearly O(k α(mn)) time?
'''

# Union Find (Disjoint Set Union)

from typing import List


class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, node: int):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1

        if self.rank[root1] == self.rank[root2]:
            self.rank[root1] += 1

        return True


class Solution:
    def numIslands2(
        self,
        m: int,
        n: int,
        positions: List[List[int]]
    ) -> List[int]:

        union_find = UnionFind()
        land = set()
        islands = 0
        answer = []

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for row, col in positions:

            # Ignore duplicate land additions.
            if (row, col) in land:
                answer.append(islands)
                continue

            land.add((row, col))

            node = row * n + col
            union_find.add(node)

            islands += 1

            # Merge neighboring lands.
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < m and
                    0 <= new_col < n and
                    (new_row, new_col) in land
                ):
                    neighbor = new_row * n + new_col

                    if union_find.union(node, neighbor):
                        islands -= 1

            answer.append(islands)

        return answer


# Example usage
solution = Solution()

# Example 1
m1 = 3
n1 = 3
positions1 = [
    [0, 0],
    [0, 1],
    [1, 2],
    [2, 1],
    [1, 1]
]

print(solution.numIslands2(m1, n1, positions1))
# Output: [1, 1, 2, 3, 1]

# Example 2
m2 = 1
n2 = 1
positions2 = [[0, 0]]

print(solution.numIslands2(m2, n2, positions2))
# Output: [1]

# Example 3
m3 = 2
n3 = 2
positions3 = [
    [0, 0],
    [1, 1],
    [0, 1],
    [1, 0]
]

print(solution.numIslands2(m3, n3, positions3))
# Output: [1, 2, 1, 1]

# Example 4 (Duplicate Position)
m4 = 2
n4 = 3
positions4 = [
    [0, 0],
    [0, 0],
    [0, 1]
]

print(solution.numIslands2(m4, n4, positions4))
# Output: [1, 1, 1]
