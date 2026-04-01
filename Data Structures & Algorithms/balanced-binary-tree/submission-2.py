# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #for each node, get the height of the left and right
        #compare heights, if heights differ by more that 1, return something
        #base case -> when node == None
        
        def dfs(node):
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        return False if dfs(root) == -1 else True



