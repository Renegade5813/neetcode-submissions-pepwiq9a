class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        sub = []
        def dfs():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            for num in nums:
                if num not in sub:
                    sub.append(num)
                    dfs()
                    sub.pop()

            
        dfs()
        return res