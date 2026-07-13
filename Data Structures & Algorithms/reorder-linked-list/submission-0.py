# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        slow = None
        
        while cur:
            tmp = cur.next
            cur.next = slow
            slow = cur
            cur = tmp
            
        while slow:
            tmp = head.next
            head.next = slow
            head = tmp

            tmp = slow.next
            slow.next = head
            slow = tmp