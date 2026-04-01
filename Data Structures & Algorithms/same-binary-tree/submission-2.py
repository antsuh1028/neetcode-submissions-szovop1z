# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #for each p_node and q_node, if both are equal value, return both q_node and p_node children are true, else return False
        #base case -> if p_node and q_node both None: return True

        if q is None and p is None:
            return True
        if q is None or p is None:
            return False
            
        if q.val == p.val:
            return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)

        return False