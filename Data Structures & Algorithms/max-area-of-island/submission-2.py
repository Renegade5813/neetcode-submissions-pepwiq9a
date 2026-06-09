class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        marea =0
    
        visit = set()

        def dfs(x,y,carea):
            if x<0 or x>=R or y<0 or y>=C or grid[x][y]==0 or (x,y) in visit:
                return carea
            carea +=1
            visit.add((x,y))
            carea =dfs(x+1, y, carea)
            carea =dfs(x, y-1, carea)
            carea =dfs(x, y+1, carea)
            carea =dfs(x-1, y, carea)
            return carea


        
        for i in range(R):
            for j in range(C):
                if grid[i][j] ==1 and (i,j) not in visit:
                    
                    marea = max(marea, dfs(i,j,0))
                    
        return marea

