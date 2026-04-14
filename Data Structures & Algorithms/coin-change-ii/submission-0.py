class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, csum):
            if (i, csum) in dp:
                return dp[(i, csum)] 
            if csum == amount:
                return 1
            if csum > amount or i == len(coins):
                return 0 
            
            dp[(i,csum)] = dfs(i, csum+coins[i]) + dfs(i+1, csum)
            return dp[(i, csum)]
        return dfs(0, 0)