class LinkedList:
    class Node:
        def __init__(self, data=-1):
            self.data= data
            self.next= None
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    
    def get(self, index: int) -> int:
        cur=self.head
        i=0
        if index >= self.size:
            return -1
        while(i<self.size):
            if i==index:
                return cur.data
            else:
                i+=1
                cur=cur.next
        

    def insertHead(self, val: int) -> None:
        new_node= self.Node(data=val)
        if self.size==0:
            self.head=new_node
            self.tail=new_node

        else:
            new_node.next=self.head
            self.head=new_node
        self.size+=1
        

    def insertTail(self, val: int) -> None:
        new_node=self.Node(data=val)
        if self.size==0:
            self.tail=new_node
            self.head=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1

    def remove(self, index: int) -> bool:
        if index>=self.size:
            return False
        if index==0  and self.head.next:
            self.head=self.head.next
            self.size-=1
            return True
        elif index==0 and self.head.next==None:
            self.head=None
            self.tail=None
            self.size-=1
            return True
        i=0
        cur=self.head
        while (i< index-1):
            i+=1
            cur=cur.next
        #cur is at prev of node to be deleted
        if cur.next==self.tail:
            cur.next=None
            self.tail=cur
        else:
            cur.next=cur.next.next
        
        self.size-=1
        return True



        

    def getValues(self) -> List[int]:
        arr=[]
        cur=self.head
        for i in range(self.size):
            arr.append(cur.data)
            cur=cur.next
        return arr
        
