'''
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: True

Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: False

Example 3:
    Input: root = [], targetSum = 0
    Output: False

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
'''

# Depth-First Search (Recursive)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # Check if current node is a leaf
        if not root.left and not root.right:
            return targetSum == root.val

        remaining_sum = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining_sum)
            or self.hasPathSum(root.right, remaining_sum)
        )


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.right = TreeNode(1)

print(solution.hasPathSum(root1, 22))  # Output: True

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(solution.hasPathSum(root2, 5))  # Output: False

# Example 3
print(solution.hasPathSum(None, 0))  # Output: False
