'''
107. Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.

(Level order traversal visits nodes level by level from left to right, starting from the leaf level up to the root.)

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[15,7],[9,20],[3]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
'''

# BFS + Reverse Levels
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result[::-1]


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(solution.levelOrderBottom(root1))
# Output: [[15,7],[9,20],[3]]

# Example 2
root2 = TreeNode(1)
print(solution.levelOrderBottom(root2))
# Output: [[1]]

# Example 3
print(solution.levelOrderBottom(None))
# Output: []
