from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        buy = -prices[0]   # bought stock
        sold = 0            # just sold
        rest = 0            # cooldown / doing nothing
        
        for i in range(1, len(prices)):
            prev_buy = buy
            prev_sold = sold
            prev_rest = rest
            
            buy = max(prev_buy, prev_rest - prices[i])  # buy or keep buying
            sold = prev_buy + prices[i]                  # sell today
            rest = max(prev_rest, prev_sold)              # stay idle
        
        return max(sold, rest)