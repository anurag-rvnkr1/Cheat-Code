'''
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]

Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
'''

# In-Place Sublist Reversal
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node before the left position
        for _ in range(left - 1):
            prev = prev.next

        # Reverse nodes from left to right
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


# Example usage
def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


solution = Solution()

head1 = build_list([1, 2, 3, 4, 5])
print_list(solution.reverseBetween(head1, 2, 4))  # Output: [1,4,3,2,5]

head2 = build_list([5])
print_list(solution.reverseBetween(head2, 1, 1))  # Output: [5]
