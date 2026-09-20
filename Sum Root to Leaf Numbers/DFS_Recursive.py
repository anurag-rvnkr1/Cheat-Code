'''
129. Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.

Example 1:
    Input: root = [1,2,3]
    Output: 25

Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, the total sum is 12 + 13 = 25.

Example 2:
    Input: root = [4,9,0,5,1]
    Output: 1026

Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, the total sum is 495 + 491 + 40 = 1026.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
'''

# Depth-First Search (Recursive)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current_number):
            if not node:
                return 0

            current_number = current_number * 10 + node.val

            # If it is a leaf node, return the formed number.
            if not node.left and not node.right:
                return current_number

            return (
                dfs(node.left, current_number)
                + dfs(node.right, current_number)
            )

        return dfs(root, 0)


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

print(solution.sumNumbers(root1))  # Output: 25

# Example 2
root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)

print(solution.sumNumbers(root2))  # Output: 1026

# Example 3
root3 = TreeNode(0)

print(solution.sumNumbers(root3))  # Output: 0
