class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        
        def dfs(sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
        
            for i in range(len(nums)):
                if nums[i] not in sub :
                    sub.append(nums[i])
                    dfs( sub)
                    sub.pop()
                
        dfs([])
        return res