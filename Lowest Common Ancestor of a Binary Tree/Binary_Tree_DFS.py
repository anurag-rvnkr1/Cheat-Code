'''
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA:
    "The lowest common ancestor is the lowest node in the tree that has both
    p and q as descendants (where a node can be a descendant of itself)."

Unlike a Binary Search Tree, this tree has no ordering property.

Example 1:
    Input:
        root = [3,5,1,6,2,0,8,null,null,7,4]
        p = 5
        q = 1
    Output: 3

Example 2:
    Input:
        root = [3,5,1,6,2,0,8,null,null,7,4]
        p = 5
        q = 4
    Output: 5

Explanation:
    Node 5 is an ancestor of node 4.

Example 3:
    Input:
        root = [1,2]
        p = 1
        q = 2
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [2, 10^5].
    -10^9 <= Node.val <= 10^9
    All Node.val values are unique.
    p != q
    p and q exist in the binary tree.
'''

# Binary Tree + DFS (Recursive)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        # Base cases.
        if not root or root == p or root == q:
            return root

        # Search in left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return a node, current root is the LCA.
        if left and right:
            return root

        # Otherwise return the non-null subtree.
        return left if left else right


# Example usage
solution = Solution()

# Example Binary Tree
#              3
#           /     \
#          5       1
#        /   \   /   \
#       6     2 0     8
#            / \
#           7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

# Example 1
p1 = root.left          # Node 5
q1 = root.right         # Node 1
print(solution.lowestCommonAncestor(root, p1, q1).val)
# Output: 3

# Example 2
p2 = root.left          # Node 5
q2 = root.left.right.right  # Node 4
print(solution.lowestCommonAncestor(root, p2, q2).val)
# Output: 5

# Example 3
root2 = TreeNode(1)
root2.left = TreeNode(2)

p3 = root2              # Node 1
q3 = root2.left         # Node 2
print(solution.lowestCommonAncestor(root2, p3, q3).val)
# Output: 1
