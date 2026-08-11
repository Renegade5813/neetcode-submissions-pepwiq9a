class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R,C= len(grid), len(grid[0])
        visit= set()

        def dfs(grid,r,c, visit):
            if r<0 or c<0 or r==R or c==C or (r,c) in visit or grid[r][c]==1:
                return 0
            if r==R-1 and c==C-1:
                return 1
            visit.add((r,c))
            count=0
            neighbor=((0,1),(0,-1),(1,0),(-1,0))
            for dr,dc in neighbor:
                count+=dfs(grid,r+dr,c+dc,visit)
            
            visit.remove((r,c))
            return count
        return dfs(grid,0,0,visit)

        