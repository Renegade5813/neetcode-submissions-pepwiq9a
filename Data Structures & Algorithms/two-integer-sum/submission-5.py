class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs ={}
        for i,num in enumerate(nums):
            sec = target - nums[i]
            if sec in hs:
                return [hs[sec],i] 
            hs[num] =i