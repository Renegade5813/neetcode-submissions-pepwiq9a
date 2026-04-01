class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for i in s:
            if i.isalnum():
                ans += i
        return ans[::-1] == ans

