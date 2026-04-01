class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        gc = []
        for i, j in zip(customers, grumpy):
            gc += [i * j]
        
        maxx = 0
        
        base = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        # window should be length = minutes
        summ = sum(gc[0:minutes])
        maxx = summ

        # slide the window: i is the right end index
        for i in range(minutes, len(gc)):
            summ = summ - gc[i - minutes] + gc[i]
            maxx = max(maxx, summ)
        
        return base + maxx