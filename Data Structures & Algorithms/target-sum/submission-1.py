class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, csum):
            if (i,csum) in dp:
                return dp[(i, csum)]
            if i == len(nums):
                return 1 if csum == target else 0
            dp[(i, csum)] = (backtrack(i+1, csum+nums[i]) + backtrack(i+1, csum-nums[i]))
            return dp[(i,csum)]
        return backtrack(0,0)