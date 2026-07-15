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

        def dfs(node):
            if node == None:
                return 

            if node.left:
                dfs(node.left)
                self.lst.append(node.val)
            else:
                self.lst.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)
        print(self.lst)
        return self.lst[k - 1]