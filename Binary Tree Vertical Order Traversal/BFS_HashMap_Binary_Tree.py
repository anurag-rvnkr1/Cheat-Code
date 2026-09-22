'''
314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return its vertical order traversal.

For each node:
    - Root has column = 0.
    - Left child has column - 1.
    - Right child has column + 1.

Nodes in the same row and column should appear in left-to-right order
(BFS traversal order).

Return the vertical order from the leftmost column to the rightmost column.

Example 1:
    Input:
        root = [3,9,20,null,null,15,7]

    Output:
        [[9],[3,15],[20],[7]]

Example 2:
    Input:
        root = [3,9,8,4,0,1,7]

    Output:
        [[4],[9],[3,0,1],[8],[7]]

Example 3:
    Input:
        root = [1,2,3,4,5,6,7]

    Output:
        [[4],[2],[1,5,6],[3],[7]]

Constraints:
    The number of nodes is in the range [0, 100].
    -100 <= Node.val <= 100
'''

# BFS + HashMap + Binary Tree

from typing import Optional, List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        queue = deque([(root, 0)])

        min_column = 0
        max_column = 0

        while queue:
            node, column = queue.popleft()

            column_table[column].append(node.val)

            min_column = min(min_column, column)
            max_column = max(max_column, column)

            if node.left:
                queue.append((node.left, column - 1))

            if node.right:
                queue.append((node.right, column + 1))

        result = []

        for column in range(min_column, max_column + 1):
            result.append(column_table[column])

        return result


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(solution.verticalOrder(root1))
# Output: [[9], [3, 15], [20], [7]]

# Example 2
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(8)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(0)
root2.right.left = TreeNode(1)
root2.right.right = TreeNode(7)

print(solution.verticalOrder(root2))
# Output: [[4], [9], [3, 0, 1], [8], [7]]

# Example 3
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(7)

print(solution.verticalOrder(root3))
# Output: [[4], [2], [1, 5, 6], [3], [7]]

# Example 4
root4 = TreeNode(1)

print(solution.verticalOrder(root4))
# Output: [[1]]
