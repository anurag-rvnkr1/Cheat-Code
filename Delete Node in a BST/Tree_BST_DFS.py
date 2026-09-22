'''
450. Delete Node in a BST

Given the root of a Binary Search Tree (BST) and a key, delete the node with the
given key and return the root of the BST.

The deletion should preserve the BST property.

Example 1:
    Input:
        root = [5,3,6,2,4,null,7]
        key = 3

    Output:
        [5,4,6,2,null,null,7]

Example 2:
    Input:
        root = [5,3,6,2,4,null,7]
        key = 0

    Output:
        [5,3,6,2,4,null,7]

Example 3:
    Input:
        root = []
        key = 0

    Output:
        []

Constraints:
    Number of nodes is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    Each node has a unique value.
    root is a valid BST.
    -10^5 <= key <= 10^5
'''

# Binary Search Tree + DFS

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(
        self,
        root: Optional[TreeNode],
        key: int
    ) -> Optional[TreeNode]:

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Node with only right child or no child.
            if not root.left:
                return root.right

            # Node with only left child.
            if not root.right:
                return root.left

            # Node with two children.
            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root


# -----------------------------
# Helper Functions for Testing
# -----------------------------

def inorder(root):
    if not root:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(6)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(7)

updated1 = solution.deleteNode(root1, 3)
print(inorder(updated1))
# Output: [2,4,5,6,7]

# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

updated2 = solution.deleteNode(root2, 0)
print(inorder(updated2))
# Output: [2,3,4,5,6,7]

# Example 3
root3 = None
updated3 = solution.deleteNode(root3, 0)
print(updated3)
# Output: None

# Example 4
root4 = TreeNode(1)
updated4 = solution.deleteNode(root4, 1)
print(inorder(updated4))
# Output: []

# Example 5
root5 = TreeNode(8)
root5.left = TreeNode(5)
root5.right = TreeNode(10)
root5.left.left = TreeNode(3)
root5.left.right = TreeNode(6)

updated5 = solution.deleteNode(root5, 8)
print(inorder(updated5))
# Output: [3,5,6,10]

# Example 6
root6 = TreeNode(50)
root6.left = TreeNode(30)
root6.right = TreeNode(70)
root6.right.left = TreeNode(60)
root6.right.right = TreeNode(80)

updated6 = solution.deleteNode(root6, 70)
print(inorder(updated6))
# Output: [30,50,60,80]
