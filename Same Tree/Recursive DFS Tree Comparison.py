'''
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: True

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: False

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: False

Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -10^4 <= Node.val <= 10^4
'''

# Recursive DFS Tree Comparison
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Both nodes are None
        if not p and not q:
            return True

        # One node is None or values don't match
        if not p or not q or p.val != q.val:
            return False

        # Compare left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )


# Example usage
solution = Solution()

# Example 1
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

print(solution.isSameTree(p1, q1))  # Output: True

# Example 2
p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)

print(solution.isSameTree(p2, q2))  # Output: False

# Example 3
p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)

q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)

print(solution.isSameTree(p3, q3))  # Output: False
