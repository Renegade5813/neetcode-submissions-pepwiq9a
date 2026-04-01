class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapp = {}
        for i in range(len(nums)):
            if nums[i] in mapp:
                return nums[i]
            mapp[nums[i]] = True