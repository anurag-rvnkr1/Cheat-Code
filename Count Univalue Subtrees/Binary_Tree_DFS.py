'''
250. Count Univalue Subtrees

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1:
    Input: root = [5,1,5,5,5,null,5]
    Output: 4

Explanation:
            5
          /   \
         1     5
        / \     \
       5   5     5

    The four uni-value subtrees are:
        - Left leaf (5)
        - Right leaf (5)
        - Middle leaf (5)
        - Right subtree rooted at the right child (5)

Example 2:
    Input: root = []
    Output: 0

Example 3:
    Input: root = [5,5,5,5,5,null,5]
    Output: 6

Constraints:
    The number of nodes in the tree is in the range [0, 1000].
    -1000 <= Node.val <= 1000
'''

# Binary Tree + DFS

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            left_unival = dfs(node.left)
            right_unival = dfs(node.right)

            if not left_unival or not right_unival:
                return False

            if node.left and node.left.val != node.val:
                return False

            if node.right and node.right.val != node.val:
                return False

            self.count += 1
            return True

        dfs(root)
        return self.count


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(5)
root1.left = TreeNode(1)
root1.right = TreeNode(5)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(5)

print(solution.countUnivalSubtrees(root1))
# Output: 4

# Example 2
root2 = None

print(solution.countUnivalSubtrees(root2))
# Output: 0

# Example 3
root3 = TreeNode(5)
root3.left = TreeNode(5)
root3.right = TreeNode(5)
root3.left.left = TreeNode(5)
root3.left.right = TreeNode(5)
root3.right.right = TreeNode(5)

print(solution.countUnivalSubtrees(root3))
# Output: 6

# Example 4
root4 = TreeNode(1)
root4.left = TreeNode(1)
root4.right = TreeNode(1)
root4.left.left = TreeNode(1)
root4.left.right = TreeNode(2)

print(solution.countUnivalSubtrees(root4))
# Output: 3
