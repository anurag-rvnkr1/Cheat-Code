'''
513. Find Bottom Left Tree Value

Given the root of a binary tree, return the leftmost value in the last row
of the tree.

Example 1:
    Input:
        root = [2,1,3]

    Output:
        1

Example 2:
    Input:
        root = [1,2,3,4,null,5,6,null,null,7]

    Output:
        7

Constraints:
    Number of nodes is in the range [1, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
'''

# Tree + Level Order Traversal (BFS)

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        bottom_left = root.val

        while queue:
            level_size = len(queue)

            # First node of the current level is the leftmost node.
            bottom_left = queue[0].val

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return bottom_left


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(solution.findBottomLeftValue(root1))
# Output: 1

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.right.left = TreeNode(5)
root2.right.right = TreeNode(6)
root2.right.left.left = TreeNode(7)

print(solution.findBottomLeftValue(root2))
# Output: 7

# Example 3
root3 = TreeNode(10)
print(solution.findBottomLeftValue(root3))
# Output: 10

# Example 4
root4 = TreeNode(5)
root4.left = TreeNode(3)
root4.left.left = TreeNode(2)
root4.left.left.left = TreeNode(1)

print(solution.findBottomLeftValue(root4))
# Output: 1

# Example 5
root5 = TreeNode(8)
root5.left = TreeNode(4)
root5.right = TreeNode(12)
root5.left.left = TreeNode(2)
root5.left.right = TreeNode(6)
root5.right.left = TreeNode(10)
root5.right.right = TreeNode(14)

print(solution.findBottomLeftValue(root5))
# Output: 2

# Example 6
root6 = TreeNode(1)
root6.right = TreeNode(2)
root6.right.right = TreeNode(3)
root6.right.right.right = TreeNode(4)

print(solution.findBottomLeftValue(root6))
# Output: 4
