# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f,s = head, head
        prev = None

        while f and f.next:
            f = f.next.next
            prev = s
            s = s.next
        print(s, prev)

        #reverse link list from s
        curr = s
        temp = None
        if not prev:
            return
        prev.next = None
        previous = None
        while curr:
            temp = curr.next
            curr.next = previous
            previous = curr
            curr = temp
        
        temp1, temp2 = None,None
        curr1, curr2 = head, previous

        while curr1 and curr2:
            # print(curr1.val,curr1.next.val, " ",curr2.val,curr2.next.val)
            temp1 = curr1.next
            curr1.next = curr2
            temp2 = curr2.next
            curr2.next = temp1
            curr1 = temp1
            print(bool(curr2.next))
            if not curr2.next:
                print(curr2.val)

                curr2.next = temp2
                print("here")
            curr2 = temp2
        # if curr1:

            
        # print(curr1.val, curr2.val)

        # while te
        # previous

            




