'''
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.

Return the linked list sorted as well.

Example 1:
    Input: head = [1,1,2]
    Output: [1,2]

Example 2:
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
'''

# Iterative Linked List Traversal
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head


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

head1 = build_list([1, 1, 2])
print_list(solution.deleteDuplicates(head1))  # Output: [1,2]

head2 = build_list([1, 1, 2, 3, 3])
print_list(solution.deleteDuplicates(head2))  # Output: [1,2,3]
