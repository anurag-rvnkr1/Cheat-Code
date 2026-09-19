'''
109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees
of every node never differs by more than one.

Example 1:
    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]

Example 2:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in head is in the range [0, 2 * 10^4].
    -10^5 <= Node.val <= 10^5
'''

# Slow and Fast Pointer + Divide and Conquer
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        # Find middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split the linked list
        prev.next = None

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root


# Example usage
def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def level_order(root):
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

    while result and result[-1] is None:
        result.pop()

    return result


solution = Solution()

head1 = build_list([-10, -3, 0, 5, 9])
root1 = solution.sortedListToBST(head1)
print(level_order(root1))
# Output: [0, -10, 5, None, -3, None, 9] (or another valid balanced BST)

head2 = build_list([])
root2 = solution.sortedListToBST(head2)
print(level_order(root2))
# Output: []
