# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if node == None:
                return True

            if node.val > lower and node.val < upper:
                if node.left:
                    left = dfs(node.left, lower, node.val)
                else:
                    left = True

                if node.right:
                    right = dfs(node.right, node.val, upper)
                else:
                    right = True
            else:
                return False

            return left and right
        
        return dfs(root, float('-inf'), float('inf'))