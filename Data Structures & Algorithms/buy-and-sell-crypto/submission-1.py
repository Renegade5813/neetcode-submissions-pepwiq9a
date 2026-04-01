class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        if not prices:
            return 0
        bprice=prices[0] 
        for i in range(1,len(prices)):
            if prices[i]<bprice:
                bprice = prices[i]
            profit = prices[i]-bprice
            if profit>max_pro:
                max_pro = profit
        return max_pro  

