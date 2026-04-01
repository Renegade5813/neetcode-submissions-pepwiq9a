class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub =[]
        nums.sort()
        def dfs(i, tot):
            if tot ==target:
                res.append(sub.copy())
                return
            if i>=len(nums) or tot>target:
                return
            
            sub.append(nums[i])
            dfs(i, tot + nums[i])
            sub.pop()
            dfs(i+1, tot)
        dfs(0,0)
        return res


