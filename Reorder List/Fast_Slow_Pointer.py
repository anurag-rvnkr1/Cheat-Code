'''
143. Reorder List

You are given the head of a singly linked list.

Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 10^4].
    1 <= Node.val <= 1000
'''

# Fast & Slow Pointer + Reverse Linked List + Merge

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list.
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half.
        prev = None
        current = slow.next
        slow.next = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Merge the two halves.
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


# Helper function to print linked list
def printList(head):
    current = head

    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next

    print()


# Example usage
solution = Solution()

# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

solution.reorderList(head1)
printList(head1)
# Output: 1 -> 4 -> 2 -> 3

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)

solution.reorderList(head2)
printList(head2)
# Output: 1 -> 5 -> 2 -> 4 -> 3

# Example 3
head3 = ListNode(1)

solution.reorderList(head3)
printList(head3)
# Output: 1
