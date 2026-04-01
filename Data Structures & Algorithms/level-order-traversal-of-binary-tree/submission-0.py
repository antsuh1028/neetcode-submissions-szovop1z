from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lst = []
        order = deque([])
        order.append(root)

        while order:
            temp = []
            lenO = len(order)
            for x in range(lenO): 
                node = order.popleft()
                if node.left:
                    order.append(node.left)
                if node.right:
                    order.append(node.right)
                temp.append(node.val)
            lst.append(temp)
        return lst
            



        return lst

