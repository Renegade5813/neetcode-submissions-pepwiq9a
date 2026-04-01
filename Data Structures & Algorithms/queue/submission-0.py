class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev
class Deque:
    
    def __init__(self):
        self.head= None
        self.tail=None
        self.size=0


    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        else:
            return False
        

    def append(self, value: int) -> None:
        new_node=Node(value)
        if self.size==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.size+=1
        return
            
        

    def appendleft(self, value: int) -> None:
        new_node=Node(value)
        if self.size==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.size+=1
        return

        

    def pop(self) -> int:
        if self.size==0:
            return -1
        elif self.size==1:
            val=self.head.val
            self.head=None
            self.tail=None
            self.size-=1
            return val
        else:
            val=self.tail.val
            self.tail=self.tail.prev
            self.size-=1
            return val

    def popleft(self) -> int:
        if self.size==0:
            return -1
        elif self.size==1:
            val=self.head.val
            self.head=None
            self.tail=None
            self.size-=1
            return val
        else:
            val=self.head.val
            self.head=self.head.next
            self.size-=1
            return val


        
