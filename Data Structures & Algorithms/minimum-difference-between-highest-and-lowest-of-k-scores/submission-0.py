class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()

        minn = float('inf')

        for i in range(len(nums)):
            if i+k-1 < len(nums):
                minn = min(nums[i+k-1] - nums[i], minn)
        return minn
