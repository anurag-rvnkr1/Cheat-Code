'''
82. Remove Duplicates from Sorted List II

You are given the head of a sorted linked list.

Delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:
    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]

Example 2:
    Input: head = [1,1,1,2,3]
    Output: [2,3]

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
'''

# Dummy Node + Two Pointers
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            # Check if current value is duplicated
            if curr.next and curr.val == curr.next.val:

                duplicate = curr.val

                # Skip all nodes with the duplicate value
                while curr and curr.val == duplicate:
                    curr = curr.next

                # Connect previous unique node to next distinct node
                prev.next = curr

            else:
                # Current node is unique
                prev = curr
                curr = curr.next

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

head1 = build_list([1, 2, 3, 3, 4, 4, 5])
print_list(solution.deleteDuplicates(head1))  # Output: [1,2,5]

head2 = build_list([1, 1, 1, 2, 3])
print_list(solution.deleteDuplicates(head2))  # Output: [2,3]
