'''
255. Verify Preorder Sequence in Binary Search Tree

Given an array of unique integers preorder, determine whether it is a valid
preorder traversal sequence of a Binary Search Tree (BST).

Return True if it is valid, otherwise return False.

Example 1:
    Input: preorder = [5,2,1,3,6]
    Output: True

Explanation:
    This is a valid preorder traversal of a BST.

Example 2:
    Input: preorder = [5,2,6,1,3]
    Output: False

Explanation:
    After visiting node 6, node 1 cannot appear because it is smaller than 5.

Constraints:
    1 <= preorder.length <= 10^4
    1 <= preorder[i] <= 10^4
    All values in preorder are unique.

Follow-up:
    Could you solve it using only O(1) extra space?
'''

# Stack + Binary Search Tree

from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = float("-inf")

        for value in preorder:

            # Current value must be greater than the lower bound.
            if value < lower_bound:
                return False

            # Move to the right subtree.
            while stack and value > stack[-1]:
                lower_bound = stack.pop()

            stack.append(value)

        return True


# Example usage
solution = Solution()

# Example 1
preorder1 = [5, 2, 1, 3, 6]
print(solution.verifyPreorder(preorder1))
# Output: True

# Example 2
preorder2 = [5, 2, 6, 1, 3]
print(solution.verifyPreorder(preorder2))
# Output: False

# Example 3
preorder3 = [8, 5, 1, 7, 10, 12]
print(solution.verifyPreorder(preorder3))
# Output: True

# Example 4
preorder4 = [8, 10, 5]
print(solution.verifyPreorder(preorder4))
# Output: False
