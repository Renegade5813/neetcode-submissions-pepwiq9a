class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm ={}
        for i, num in enumerate(nums):
            sec = target - nums[i]
            if sec in hm:
                return [hm[sec], i]
            hm[num] = i