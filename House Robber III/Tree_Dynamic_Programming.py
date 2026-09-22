'''
337. House Robber III

The thief has found himself a new place for his thievery again.

This time, all houses form a binary tree.

If two directly connected houses are robbed on the same night,
the police will be alerted.

Return the maximum amount of money the thief can rob without
alerting the police.

Example 1:
    Input:
        root = [3,2,3,null,3,null,1]

    Output:
        7

Explanation:
        Rob houses with values 3 + 3 + 1 = 7.

Example 2:
    Input:
        root = [3,4,5,1,3,null,1]

    Output:
        9

Explanation:
        Rob houses with values 4 + 5 = 9.

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    0 <= Node.val <= 10^4
'''

# Tree Dynamic Programming (Postorder DFS)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # Returns (rob_current, skip_current)
        def dfs(node: Optional[TreeNode]):
            if not node:
                return (0, 0)

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # Rob current node.
            rob_current = (
                node.val
                + left_skip
                + right_skip
            )

            # Skip current node.
            skip_current = (
                max(left_rob, left_skip)
                + max(right_rob, right_skip)
            )

            return (rob_current, skip_current)

        rob_root, skip_root = dfs(root)

        return max(rob_root, skip_root)


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(1)

print(solution.rob(root1))
# Output: 7

# Example 2
root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(1)

print(solution.rob(root2))
# Output: 9

# Example 3
root3 = TreeNode(10)

print(solution.rob(root3))
# Output: 10

# Example 4
root4 = TreeNode(2)
root4.left = TreeNode(1)
root4.right = TreeNode(3)
root4.left.right = TreeNode(4)

print(solution.rob(root4))
# Output: 7

# Example 5
root5 = TreeNode(4)
root5.left = TreeNode(1)
root5.right = TreeNode(5)
root5.left.left = TreeNode(2)
root5.left.right = TreeNode(3)

print(solution.rob(root5))
# Output: 10

# Example 6
root6 = TreeNode(5)
root6.left = TreeNode(3)
root6.right = TreeNode(6)
root6.left.left = TreeNode(2)
root6.left.right = TreeNode(4)
root6.right.right = TreeNode(7)

print(solution.rob(root6))
# Output: 18
