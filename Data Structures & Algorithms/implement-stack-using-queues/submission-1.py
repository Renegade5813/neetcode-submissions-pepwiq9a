from collections import deque
class MyStack:

    def __init__(self):
        self.stack=deque()
        self.size=0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size+=1

        

    def pop(self) -> int:
        if self.size==0:
            return -1
        for i in range(self.size-1):
            self.push(self.stack.popleft())
        val=self.stack.popleft()
        self.size-=1
        return val

        

    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]
        else:
            return -1
        

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()