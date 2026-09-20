'''
111. Minimum Depth of Binary Tree

Given a binary tree, return its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node
down to the nearest leaf node.

Note:
A leaf is a node with no children.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 2

Example 2:
    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5

Constraints:
    The number of nodes in the tree is in the range [0, 10^5].
    -1000 <= Node.val <= 1000
'''

# Breadth-First Search (BFS)

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # First leaf node encountered gives minimum depth.
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(solution.minDepth(root1))  # Output: 2

# Example 2
root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

print(solution.minDepth(root2))  # Output: 5

# Example 3
print(solution.minDepth(None))  # Output: 0
