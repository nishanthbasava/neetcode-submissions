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

        self.counter = 0

        def dfs(node):
            if node == None:
                return None

            left_answer = dfs(node.left)

            if left_answer is not None:
                return left_answer

            self.counter += 1

            if self.counter == k:
                return node.val
            
            return dfs(node.right)

        return dfs(root)