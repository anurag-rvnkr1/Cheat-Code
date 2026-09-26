'''
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value
in each row of the tree.

Example 1:
    Input:
        root = [1,3,2,5,3,null,9]

    Output:
        [1,3,9]

Example 2:
    Input:
        root = [1,2,3]

    Output:
        [1,3]

Constraints:
    Number of nodes is in the range [0, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
'''

# Tree + Level Order Traversal (BFS)

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            maximum = float("-inf")

            for _ in range(level_size):
                node = queue.popleft()
                maximum = max(maximum, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            answer.append(maximum)

        return answer


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(9)

print(solution.largestValues(root1))
# Output: [1,3,9]

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(solution.largestValues(root2))
# Output: [1,3]

# Example 3
root3 = TreeNode(-1)
root3.left = TreeNode(-5)
root3.right = TreeNode(-3)

print(solution.largestValues(root3))
# Output: [-1,-3]

# Example 4
root4 = TreeNode(10)

print(solution.largestValues(root4))
# Output: [10]

# Example 5
root5 = None

print(solution.largestValues(root5))
# Output: []

# Example 6
root6 = TreeNode(5)
root6.left = TreeNode(1)
root6.right = TreeNode(8)
root6.left.left = TreeNode(0)
root6.left.right = TreeNode(4)
root6.right.left = TreeNode(7)
root6.right.right = TreeNode(9)

print(solution.largestValues(root6))
# Output: [5,8,9]
