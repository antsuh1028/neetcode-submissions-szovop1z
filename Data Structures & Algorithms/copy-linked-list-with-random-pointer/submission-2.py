"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dct = {} #orignal pointer, pointer to that node
        current = head
        if current:
            new_head = Node(x=current.val)
            dct[current] = new_head
            current = current.next
        else:
            return None
        temp = new_head
        count = 0
        while current:
            new_node = Node(current.val)
            temp.next = new_node
            # temp.val = current.val

            dct[current] = new_node

            temp = temp.next
            current = current.next
            count+=1

        current = head
        temp = new_head

        while current:
            if current.random:
                temp.random = dct[current.random]
            temp = temp.next
            current = current.next
        return new_head

