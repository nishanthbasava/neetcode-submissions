# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        self.max_diameter = 0

        def dfs(node):
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left + right + 2)
            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter