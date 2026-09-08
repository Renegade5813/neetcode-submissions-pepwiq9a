class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        return max(dict.values()) > 1