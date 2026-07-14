# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(m + n), m is length of l1 and n is length of l2
        # Space Complexity: O(1)

        dummy = ListNode()
        carry = False
        cur = dummy

        while l1 and l2:
            total = l1.val + l2.val

            if carry:
                total += 1

            cur.next = ListNode(total % 10)

            if total >= 10:
                carry = True
            else:
                carry = False

            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l1:
            if carry:
                total = l1.val + 1
                cur.next = ListNode(total % 10)

                if total == 10:
                    carry = True
                else:
                    carry = False
            else:
                cur.next = ListNode(l1.val)
                carry = False

            l1 = l1.next
            cur = cur.next

        while l2:
            if carry:
                total = l2.val + 1
                cur.next = ListNode(total % 10)

                if total == 10:
                    carry = True
                else:
                    carry = False
            else:
                cur.next = ListNode(l2.val)
                carry = False

            l2 = l2.next
            cur = cur.next

        if carry:
            cur.next = ListNode(1)

        return dummy.next