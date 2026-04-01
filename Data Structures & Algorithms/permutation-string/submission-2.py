class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s11 = {}

        for ch in s1:
            if ch in s11:
                s11[ch] += 1
            else:
                s11[ch] = 1

        check = {}
        for idx in range(len(s1)):
            ch = s2[idx]
            if ch in check:
                check[ch] += 1
            else:
                check[ch] = 1
        
        if check == s11:
            return True

        i = 1
        j = i + len(s1) - 1  # right end index of the window
        while j < len(s2):
            left_char = s2[i - 1]
            check[left_char] -= 1
            if check[left_char] == 0:
                del check[left_char]

            right_char = s2[j]
            if right_char in check:
                check[right_char] += 1
            else:
                check[right_char] = 1

            if check == s11:
                return True
            
            i += 1
            j += 1

        return False