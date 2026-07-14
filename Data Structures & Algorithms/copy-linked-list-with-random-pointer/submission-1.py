"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        read = head
        copy = {}
        #Two passes

        while read:
            copy[read] = Node(read.val)
            read = read.next

        read = head

        while read:
            copy[read].next = copy[read.next] if read.next else None
            copy[read].random = copy[read.random] if read.random else None
            read = read.next

        return copy[head] if head else None
