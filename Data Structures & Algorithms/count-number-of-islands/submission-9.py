class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C= len(grid),len(grid[0])
        visit=set()

        num_island=0
        def dfs(grid, r,c,visit):
            if r<0 or c<0 or r==R or c==C or grid[r][c]=='0' or (r,c) in visit:
                return 
            visit.add((r,c))
            neighbor=((1,0),(-1,0),(0,1),(0,-1))
            for dr,dc in neighbor:
                dfs(grid,r+dr,c+dc,visit)

        for r in range(R):
            for c in range(C):
                if grid[r][c]=='1' and (r,c) not in visit:
                    dfs(grid,r,c,visit)
                    num_island+=1
        
        return num_island


        