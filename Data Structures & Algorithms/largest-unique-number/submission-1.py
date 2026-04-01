class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        
        for i in range(1000, -1, -1):
            if count[i] == 1:
                return i
        
        return -1