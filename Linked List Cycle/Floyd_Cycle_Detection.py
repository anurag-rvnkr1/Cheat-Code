'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer.

Return True if there is a cycle in the linked list. Otherwise, return False.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: True

    Explanation:
        There is a cycle where the tail connects to the 2nd node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: True

Example 3:
    Input: head = [1], pos = -1
    Output: False

Constraints:
    The number of nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked list.
'''

# Floyd's Cycle Detection (Tortoise and Hare)

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Example usage
solution = Solution()

# Example 1
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next  # Creates cycle

print(solution.hasCycle(head1))  # Output: True

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2  # Creates cycle

print(solution.hasCycle(head2))  # Output: True

# Example 3
head3 = ListNode(1)

print(solution.hasCycle(head3))  # Output: False
