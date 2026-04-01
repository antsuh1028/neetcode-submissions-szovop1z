# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = None
        prev = None

        while curr:
            print(curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


        
        # 1->2->3->4
        #

        #4->3->2->1
        