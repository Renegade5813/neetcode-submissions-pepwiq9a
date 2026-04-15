class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub =[]
        nums.sort()
        def dfs(i, csum):
            if csum == target:
                res.append(sub.copy())
                return
            if i>=len(nums) or csum>target:
                return
            sub.append(nums[i])
        
            dfs(i, nums[i]+ csum)
            sub.pop()
            dfs(i+1,csum)
        dfs(0,0)
        return res

