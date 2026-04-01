# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def traverse(root2: TreeNode):
            if q.val == root2.val or p.val == root2.val:
                return root2
            if q.val > root2.val > p.val or q.val < root2.val < p.val:
                return root2
            elif q.val > root2.val < p.val:
                return traverse(root2.right)
            elif q.val < root2.val > p.val:
                return traverse(root2.left)
        return traverse(root)

