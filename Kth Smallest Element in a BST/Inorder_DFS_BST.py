'''
230. Kth Smallest Element in a BST

Given the root of a Binary Search Tree (BST) and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

A Binary Search Tree satisfies:
    - The left subtree contains only nodes with keys less than the node's key.
    - The right subtree contains only nodes with keys greater than the node's key.
    - Both left and right subtrees are also BSTs.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 10^4
    0 <= Node.val <= 10^4
'''

# Inorder DFS (Binary Search Tree)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.answer = -1

        def inorder(node: Optional[TreeNode]):
            if not node or self.answer != -1:
                return

            # Visit left subtree.
            inorder(node.left)

            # Visit current node.
            self.k -= 1
            if self.k == 0:
                self.answer = node.val
                return

            # Visit right subtree.
            inorder(node.right)

        inorder(root)
        return self.answer


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(2)

print(solution.kthSmallest(root1, 1))  # Output: 1

# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)

print(solution.kthSmallest(root2, 3))  # Output: 3

# Example 3
root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(3)

print(solution.kthSmallest(root3, 2))  # Output: 2

# Example 4
root4 = TreeNode(1)

print(solution.kthSmallest(root4, 1))  # Output: 1
