class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Calculate right_sum: total minus left_sum minus current element
            right_sum = total - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            # Update left_sum for next iteration (after checking current index)
            left_sum += nums[i]
        
        return -1
