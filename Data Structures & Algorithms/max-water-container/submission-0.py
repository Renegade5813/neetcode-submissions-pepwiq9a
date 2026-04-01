class Solution:
    def maxArea(self, heights: List[int]) -> int:
        carea = marea = 0
        n = len(heights)
        i=0
        j= n-1
        while i<j:
            ht = min(heights[i],heights[j])
            carea = ht*(j-i)
            if carea>marea:
                marea = carea
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return marea