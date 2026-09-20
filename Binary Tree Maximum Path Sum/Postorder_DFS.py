'''
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
has an edge connecting them. A node can only appear in the sequence at most once.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
    Input: root = [1,2,3]
    Output: 6

Explanation:
    The maximum path is 2 -> 1 -> 3 with sum = 6.

Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42

Explanation:
    The maximum path is 15 -> 20 -> 7 with sum = 42.

Constraints:
    The number of nodes in the tree is in the range [1, 3 * 10^4].
    -1000 <= Node.val <= 1000
'''

# Postorder DFS

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # Ignore negative paths.
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Maximum path passing through current node.
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum gain to parent.
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

print(solution.maxPathSum(root1))  # Output: 6

# Example 2
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

print(solution.maxPathSum(root2))  # Output: 42

# Example 3
root3 = TreeNode(-3)

print(solution.maxPathSum(root3))  # Output: -3
