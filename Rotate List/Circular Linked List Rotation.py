'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9
'''

# Circular Linked List Rotation
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Empty list or single node
        if not head or not head.next:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Rotating by length gives the same list
        k = k % length

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head is after new tail
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head


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
print_list(solution.rotateRight(head1, 2))  # Output: [4,5,1,2,3]

head2 = build_list([0, 1, 2])
print_list(solution.rotateRight(head2, 4))  # Output: [2,0,1]
