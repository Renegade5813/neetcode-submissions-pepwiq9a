class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        l, r = 0 , n-1
        while l<r:
            summ= numbers[l]+numbers[r]
            if summ <target:
                l+=1
            elif summ>target:
                r-=1
            else:
                return [l+1, r+1]