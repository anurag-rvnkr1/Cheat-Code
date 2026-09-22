'''
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of
paths where the sum of the values along the path equals targetSum.

The path:
    - Must go downwards (parent to child).
    - Does not need to start at the root.
    - Does not need to end at a leaf.

Example 1:
    Input:
        root = [10,5,-3,3,2,null,11,3,-2,null,1]
        targetSum = 8

    Output:
        3

Example 2:
    Input:
        root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
        targetSum = 22

    Output:
        3

Constraints:
    Number of nodes is in the range [0, 1000].
    -10^9 <= Node.val <= 10^9
    -1000 <= targetSum <= 1000
'''

# Tree DFS + Prefix Sum

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        paths = 0

        def dfs(node: Optional[TreeNode], current_sum: int):
            nonlocal paths

            if not node:
                return

            current_sum += node.val

            # Count paths ending at current node.
            paths += prefix_count[current_sum - targetSum]

            prefix_count[current_sum] += 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Backtrack.
            prefix_count[current_sum] -= 1

        dfs(root, 0)
        return paths


# -----------------------------
# Example usage
# -----------------------------
solution = Solution()

# Example 1
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(-3)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(2)
root1.right.right = TreeNode(11)
root1.left.left.left = TreeNode(3)
root1.left.left.right = TreeNode(-2)
root1.left.right.right = TreeNode(1)

print(solution.pathSum(root1, 8))
# Output: 3

# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(4)
root2.right = TreeNode(8)
root2.left.left = TreeNode(11)
root2.left.left.left = TreeNode(7)
root2.left.left.right = TreeNode(2)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(4)
root2.right.right.left = TreeNode(5)
root2.right.right.right = TreeNode(1)

print(solution.pathSum(root2, 22))
# Output: 3

# Example 3
root3 = TreeNode(1)
root3.left = TreeNode(-2)
root3.right = TreeNode(-3)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(3)
root3.left.left.left = TreeNode(-1)
root3.right.left = TreeNode(-2)

print(solution.pathSum(root3, -1))
# Output: 4

# Example 4
root4 = TreeNode(1)
print(solution.pathSum(root4, 1))
# Output: 1

# Example 5
root5 = None
print(solution.pathSum(root5, 0))
# Output: 0

# Example 6
root6 = TreeNode(0)
root6.left = TreeNode(1)
root6.right = TreeNode(1)
root6.left.left = TreeNode(1)
root6.left.right = TreeNode(-1)

print(solution.pathSum(root6, 2))
# Output: 2
