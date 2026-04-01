# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recursion
        # basecase -> when the node is null, return 0
        # X else return the max(dfs(left), dfs(right)) + 1
        # X or else return dfs(left) + dfs(right) + 1
        # get the heights of hte left and right children, add, then updata max
        mx = 0
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal mx
            mx = max(mx, left + right)

            return max(left,right) + 1
        dfs(root)
        return mx