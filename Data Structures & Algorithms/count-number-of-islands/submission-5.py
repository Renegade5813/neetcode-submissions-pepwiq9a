class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])        
        visit = set()
        islands =0

        def dfs(r,c):
            if r<0 or r>=R or c<0 or c>=C or grid[r][c] == "0" or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return


        for r in range(R):
            for c in range(C):
                if grid[r][c] =="1" and (r,c) not in visit:
                    
                    dfs(r,c)
                    islands +=1
        
        return islands



        