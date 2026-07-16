class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C= len(grid), len(grid[0])
        island=0
        visit=set()

        def dfs(grid,r,c):
            if r<0 or c<0 or r==R or c==C or grid[r][c]=='0'or (r,c) in visit:
                return 0
            visit.add((r,c))
            dfs(grid,r-1,c)
            dfs(grid,r+1,c)
            dfs(grid,r,c+1)
            dfs(grid,r,c-1)
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='1' and (r,c) not in visit:
                    dfs(grid,r,c)
                    island+=1
        return island
        