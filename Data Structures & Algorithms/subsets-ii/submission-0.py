class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub =[]
        def dfs(start):
            res.append(sub.copy())
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                dfs(i+1)
                sub.pop()
              
            
        dfs(0)
        return res       