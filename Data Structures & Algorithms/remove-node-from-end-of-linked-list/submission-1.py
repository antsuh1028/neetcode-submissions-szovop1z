# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointer
        first, second = head, head

        
        for i in range(n):
            first = first.next
        # if not first:
        #     return None
        
        prev = None
        while first:
            first = first.next
            prev = second
            second = second.next
        
        #remove the node
        if prev:
            prev.next = second.next
            
        else:
            head = second.next

        second.next = None
        return head


