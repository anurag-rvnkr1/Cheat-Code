'''
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer.

Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: Node with value 2

    Explanation:
        The tail connects to the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: Node with value 1

Example 3:
    Input: head = [1], pos = -1
    Output: None

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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect cycle.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Find the starting node of the cycle.
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


# Example usage
solution = Solution()

# Example 1
head1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle starts at node with value 2

cycle_node = solution.detectCycle(head1)
print(cycle_node.val if cycle_node else None)  # Output: 2

# Example 2
head2 = ListNode(1)
node5 = ListNode(2)

head2.next = node5
node5.next = head2  # Cycle starts at node with value 1

cycle_node = solution.detectCycle(head2)
print(cycle_node.val if cycle_node else None)  # Output: 1

# Example 3
head3 = ListNode(1)

cycle_node = solution.detectCycle(head3)
print(cycle_node)  # Output: None
