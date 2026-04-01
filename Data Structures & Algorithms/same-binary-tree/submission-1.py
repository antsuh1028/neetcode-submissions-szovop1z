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

        def dfs(q_node, p_node):
            if q_node is None and p_node is None:
                return True
            if q_node is None or p_node is None:
                return False
            print(q_node.val,p_node.val)
            if q_node.val == p_node.val:
                return dfs(q_node.left,p_node.left) and dfs(q_node.right,p_node.right)

            return False
        
        return dfs(q,p)