# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, treeMax):
            if node == None:
                return

            if node.val >= treeMax:
                self.count += 1

            treeMax = max(treeMax, node.val)
            dfs(node.left, treeMax)
            dfs(node.right, treeMax)

        dfs(root, root.val)
        return self.count

            

        

            