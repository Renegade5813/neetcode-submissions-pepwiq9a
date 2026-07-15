class Node:
    def __init__(self,key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.nex=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity= capacity
        self.LRU={}
        self.left=self.right=Node(0,0)
        self.left.nex=self.right
        self.right.prev= self.left         
    
    def remove(self,node):
        prev= node.prev
        nex=node.nex
        prev.nex=nex
        nex.prev=prev
    
    def insert(self,node):
        prev=self.right.prev
        prev.nex=node
        node.prev=prev
        node.nex=self.right
        self.right.prev=node



    def get(self, key: int) -> int:
        node = self.LRU.get(key,None)
        if node!=None:
            val= node.val
            self.remove(node)
            self.insert(node)
            return val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.LRU.get(key,None):
            node= self.LRU[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            new_node=Node(key,value)
            self.insert(new_node)
            self.LRU[key]=new_node
        if len(self.LRU)>self.capacity:
            to_remove=self.left.nex
            self.remove(to_remove)
            del self.LRU[to_remove.key]




        
