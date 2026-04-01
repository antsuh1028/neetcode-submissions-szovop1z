# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find middle
        s,f = head, head.next

        while f and f.next:
            f = f.next.next
            s = s.next

        prev = None
        curr = s.next
        s.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr1,curr2 = head, prev

        while curr1 and curr2:
            tmp1,tmp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1, curr2 = tmp1, tmp2






