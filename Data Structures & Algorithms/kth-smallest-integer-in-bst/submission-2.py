# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        self.lst = []
        self.counter = 0

        def dfs(node):
            if node == None:
                return 

            dfs(node.left)
            self.lst.append(node.val)
            self.counter += 1

            if self.counter == k:
                return node.val
            
            dfs(node.right)

        dfs(root)
        return self.lst[k - 1]