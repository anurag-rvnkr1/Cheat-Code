'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
 
Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
'''
#Two Pass
class Solution:
    def removeNthFromEnd(self, head, n):

        # Step 1: Count nodes
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        # If removing first node
        if length == n:
            return head.next

        # Step 2: Go to (length - n - 1)th node
        temp = head

        for _ in range(length - n - 1):
            temp = temp.next

        # Step 3: Remove node
        temp.next = temp.next.next

        return head
    
#Example Usage
sol = Solution()
print(sol.removeNthFromEnd([1,2,3,4,5], 2))  # Output: [1,2,3,5]
print(sol.removeNthFromEnd([1], 1))          # Output: []