'''
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side
of it, and return the values of the nodes you can see ordered from top to bottom.

Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

Example 2:
    Input: root = [1,null,3]
    Output: [1,3]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''

# Breadth-First Search (Level Order Traversal)

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Last node in the current level is visible from the right.
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)

print(solution.rightSideView(root1))  # Output: [1, 3, 4]

# Example 2
root2 = TreeNode(1)
root2.right = TreeNode(3)

print(solution.rightSideView(root2))  # Output: [1, 3]

# Example 3
root3 = None

print(solution.rightSideView(root3))  # Output: []

# Example 4
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.left.left = TreeNode(3)

print(solution.rightSideView(root4))  # Output: [1, 2, 3]
