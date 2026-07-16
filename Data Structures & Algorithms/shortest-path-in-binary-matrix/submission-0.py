class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def bfs(grid):
            R,C=len(grid),len(grid[0])
            if grid[0][0]==1 or grid[R-1][C-1]==1:
                return -1
            queue =deque()
            visit=set()
            length=1
            queue.append((0,0))
            visit.add((0,0))
            while queue:
                for i in range(len(queue)):
                    r,c=queue.popleft()
                    if r==R-1 and c==C-1:
                        return length
                    
                    neighbors =[[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
                    for dr,dc in neighbors:
                        new_r,new_c=r+dr,c+dc
                        if new_r<0 or new_c<0 or new_r==R or new_c==C or (new_r,new_c) in visit or grid[new_r][new_c]==1:
                            continue
                        queue.append((new_r,new_c))
                        visit.add((new_r,new_c))
                length+=1
            return -1

        return bfs(grid)


        