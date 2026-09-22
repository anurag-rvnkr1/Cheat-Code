'''
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers.

The most significant digit comes first, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

You may not modify the input lists (i.e., reversing the lists is not allowed).

Example 1:
    Input:
        l1 = [7,2,4,3]
        l2 = [5,6,4]

    Output:
        [7,8,0,7]

Example 2:
    Input:
        l1 = [2,4,3]
        l2 = [5,6,4]

    Output:
        [8,0,7]

Example 3:
    Input:
        l1 = [0]
        l2 = [0]

    Output:
        [0]

Constraints:
    Number of nodes in each list is in the range [1, 100].
    0 <= Node.val <= 9
    The input lists do not contain leading zeros except the number 0 itself.
'''

# Linked List + Stack

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while stack1 or stack2 or carry:
            value1 = stack1.pop() if stack1 else 0
            value2 = stack2.pop() if stack2 else 0

            total = value1 + value2 + carry

            carry = total // 10

            node = ListNode(total % 10)
            node.next = head
            head = node

        return head


# -----------------------------
# Helper Functions
# -----------------------------

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Example usage
solution = Solution()

# Example 1
l1 = build_linked_list([7,2,4,3])
l2 = build_linked_list([5,6,4])
print(linked_list_to_list(solution.addTwoNumbers(l1, l2)))
# Output: [7,8,0,7]

# Example 2
l3 = build_linked_list([2,4,3])
l4 = build_linked_list([5,6,4])
print(linked_list_to_list(solution.addTwoNumbers(l3, l4)))
# Output: [8,0,7]

# Example 3
l5 = build_linked_list([0])
l6 = build_linked_list([0])
print(linked_list_to_list(solution.addTwoNumbers(l5, l6)))
# Output: [0]

# Example 4
l7 = build_linked_list([9,9,9,9])
l8 = build_linked_list([1])
print(linked_list_to_list(solution.addTwoNumbers(l7, l8)))
# Output: [1,0,0,0,0]

# Example 5
l9 = build_linked_list([1])
l10 = build_linked_list([9,9,9])
print(linked_list_to_list(solution.addTwoNumbers(l9, l10)))
# Output: [1,0,0,0]

# Example 6
l11 = build_linked_list([6,1,7])
l12 = build_linked_list([2,9,5])
print(linked_list_to_list(solution.addTwoNumbers(l11, l12)))
# Output: [9,1,2]
