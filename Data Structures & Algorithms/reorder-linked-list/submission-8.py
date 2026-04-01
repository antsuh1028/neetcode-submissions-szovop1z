# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head, head.next

        while f and f.next:
            f = f.next.next
            s = s.next
        
        second = s.next
        prev = s.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first,second = head, prev
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        # #reverse link list from s
        # curr = s
        # temp = None
        # prev.next = None
        # previous = None
        # while curr:
        #     temp = curr.next
        #     curr.next = previous
        #     previous = curr
        #     curr = temp
        
        # temp1, temp2 = None,None
        # curr1, curr2 = head, previous

        # while curr1 and curr2:
        #     temp1 = curr1.next
        #     curr1.next = curr2
        #     temp2 = curr2.next
        #     curr2.next = temp1
        #     curr1 = temp1
        #     if not curr2.next:
        #         curr2.next = temp2
        #     curr2 = temp2
        