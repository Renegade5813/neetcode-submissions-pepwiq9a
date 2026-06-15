class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        visit= set()
        q = deque()

        def bfs(i,j):
            if i >=ROW or i<0 or j<0 or j>= COL or (i,j) in visit or grid[i][j]==-1:
                return
            visit.add((i,j))
            q.append([i,j])
    
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==0:
                    q.append((i,j))
                    visit.add((i,j))
        dist =0
        while q:
            for x in range(len(q)):
                i,j = q.popleft()      
                grid[i][j] = dist
                bfs(i+1,j)
                bfs(i-1,j)
                bfs(i,j-1)
                bfs(i,j+1)   
            dist +=1           

        

                
                
                
             
