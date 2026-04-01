# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = l1,l2
        prev = None
        carry = 0
        res = None

        while curr1 and curr2:
            print(curr1.val,curr2.val)
            val = curr1.val + curr2.val + carry
            carry = val // 10
            print("carry", carry)
            node = ListNode(val % 10, None)
        
            if prev:
                prev.next = node
            else:
                res = node

            prev = node
            curr1,curr2 = curr1.next, curr2.next

        while curr1:
            val = curr1.val + carry
            print(val)
            carry = val // 10
            print(carry)
            node = ListNode(val % 10)
            curr1 = curr1.next
            if prev:
                prev.next = node
            else:
                res = node

            prev = node
        while curr2:
            val = curr2.val + carry
            carry = val // 10
            node = ListNode(val % 10)
            curr2 = curr2.next
            if prev:
                prev.next = node
            else:
                res = node

            prev = node
        if carry:
            node = ListNode(carry, None)
            prev.next = node
        return res
        #[1,2,3]
        #[5,7]

