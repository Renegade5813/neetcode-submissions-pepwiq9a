class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        R,C= len(grid), len(grid[0])
        visit=set()

        def dfs(grid,r,c):
            if r<0 or c<0 or r==R or c==C or grid[r][c]==0 or (r,c) in visit:
                return 0
            
            visit.add((r,c))
            area=1
            neighbor=((1,0),(-1,0),(0,1),(0,-1))
            for dr,dc in neighbor:
                area+=dfs(grid,r+dr,c+dc)
            return area
        max_area=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1 and (r,c) not in visit:
                    max_area=max(max_area,dfs(grid,r,c))
        
        return max_area


        