# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        #first pass to get length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        if n == length:
            head = head.next
        else:
            prev = None
            cur = head
            for i in range(length - n):
                prev = cur
                cur = cur.next

            prev.next = cur.next

        return head