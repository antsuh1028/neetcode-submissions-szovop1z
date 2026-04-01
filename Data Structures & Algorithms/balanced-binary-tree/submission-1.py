# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getBranchLength(root: Optional[TreeNode]) -> int:
            if not root: 
                return (True, 0)
            
            ll, lr = getBranchLength(root.left)
            rl,rr = getBranchLength(root.right)

            balanced = ll and rl and abs(lr - rr) <= 1


            return (balanced, max(lr,rr) + 1)
        return getBranchLength(root)[0]


