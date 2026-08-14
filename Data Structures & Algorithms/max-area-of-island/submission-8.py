class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        R,C= len(grid), len(grid[0])

        def dfs(grid,r,c):
            if r<0 or c<0 or r==R or c==C or grid[r][c]==0:
                return 0
            grid[r][c]=0
            area=1
            neighbor=((1,0),(-1,0),(0,1),(0,-1))
            for dr,dc in neighbor:
                area+=dfs(grid,r+dr,c+dc)
            return area
        max_area=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    max_area=max(max_area,dfs(grid,r,c))
        
        return max_area


        