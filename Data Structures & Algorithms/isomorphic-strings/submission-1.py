class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_ST = {}
        map_TS = {}
        for i,j in zip(s,t):
            if i in map_ST and map_ST[i] != j:
                return False
            if j in map_TS and map_TS[j] != i:
                return False
            map_ST[i] = j
            map_TS[j] = i
        return True