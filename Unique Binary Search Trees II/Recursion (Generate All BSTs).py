'''
95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees), which have exactly n nodes of unique values from 1 to n.

Return the answer in any order.

Example 1:
    Input: n = 3
    Output:
    [
        [1,null,2,null,3],
        [1,null,3,2],
        [2,1,3],
        [3,1,null,null,2],
        [3,2,null,1]
    ]

Example 2:
    Input: n = 1
    Output: [[1]]

Constraints:
    1 <= n <= 8
'''

# Recursion (Generate All BSTs)
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def build(start, end):

            if start > end:
                return [None]

            trees = []

            for root in range(start, end + 1):

                left_trees = build(start, root - 1)
                right_trees = build(root + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            return trees

        return build(1, n)


# Example usage
def serialize(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


solution = Solution()

trees1 = solution.generateTrees(3)
print([serialize(tree) for tree in trees1])
# Output:
# [
# [1,None,2,None,3],
# [1,None,3,2],
# [2,1,3],
# [3,1,None,None,2],
# [3,2,None,1]
# ]

trees2 = solution.generateTrees(1)
print([serialize(tree) for tree in trees2])
# Output: [[1]]
