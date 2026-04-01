class MinStack:

    def __init__(self):
        self.stack =[]
        self.extra=[]
        self.length=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.length==0:
            self.extra.append(val)
        else:
            if self.extra[-1]<val:
                self.extra.append(self.extra[-1])
            else:
                self.extra.append(val)
        self.length+=1

    def pop(self) -> None:
        self.stack.pop()
        self.extra.pop()
        self.length-=1


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.extra[-1]
        
