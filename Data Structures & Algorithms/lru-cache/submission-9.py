class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _insert(self, node): # adds to the fron of list. rewrite the hashmap
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node
        return
        

    def _remove(self, node): # unlinks the node
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.hashMap:
            
            node = self.hashMap[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            self._remove(node)
        
            self._insert(node)
            return
        node = Node(key,value)
        self.hashMap[key] = node
        self._insert(node)

        if len(self.hashMap) > self.cap:
            last_visited = self.head.next
            self._remove(last_visited)
            del self.hashMap[last_visited.key]
        return






