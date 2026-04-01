class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hs ={}
        for i, num in enumerate(numbers):
            comp = target - num
            if comp in hs:
                return [hs[comp]+1, i+1]
            hs[num] = i