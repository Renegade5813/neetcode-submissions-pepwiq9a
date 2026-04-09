class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i in words:
            for j in words:
                if i != j:
                    if i in j:
                        ans.add(i)
                    elif j in i:
                        ans.add(j)
        return list(ans)