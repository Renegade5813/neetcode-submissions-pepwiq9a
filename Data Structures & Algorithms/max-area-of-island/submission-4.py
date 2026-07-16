class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        def dfs(grid,r,c):
            if r<0 or c<0 or r==R or c==C or grid[r][c]==0:
                return 0
            grid[r][c]=0
            area=1
            area+=dfs(grid,r+1,c)
            area+=dfs(grid,r-1,c)
            area+=dfs(grid,r,c+1)
            area+=dfs(grid,r,c-1)
            return area
        
        areas=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    areas=max(areas,dfs(grid,r,c))
        return areas

