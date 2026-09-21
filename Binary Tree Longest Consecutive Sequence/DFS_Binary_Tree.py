'''
298. Binary Tree Longest Consecutive Sequence

Given the root of a binary tree, return the length of the longest consecutive
sequence path.

The path must move from parent to child.

A consecutive sequence means:
    child.val == parent.val + 1

The path does not have to start at the root.

Example 1:
    Input:
        root = [1,null,3,2,4,null,null,null,5]

    Output:
        3

Explanation:
        3 -> 4 -> 5

Example 2:
    Input:
        root = [2,null,3,2,null,1]

    Output:
        2

Explanation:
        2 -> 3

Constraints:
    The number of nodes is in the range [0, 3 * 10^4].
    -3 * 10^4 <= Node.val <= 3 * 10^4
'''

# DFS + Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def dfs(node: Optional[TreeNode], parent_value: int, length: int):
            if not node:
                return

            # Continue or restart the sequence.
            if node.val == parent_value + 1:
                length += 1
            else:
                length = 1

            self.longest = max(self.longest, length)

            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)

        if root:
            dfs(root, root.val - 1, 0)

        return self.longest


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.right = TreeNode(3)
root1.right.left = TreeNode(2)
root1.right.right = TreeNode(4)
root1.right.right.right = TreeNode(5)

print(solution.longestConsecutive(root1))
# Output: 3

# Example 2
root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.left = TreeNode(2)
root2.right.left.left = TreeNode(1)

print(solution.longestConsecutive(root2))
# Output: 2

# Example 3
root3 = TreeNode(5)
root3.left = TreeNode(6)
root3.left.left = TreeNode(7)

print(solution.longestConsecutive(root3))
# Output: 3

# Example 4
root4 = TreeNode(3)
root4.left = TreeNode(2)
root4.right = TreeNode(4)
root4.right.right = TreeNode(5)

print(solution.longestConsecutive(root4))
# Output: 3

# Example 5
root5 = None

print(solution.longestConsecutive(root5))
# Output: 0
