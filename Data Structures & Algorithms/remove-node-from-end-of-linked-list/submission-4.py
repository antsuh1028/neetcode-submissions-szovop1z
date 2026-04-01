# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        
        
        length = 0
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        print(length, length - n)

        curr = head
        count = 0
        prev = None
        while curr:
            if count == (length - n):
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                return head
            else:
                prev = curr
                curr = curr.next    
                count += 1

        