'''
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

You must sort the linked list in O(n log n) time and O(log n) space complexity.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 5 * 10^4].
    -10^5 <= Node.val <= 10^5
'''

# Merge Sort

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the list.
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Step 2: Recursively sort both halves.
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge two sorted linked lists.
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        current.next = left if left else right

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
head1 = ListNode(4)
head1.next = ListNode(2)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(3)

sorted_head1 = solution.sortList(head1)
printList(sorted_head1)
# Output: 1 -> 2 -> 3 -> 4

# Example 2
head2 = ListNode(-1)
head2.next = ListNode(5)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(0)

sorted_head2 = solution.sortList(head2)
printList(sorted_head2)
# Output: -1 -> 0 -> 3 -> 4 -> 5

# Example 3
head3 = None

sorted_head3 = solution.sortList(head3)
print(sorted_head3)
# Output: None
