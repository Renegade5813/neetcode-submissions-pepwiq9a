class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()[::-1]
        l = 0
        for i in s:
            if i == ' ':
                break
            l += 1
        return l