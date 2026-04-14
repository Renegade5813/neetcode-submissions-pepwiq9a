class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = ListNode(0,0)
        self.right = ListNode(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = self.right



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        self.remove(node)
        self.insert(node)
        return node.val
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
            self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(self.left.next)
            del self.cache[lru.key]
    

