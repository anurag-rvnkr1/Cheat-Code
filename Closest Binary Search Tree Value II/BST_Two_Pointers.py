'''
272. Closest Binary Search Tree Value II

Given the root of a Binary Search Tree (BST), a target value, and an integer k,
return the k values in the BST that are closest to the target.

You may return the answer in any order.

You are guaranteed that there is only one unique set of k values closest
to the target.

Example 1:
    Input:
        root = [4,2,5,1,3]
        target = 3.714286
        k = 2

    Output: [4,3]

Example 2:
    Input:
        root = [1]
        target = 0.000000
        k = 1

    Output: [1]

Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 10^4
    0 <= Node.val <= 10^9
    -10^9 <= target <= 10^9

Follow-up:
    Assume the BST is balanced. Can you solve it in less than O(n)?
'''

# Binary Search Tree + Inorder Traversal + Two Pointers

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(
        self,
        root: Optional[TreeNode],
        target: float,
        k: int
    ) -> List[int]:

        inorder_values = []

        # Step 1: Inorder traversal gives sorted values.
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            inorder_values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Binary search for insertion position.
        left = 0
        right = len(inorder_values)

        while left < right:
            mid = (left + right) // 2

            if inorder_values[mid] < target:
                left = mid + 1
            else:
                right = mid

        left_pointer = left - 1
        right_pointer = left

        result = []

        # Step 3: Expand outward to find k closest values.
        while k > 0:
            if left_pointer < 0:
                result.append(inorder_values[right_pointer])
                right_pointer += 1

            elif right_pointer >= len(inorder_values):
                result.append(inorder_values[left_pointer])
                left_pointer -= 1

            elif (
                abs(inorder_values[left_pointer] - target) <=
                abs(inorder_values[right_pointer] - target)
            ):
                result.append(inorder_values[left_pointer])
                left_pointer -= 1

            else:
                result.append(inorder_values[right_pointer])
                right_pointer += 1

            k -= 1

        return result


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

target1 = 3.714286
k1 = 2

print(solution.closestKValues(root1, target1, k1))
# Output: [4, 3]

# Example 2
root2 = TreeNode(1)

target2 = 0.0
k2 = 1

print(solution.closestKValues(root2, target2, k2))
# Output: [1]

# Example 3
root3 = TreeNode(8)
root3.left = TreeNode(3)
root3.right = TreeNode(10)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(6)
root3.left.right.left = TreeNode(4)
root3.left.right.right = TreeNode(7)
root3.right.right = TreeNode(14)

target3 = 5.2
k3 = 3

print(solution.closestKValues(root3, target3, k3))
# Output: [6, 4, 7]

# Example 4
root4 = TreeNode(2)
root4.left = TreeNode(1)
root4.right = TreeNode(3)

target4 = 2.5
k4 = 2

print(solution.closestKValues(root4, target4, k4))
# Output: [2, 3]
