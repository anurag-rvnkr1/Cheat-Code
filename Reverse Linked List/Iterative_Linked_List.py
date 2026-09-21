'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 5000].
    -5000 <= Node.val <= 5000
'''

# Iterative Linked List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous


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
head1.next.next.next.next = ListNode(5)

reversed_head1 = solution.reverseList(head1)
printList(reversed_head1)  # Output: 5 -> 4 -> 3 -> 2 -> 1

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)

reversed_head2 = solution.reverseList(head2)
printList(reversed_head2)  # Output: 2 -> 1

# Example 3
head3 = None

reversed_head3 = solution.reverseList(head3)
printList(reversed_head3)  # Output:

# Example 4
head4 = ListNode(10)

reversed_head4 = solution.reverseList(head4)
printList(reversed_head4)  # Output: 10
