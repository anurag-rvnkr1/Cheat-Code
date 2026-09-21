'''
222. Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes
in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled
in a complete binary tree, and all nodes in the last level are as far left as possible.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: 6

Example 2:
    Input: root = []
    Output: 0

Example 3:
    Input: root = [1]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [0, 5 * 10^4].
    0 <= Node.val <= 5 * 10^4
    The tree is guaranteed to be complete.
'''

# Binary Tree + Binary Search

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def leftHeight(node):
            height = 0

            while node:
                height += 1
                node = node.left

            return height

        def rightHeight(node):
            height = 0

            while node:
                height += 1
                node = node.right

            return height

        if not root:
            return 0

        left_height = leftHeight(root)
        right_height = rightHeight(root)

        # Perfect binary tree.
        if left_height == right_height:
            return (1 << left_height) - 1

        return (
            1 +
            self.countNodes(root.left) +
            self.countNodes(root.right)
        )


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)

print(solution.countNodes(root1))  # Output: 6

# Example 2
root2 = None

print(solution.countNodes(root2))  # Output: 0

# Example 3
root3 = TreeNode(1)

print(solution.countNodes(root3))  # Output: 1

# Example 4
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.left.left = TreeNode(4)
root4.left.right = TreeNode(5)
root4.right.left = TreeNode(6)
root4.right.right = TreeNode(7)

print(solution.countNodes(root4))  # Output: 7
