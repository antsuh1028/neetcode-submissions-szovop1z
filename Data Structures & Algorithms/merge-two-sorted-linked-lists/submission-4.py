# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one, two = list1, list2
        if not one:
            return two
        if not two:
            return one
        if one.val <= two.val:
            res = one
            one = one.next
        else:
            res = two
            two = two.next
        res_head = res

        while one and two:
            print(one.val,two.val)
            if one.val <= two.val:
                res.next = one
                one = one.next
            else:
                res.next = two
                two = two.next

            res = res.next
        if one:
            res.next = one
        if two:
            res.next = two
        return res_head
