class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        for i in range(0, len(nums)+1):
            actual_sum += i
        missing_sum = 0
        for i in nums:
            missing_sum += i

        return actual_sum - missing_sum