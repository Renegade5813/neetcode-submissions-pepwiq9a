class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        queue=deque()
        R,C= len(grid), len(grid[0])
        visit=set()
        time=0

        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i,j))
        
        while queue and fresh>0:

            for i in range(len(queue)):
                r,c= queue.popleft()
                neighbor=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in neighbor:
                    new_r,new_c=r+dr,c+dc
                    if new_r<0 or new_c<0 or new_r==R or new_c==C or grid[new_r][new_c]!=1 or (new_r,new_c) in visit:
                        continue
                    grid[new_r][new_c]=2
                    queue.append((new_r,new_c))
                    visit.add((new_r,new_c))
                    fresh-=1
            time+=1
        
        return time if fresh==0 else -1