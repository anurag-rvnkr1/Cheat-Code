'''
331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use preorder traversal.

When a node is null, record it using '#'.

Given a comma-separated preorder serialization string, return True if it is a
correct serialization of a binary tree without reconstructing the tree.

Example 1:
    Input:
        preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"

    Output:
        True

Example 2:
    Input:
        preorder = "1,#"

    Output:
        False

Example 3:
    Input:
        preorder = "9,#,#,1"

    Output:
        False

Constraints:
    1 <= preorder.length <= 10^4
    preorder consists of digits, '#', and commas.
'''

# Degree Counting (Optimal O(n) Solution)


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # One incoming slot for the root.
        slots = 1

        for node in preorder.split(","):
            # Every node occupies one slot.
            slots -= 1

            if slots < 0:
                return False

            # Non-null nodes create two new slots.
            if node != "#":
                slots += 2

        return slots == 0


# Example usage
solution = Solution()

# Example 1
preorder1 = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(solution.isValidSerialization(preorder1))
# Output: True

# Example 2
preorder2 = "1,#"
print(solution.isValidSerialization(preorder2))
# Output: False

# Example 3
preorder3 = "9,#,#,1"
print(solution.isValidSerialization(preorder3))
# Output: False

# Example 4
preorder4 = "#"
print(solution.isValidSerialization(preorder4))
# Output: True

# Example 5
preorder5 = "7,2,#,2,#,#,#,6,#"
print(solution.isValidSerialization(preorder5))
# Output: False

# Example 6
preorder6 = "1,2,#,#,3,#,#"
print(solution.isValidSerialization(preorder6))
# Output: True
