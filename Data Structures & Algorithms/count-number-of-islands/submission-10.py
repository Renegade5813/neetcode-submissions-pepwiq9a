class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C= len(grid), len(grid[0])
        visit = set()

        def dfs(grid,r,c, visit):
            if r<0 or c<0 or r==R or c==C or grid[r][c]=='0' or (r,c) in visit:
                return 0
            visit.add((r,c))
            neighbor =((1,0),(-1,0),(0,1),(0,-1))
            for dr,dc in neighbor:
                dfs(grid,r+dr,c+dc,visit)
        
        count=0
        for r in range(R):
            for c in range(C):
                if (r,c) not in visit and grid[r][c]=='1':
                    dfs(grid,r,c,visit)
                    count+=1
        return count



        