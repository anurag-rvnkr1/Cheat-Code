'''
234. Palindrome Linked List

Given the head of a singly linked list, return True if it is a palindrome,
or False otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: True

Example 2:
    Input: head = [1,2]
    Output: False

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9

Follow-up:
    Could you do it in O(n) time and O(1) space?
'''

# Linked List + Two Pointers

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list.
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half.
        previous = None
        current = slow

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # Step 3: Compare first half and reversed second half.
        left = head
        right = previous

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


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
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)

print(solution.isPalindrome(head1))  # Output: True

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)

print(solution.isPalindrome(head2))  # Output: False

# Example 3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(2)
head3.next.next.next.next = ListNode(1)

print(solution.isPalindrome(head3))  # Output: True

# Example 4
head4 = ListNode(1)

print(solution.isPalindrome(head4))  # Output: True
