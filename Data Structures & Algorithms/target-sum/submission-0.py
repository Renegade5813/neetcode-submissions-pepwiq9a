class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def backtrack(i, csum):
            if i == len(nums):
                return 1 if csum == target else 0
            return(backtrack(i+1, csum+nums[i]) + backtrack(i+1, csum-nums[i]))
        return backtrack(0,0)