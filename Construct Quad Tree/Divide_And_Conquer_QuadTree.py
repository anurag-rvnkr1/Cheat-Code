'''
427. Construct Quad Tree

Given an n x n binary matrix grid, return the root of the Quad Tree representing it.

A Quad Tree node contains:
    - val: True if the region contains 1s, otherwise False.
    - isLeaf: True if the node is a leaf.
    - topLeft
    - topRight
    - bottomLeft
    - bottomRight

A leaf node represents a region where all values are the same.

Example 1:
    Input:
        grid = [
            [0,1],
            [1,0]
        ]

    Output:
        Quad Tree representation.

Example 2:
    Input:
        grid = [
            [1,1],
            [1,1]
        ]

    Output:
        Single leaf node with val = True.

Constraints:
    n == grid.length == grid[i].length
    n == 2^x where 0 <= x <= 6
    1 <= n <= 64
    grid[i][j] is either 0 or 1.
'''

# Divide and Conquer (Quad Tree)

from typing import List, Optional


class Node:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Optional["Node"] = None,
        topRight: Optional["Node"] = None,
        bottomLeft: Optional["Node"] = None,
        bottomRight: Optional["Node"] = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def build(row: int, col: int, size: int) -> Node:
            value = grid[row][col]
            is_uniform = True

            # Check if the current region has the same value.
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != value:
                        is_uniform = False
                        break
                if not is_uniform:
                    break

            if is_uniform:
                return Node(bool(value), True)

            half = size // 2

            return Node(
                True,
                False,
                build(row, col, half),
                build(row, col + half, half),
                build(row + half, col, half),
                build(row + half, col + half, half),
            )

        return build(0, 0, len(grid))


# -----------------------------
# Helper Function for Testing
# -----------------------------

def preorder(node: Optional[Node]):
    if not node:
        return None

    if node.isLeaf:
        return [1 if node.val else 0]

    return [
        "Node",
        preorder(node.topLeft),
        preorder(node.topRight),
        preorder(node.bottomLeft),
        preorder(node.bottomRight),
    ]


# Example usage
solution = Solution()

# Example 1
grid1 = [
    [0,1],
    [1,0]
]
root1 = solution.construct(grid1)
print(preorder(root1))
# Output: Quad Tree preorder representation.

# Example 2
grid2 = [
    [1,1],
    [1,1]
]
root2 = solution.construct(grid2)
print(preorder(root2))
# Output: [1]

# Example 3
grid3 = [
    [0,0],
    [0,0]
]
root3 = solution.construct(grid3)
print(preorder(root3))
# Output: [0]

# Example 4
grid4 = [
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,0,1,1]
]
root4 = solution.construct(grid4)
print(preorder(root4))
# Output: Internal node with four leaf children.

# Example 5
grid5 = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]
root5 = solution.construct(grid5)
print(preorder(root5))
# Output: [1]

# Example 6
grid6 = [
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1]
]
root6 = solution.construct(grid6)
print(preorder(root6))
# Output: Deep Quad Tree representation.
