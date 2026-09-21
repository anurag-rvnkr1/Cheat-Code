'''
285. Inorder Successor in BST

Given the root of a Binary Search Tree (BST) and a node p in it,
return the inorder successor of p in the BST.

The inorder successor of p is the node with the smallest key greater than p.val.

If no successor exists, return None.

Example 1:
    Input:
        root = [2,1,3]
        p = 1

    Output:
        2

Example 2:
    Input:
        root = [5,3,6,2,4,null,null,1]
        p = 6

    Output:
        None

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -10^5 <= Node.val <= 10^5
    All Node.val values are unique.
    p is guaranteed to be a node in the BST.
'''

# Binary Search Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(
        self,
        root: Optional[TreeNode],
        p: TreeNode
    ) -> Optional[TreeNode]:

        successor = None
        current = root

        while current:

            # Current node is a possible successor.
            if p.val < current.val:
                successor = current
                current = current.left

            else:
                current = current.right

        return successor


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

p1 = root1.left

successor1 = solution.inorderSuccessor(root1, p1)
print(successor1.val if successor1 else None)
# Output: 2


# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)

p2 = root2.right

successor2 = solution.inorderSuccessor(root2, p2)
print(successor2.val if successor2 else None)
# Output: None


# Example 3
p3 = root2.left

successor3 = solution.inorderSuccessor(root2, p3)
print(successor3.val if successor3 else None)
# Output: 4


# Example 4
p4 = root2.left.right

successor4 = solution.inorderSuccessor(root2, p4)
print(successor4.val if successor4 else None)
# Output: 5
