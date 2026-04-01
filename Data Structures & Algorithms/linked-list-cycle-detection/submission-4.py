# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next

        while slow:
            if fast:
                if fast.val == slow.val:
                    return True
    
                if fast.next:
                    fast = fast.next.next
                    slow = slow.next
                else:
                    return False
            else:
                return False
            

        return False