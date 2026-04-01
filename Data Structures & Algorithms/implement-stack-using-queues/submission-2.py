from collections import deque
class MyStack:

    def __init__(self):
        self.stack=deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)

        

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.push(self.stack.popleft())
        val=self.stack.popleft()
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