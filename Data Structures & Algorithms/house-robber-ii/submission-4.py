class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.dfs(nums[1:]), self.dfs(nums[:-1]), nums[0])
    def dfs(self,nums):
        rob1, rob2 = 0,0
        for i in range(len(nums)):
            maxrob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = maxrob
        return rob2