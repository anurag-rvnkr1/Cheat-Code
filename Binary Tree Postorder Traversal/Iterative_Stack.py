'''
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Postorder Traversal Order:
    Left -> Right -> Root

Example 1:
    Input: root = [1,null,2,3]
    Output: [3,2,1]

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first so right is processed first.
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        # Reverse Root-Right-Left to get Left-Right-Root.
        return result[::-1]


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print(solution.postorderTraversal(root1))  # Output: [3, 2, 1]

# Example 2
root2 = None

print(solution.postorderTraversal(root2))  # Output: []

# Example 3
root3 = TreeNode(1)

print(solution.postorderTraversal(root3))  # Output: [1]
