# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #slow and fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        l1, l2 = head, slow.next
        slow.next = None

        #reverse l2
        curr, prev = l2,None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            if not temp:
                break
            curr = temp
        l2 = prev
        # curr2 = curr
        # while curr2:
        #     print(curr2.val)
        #     curr2 = curr2.next

        #two pointer merge
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2

        # if l1:
        #     l2.next = l1
        


        
