'''
366. Find Leaves of Binary Tree

Given the root of a binary tree, collect a tree's nodes as if you were:

    - Collect all the leaf nodes.
    - Remove all the leaf nodes.
    - Repeat until the tree becomes empty.

Return a list of lists where each inner list contains the values removed
at each round.

Example 1:
    Input:
        root = [1,2,3,4,5]

    Output:
        [[4,5,3],[2],[1]]

Example 2:
    Input:
        root = [1]

    Output:
        [[1]]

Constraints:
    The number of nodes is in the range [0, 100].
    -100 <= Node.val <= 100
'''

# Postorder DFS + Tree Height

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            height = max(left_height, right_height) + 1

            if height == len(result):
                result.append([])

            result[height].append(node.val)

            return height

        dfs(root)

        return result


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print(solution.findLeaves(root1))
# Output: [[4,5,3],[2],[1]]

# Example 2
root2 = TreeNode(1)

print(solution.findLeaves(root2))
# Output: [[1]]

# Example 3
root3 = TreeNode(10)
root3.left = TreeNode(20)
root3.right = TreeNode(30)
root3.left.left = TreeNode(40)
root3.left.right = TreeNode(50)
root3.right.right = TreeNode(60)

print(solution.findLeaves(root3))
# Output: [[40,50,60],[20,30],[10]]

# Example 4
root4 = TreeNode(5)
root4.left = TreeNode(4)
root4.left.left = TreeNode(3)
root4.left.left.left = TreeNode(2)

print(solution.findLeaves(root4))
# Output: [[2],[3],[4],[5]]

# Example 5
root5 = TreeNode(7)
root5.left = TreeNode(3)
root5.right = TreeNode(9)
root5.left.left = TreeNode(1)
root5.left.right = TreeNode(5)
root5.right.left = TreeNode(8)
root5.right.right = TreeNode(10)

print(solution.findLeaves(root5))
# Output: [[1,5,8,10],[3,9],[7]]

# Example 6
root6 = None

print(solution.findLeaves(root6))
# Output: []
