# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node,mx):
            if not node:
                return 0
            print(node.val,mx)
            if node.val >= mx:
                print("good")
                mx = node.val
                return 1 + dfs(node.left,mx) + dfs(node.right,mx)
            else:
                #1 + 
                return dfs(node.left,mx) + dfs(node.right,mx)
        return dfs(root,-float("inf"))
