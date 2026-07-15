# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time Complexity: O(m * n)
        # Space Complexity: O(m + n)

        def dfs(node1, node2): 
            if node1 == None and node2 == None:
                return True

            elif node1 == None or node2 == None:
                return False

            elif node1.val != node2.val:
                return False

            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        def dfs_2(node, subnode):
            if node == None:
                return False

            if dfs(node, subnode):
                return True
            
            return dfs_2(node.left, subnode) or dfs_2(node.right, subnode)

        return dfs_2(root, subRoot)