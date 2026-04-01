class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            
            map1 = {}
            map2 = {}

            for i,j in zip(s,t):
                if i not in map1:
                    map1[i] = 1
                else:
                    map1[i] += 1

                if j not in map2:
                    map2[j] = 1
                else:
                    map2[j] += 1
            
            if map2 == map1:
                return True
            return False





















        # if len(s)!= len(t):
        #     return False
        
        # countS, countT = {},{}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1+ countT.get(t[i],0)
        # return countS==countT