class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+= str(len(i)) + "#" + i
        return res
    def decode(self, str) -> List[str]:
        res, i = [], 0
        while i<len(str):
            j =i
            while str[j]!="#":
                j+=1
            length = int(str[i:j])
            res.append(str[j+1: j+1 +length])
            i = j+1+length
        return res