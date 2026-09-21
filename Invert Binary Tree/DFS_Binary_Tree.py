'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree and return its root.

Invert a binary tree by swapping every node's left and right children.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''

# Depth-First Search (Recursive)

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap left and right children.
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees.
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Helper function: Level Order Traversal
def printTree(root):
    if not root:
        print([])
        return

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values.
    while result and result[-1] is None:
        result.pop()

    print(result)


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)

inverted1 = solution.invertTree(root1)
printTree(inverted1)
# Output: [4, 7, 2, 9, 6, 3, 1]

# Example 2
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

inverted2 = solution.invertTree(root2)
printTree(inverted2)
# Output: [2, 3, 1]

# Example 3
root3 = None

inverted3 = solution.invertTree(root3)
printTree(inverted3)
# Output: []

# Example 4
root4 = TreeNode(1)

inverted4 = solution.invertTree(root4)
printTree(inverted4)
# Output: [1]
