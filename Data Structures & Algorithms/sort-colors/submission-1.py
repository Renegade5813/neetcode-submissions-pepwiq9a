class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts =[0]*3
        for i in nums:
            counts[i]+=1
        
        idx=0
        for i in range(0,len(counts)):
            for j in range(0, counts[i]):
                nums[idx]=i
                idx+=1
        
            
        