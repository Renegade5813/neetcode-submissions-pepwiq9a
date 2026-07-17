class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C= len(grid),len(grid[0])
        queue =deque()
        visit=set()
        time,fresh=0,0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
            
        def bfs(grid):
            nonlocal fresh, time

            while queue and fresh>0:
                for i in range(len(queue)):
                    neighbor=[[0,1],[0,-1],[1,0],[-1,0]]
                    r,c= queue.popleft()
                    for dr, dc in neighbor:
                        new_r,new_c=r+dr,c+dc
                        if new_r<0 or new_c<0 or new_r==R or new_c==C or (new_r,new_c) in visit or grid[new_r][new_c]!=1:
                            continue
                        grid[new_r][new_c]=2
                        queue.append((new_r,new_c))
                        visit.add((new_r,new_c))
                        fresh-=1
                time+=1
            return time if fresh==0 else -1
        return bfs(grid)
        
                
           
        