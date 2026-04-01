import random
class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        else:
            self.lst.append(val)
            self.idx[val] = len(self.lst) - 1
        return True        

    def remove(self, val: int) -> bool:
        if val in self.idx:
            temp = self.lst[self.idx[val]]
            self.idx[self.lst[len(self.lst) - 1]] = self.idx[val]
            self.lst[self.idx[val]] = self.lst[len(self.lst) - 1]
            self.lst[len(self.lst) - 1] = temp
            self.lst.pop()
            del self.idx[val]
            return True
        return False

        

    def getRandom(self) -> int:
        return self.lst[random.randint(0,len(self.lst)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()