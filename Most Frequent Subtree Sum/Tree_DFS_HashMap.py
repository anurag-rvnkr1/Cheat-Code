'''
508. Most Frequent Subtree Sum

Given the root of a binary tree, return the subtree sum(s) that occur most
frequently.

Subtree Sum:
    Sum of all node values in a subtree rooted at that node.

If multiple sums have the highest frequency, return all of them.

Example 1:
    Input:
        root = [5,2,-3]

    Output:
        [2,-3,4]

Explanation:
        Subtree sums:
        2
        -3
        4 (=5+2-3)
        All occur once.

Example 2:
    Input:
        root = [5,2,-5]

    Output:
        [2]

Explanation:
        Subtree sums:
        2
        -5
        2
        Sum 2 occurs twice.

Constraints:
    Number of nodes in tree is in range [1,10^4]
    -10^5 <= Node.val <= 10^5
'''

# Tree DFS + HashMap

from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(
        self,
        root: Optional[TreeNode]
    ) -> List[int]:

        frequency = defaultdict(int)

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            subtree_sum = node.val + left_sum + right_sum

            frequency[subtree_sum] += 1

            return subtree_sum

        dfs(root)

        highest_frequency = max(frequency.values())

        return [
            subtree_sum
            for subtree_sum, count in frequency.items()
            if count == highest_frequency
        ]


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
root1 = TreeNode(5)
root1.left = TreeNode(2)
root1.right = TreeNode(-3)

print(solution.findFrequentTreeSum(root1))
# Output: [2, -3, 4]

# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(2)
root2.right = TreeNode(-5)

print(solution.findFrequentTreeSum(root2))
# Output: [2]

# Example 3
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)

print(solution.findFrequentTreeSum(root3))
# Output: [2, 3, 6]

# Example 4
root4 = TreeNode(0)
root4.left = TreeNode(0)
root4.right = TreeNode(0)

print(solution.findFrequentTreeSum(root4))
# Output: [0]

# Example 5
root5 = TreeNode(10)
root5.left = TreeNode(-2)
root5.right = TreeNode(6)
root5.left.left = TreeNode(8)
root5.left.right = TreeNode(-4)

print(solution.findFrequentTreeSum(root5))
# Output: [8, -4, 2, 6, 18]

# Example 6
root6 = TreeNode(-1)
root6.left = TreeNode(-2)
root6.right = TreeNode(-3)

print(solution.findFrequentTreeSum(root6))
# Output: [-2, -3, -6]
