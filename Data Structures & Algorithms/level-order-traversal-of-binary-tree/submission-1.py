# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque

        if root is None:
            return []

        queue = deque([root])
        lst = []

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

            lst.append(level)

        return lst