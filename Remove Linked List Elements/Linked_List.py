'''
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes
of the linked list that have Node.val == val, and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 10^4].
    1 <= Node.val <= 50
    0 <= val <= 50
'''

# Linked List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
        self,
        head: Optional[ListNode],
        val: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


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
head1.next.next = ListNode(6)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(5)
head1.next.next.next.next.next.next = ListNode(6)

result1 = solution.removeElements(head1, 6)
printList(result1)  # Output: 1 -> 2 -> 3 -> 4 -> 5

# Example 2
head2 = None

result2 = solution.removeElements(head2, 1)
printList(result2)  # Output:

# Example 3
head3 = ListNode(7)
head3.next = ListNode(7)
head3.next.next = ListNode(7)
head3.next.next.next = ListNode(7)

result3 = solution.removeElements(head3, 7)
printList(result3)  # Output:

# Example 4
head4 = ListNode(1)
head4.next = ListNode(2)
head4.next.next = ListNode(2)
head4.next.next.next = ListNode(1)

result4 = solution.removeElements(head4, 2)
printList(result4)  # Output: 1 -> 1
