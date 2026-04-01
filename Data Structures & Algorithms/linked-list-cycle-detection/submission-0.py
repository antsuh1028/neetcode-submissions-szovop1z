# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        nodes = set()

        while curr:
            if curr.val in nodes:
                return True
            nodes.add(curr.val)
            curr = curr.next
        
        return False
