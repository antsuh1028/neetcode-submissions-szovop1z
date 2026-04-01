# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        init_bounds = [-math.inf, math.inf]

        def traverse( r: Optional[TreeNode], bounds ):
            if not r:
                return True
            if r.val >= bounds[1] or r.val <= bounds[0]:
                return False
            return traverse(r.left, [bounds[0],r.val]) and  traverse(r.right, [r.val, bounds[1]])

        return traverse(root, init_bounds)


