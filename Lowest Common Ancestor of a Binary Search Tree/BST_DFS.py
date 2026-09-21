'''
235. Lowest Common Ancestor of a Binary Search Tree

Given a Binary Search Tree (BST), find the lowest common ancestor (LCA)
of two given nodes in the BST.

According to the definition of LCA:
    "The lowest common ancestor is the lowest node in the tree that has both
    p and q as descendants (where a node can be a descendant of itself)."

Example 1:
    Input:
        root = [6,2,8,0,4,7,9,null,null,3,5]
        p = 2
        q = 8
    Output: 6

Example 2:
    Input:
        root = [6,2,8,0,4,7,9,null,null,3,5]
        p = 2
        q = 4
    Output: 2

Explanation:
    Node 2 is an ancestor of node 4.

Example 3:
    Input:
        root = [2,1]
        p = 2
        q = 1
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [2, 10^5].
    -10^9 <= Node.val <= 10^9
    All Node.val values are unique.
    p != q
    p and q exist in the BST.
'''

# Binary Search Tree + DFS

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

        current = root

        while current:

            # Both nodes are in the left subtree.
            if p.val < current.val and q.val < current.val:
                current = current.left

            # Both nodes are in the right subtree.
            elif p.val > current.val and q.val > current.val:
                current = current.right

            # Current node splits the path or equals one of the nodes.
            else:
                return current

        return None


# Example usage
solution = Solution()

# Example BST
#            6
#         /     \
#        2       8
#      /   \   /   \
#     0     4 7     9
#          / \
#         3   5

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Example 1
p1 = root.left        # Node 2
q1 = root.right       # Node 8
print(solution.lowestCommonAncestor(root, p1, q1).val)
# Output: 6

# Example 2
p2 = root.left        # Node 2
q2 = root.left.right  # Node 4
print(solution.lowestCommonAncestor(root, p2, q2).val)
# Output: 2

# Example 3
root2 = TreeNode(2)
root2.left = TreeNode(1)

p3 = root2            # Node 2
q3 = root2.left       # Node 1
print(solution.lowestCommonAncestor(root2, p3, q3).val)
# Output: 2
