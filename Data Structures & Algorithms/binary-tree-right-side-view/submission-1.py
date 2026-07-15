# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #need to make a list of the right most values of each layer

        #so like make a list of each layer and just add the last number from that layer to the list

        #bfs again
        from collections import deque

        if root is None:
            return []

        lst = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level.append(node.val)
                queue.popleft()

            lst.append(level[-1])

        return lst