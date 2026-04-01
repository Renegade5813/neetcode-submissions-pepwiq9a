class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i, num in enumerate(nums):
            sec = target - num
            if sec in mapp:
                return [mapp[sec], i] 
            mapp[num] =i
         