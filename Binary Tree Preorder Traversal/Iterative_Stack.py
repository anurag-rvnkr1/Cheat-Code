'''
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Preorder Traversal Order:
    Root -> Left -> Right

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''

# Iterative Stack

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push right first so left is processed first.
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print(solution.preorderTraversal(root1))  # Output: [1, 2, 3]

# Example 2
root2 = None

print(solution.preorderTraversal(root2))  # Output: []

# Example 3
root3 = TreeNode(1)

print(solution.preorderTraversal(root3))  # Output: [1]
