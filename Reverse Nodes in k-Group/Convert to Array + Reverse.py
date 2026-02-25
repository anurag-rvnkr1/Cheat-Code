'''
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    
Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
 
Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000
'''
#Convert to Array + Reverse

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):

        if not head or k == 1:
            return head

        arr = []
        curr = head

        # Store values
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Reverse in groups
        for i in range(0, len(arr), k):

            if i + k <= len(arr):
                arr[i:i+k] = reversed(arr[i:i+k])

        # Rebuild list
        dummy = ListNode(0)
        curr = dummy

        for v in arr:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next

#Example Usage
sol=Solution()
print(sol.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
print(sol.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3))