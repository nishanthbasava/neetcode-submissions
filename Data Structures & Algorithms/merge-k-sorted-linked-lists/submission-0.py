# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time Complexity: O(n * k) , k is number of lists and n is total number of nodes
        # Space Complexity: O(1)

        dummy = ListNode(0)
        cur = dummy

        while lists:
            min_node = ListNode(1001)
            min_i = -1

            for i in range(len(lists)):
                if lists[i].val < min_node.val:
                    min_node = lists[i]
                    min_i = i

            cur.next = lists[min_i]
            cur = cur.next

            if lists[min_i].next == None:
                lists.remove(lists[min_i])
            else:
                lists[min_i] = lists[min_i].next

            cur.next = None

        return dummy.next





