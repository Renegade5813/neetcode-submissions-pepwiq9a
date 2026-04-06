class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s=0
        current_1s=0
        for i in nums:
            if i == 1:
                current_1s += 1
                max_1s = max(current_1s, max_1s)
            else:
                current_1s = 0
                
        return max_1s