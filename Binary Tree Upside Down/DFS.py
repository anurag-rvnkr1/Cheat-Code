'''
156. Binary Tree Upside Down

Given the root of a binary tree where every right child is either a leaf node
or None, flip it upside down and return the new root.

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

Example 1:
    Input: root = [1,2,3,4,5]
    Output: [4,5,2,null,null,3,1]

Explanation:
        1               4
       / \             / \
      2   3    -->    5   2
     / \                 / \
    4   5               3   1

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 10].
    1 <= Node.val <= 10
    Every right node has a sibling and no children.
'''

# Depth-First Search (Recursive)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root

        root.left = None
        root.right = None

        return new_root


# Helper function for preorder traversal
def preorder(root):
    if not root:
        return []

    return [root.val] + preorder(root.left) + preorder(root.right)


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

new_root1 = solution.upsideDownBinaryTree(root1)
print(preorder(new_root1))  # Output: [4, 5, 2, 3, 1]

# Example 2
root2 = None
new_root2 = solution.upsideDownBinaryTree(root2)
print(preorder(new_root2))  # Output: []

# Example 3
root3 = TreeNode(1)
new_root3 = solution.upsideDownBinaryTree(root3)
print(preorder(new_root3))  # Output: [1]
