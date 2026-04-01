# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        fast = head.next

        while curr and fast:
            print(curr.val, fast.val)
            if curr.val == fast.val:
                return True
            
            if fast.next:
                fast=fast.next.next
            else:
                break
            curr = curr.next
        
        return False
