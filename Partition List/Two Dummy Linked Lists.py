'''
86. Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
'''

# Two Dummy Linked Lists
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy
        large = large_dummy

        curr = head

        while curr:

            if curr.val < x:
                small.next = curr
                small = small.next

            else:
                large.next = curr
                large = large.next

            curr = curr.next

        # Connect the two partitions
        small.next = large_dummy.next

        # Important: terminate the large list
        large.next = None

        return small_dummy.next


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

head1 = build_list([1, 4, 3, 2, 5, 2])
print_list(solution.partition(head1, 3))  # Output: [1,2,2,4,3,5]

head2 = build_list([2, 1])
print_list(solution.partition(head2, 2))  # Output: [1,2]
