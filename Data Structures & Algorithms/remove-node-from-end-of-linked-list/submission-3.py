# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        #want slow to end up at (length - n)th term so can delete the next one

        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
       
        slow.next = slow.next.next

        return head