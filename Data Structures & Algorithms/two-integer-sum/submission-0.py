class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i, val in enumerate(nums):
            second = target- val
            if second in pair:
                return [pair[second],i]
            pair[val] = i