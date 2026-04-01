class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            prefix = [1] * len(nums)
            suffix = [1] * len(nums)

            prefix[1] = nums[0]
            suffix[len(nums) - 2] = nums[-1]

            ans = []

            for i in range(1, len(nums)):
                prefix[i] = nums[i - 1] * prefix[i-1]
            
            for i in range(len(nums) - 2, -1, -1):
                suffix[i] = nums[i + 1] * suffix[i + 1]
            
            for i in range(len(nums)):
                ans.append(suffix[i] * prefix[i])
            
            return ans