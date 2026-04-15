class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()
        
        def dfs(i, csum):
            if csum == target:
                res.append(sub.copy())
                return
            if csum>target or i>= len(candidates):
                return
            sub.append(candidates[i])
            dfs(i+1, csum+candidates[i])
            sub.pop()
            
            while (i+1 <len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            dfs(i+1, csum)
        dfs(0, 0)
        return res



