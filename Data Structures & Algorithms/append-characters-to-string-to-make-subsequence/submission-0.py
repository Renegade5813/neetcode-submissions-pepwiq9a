class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = len(t)
        j = 0 
        k = 0

        while i > 0 and j < len(t) and k < len(s):
            if t[j] == s[k]:
                i -= 1
                j += 1
                k += 1
            else:
                k += 1
        return i