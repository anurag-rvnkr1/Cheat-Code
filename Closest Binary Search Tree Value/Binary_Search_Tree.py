'''
270. Closest Binary Search Tree Value

Given the root of a Binary Search Tree (BST) and a target value, return the
value in the BST that is closest to the target.

You are guaranteed to have only one unique closest value.

Example 1:
    Input:
        root = [4,2,5,1,3]
        target = 3.714286

    Output:
        4

Example 2:
    Input:
        root = [1]
        target = 4.428571

    Output:
        1

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    0 <= Node.val <= 10^9
    -10^9 <= target <= 10^9
'''

# Binary Search Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        current = root

        while current:
            # Update closest value if current node is nearer to target.
            if abs(current.val - target) < abs(closest - target):
                closest = current.val

            # Traverse according to BST property.
            if target < current.val:
                current = current.left
            elif target > current.val:
                current = current.right
            else:
                return current.val

        return closest


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

target1 = 3.714286
print(solution.closestValue(root1, target1))
# Output: 4

# Example 2
root2 = TreeNode(1)

target2 = 4.428571
print(solution.closestValue(root2, target2))
# Output: 1

# Example 3
root3 = TreeNode(8)
root3.left = TreeNode(3)
root3.right = TreeNode(10)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(6)
root3.left.right.left = TreeNode(4)
root3.left.right.right = TreeNode(7)

target3 = 5.8
print(solution.closestValue(root3, target3))
# Output: 6

# Example 4
root4 = TreeNode(2)
root4.left = TreeNode(1)
root4.right = TreeNode(3)

target4 = 2.1
print(solution.closestValue(root4, target4))
# Output: 2
