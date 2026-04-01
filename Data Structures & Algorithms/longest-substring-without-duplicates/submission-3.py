class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrSet = set() 
        left =0
        maxlen = 0
        for r in range(len(s)):
            while s[r] in chrSet:
                chrSet.remove(s[left])
                left+=1
            chrSet.add(s[r])
            maxlen = max(maxlen, r-left+1)
        return maxlen