class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def bfs(grid):
            R,C= len(grid), len(grid[0])
            if grid[0][0]==1 or grid[R-1][C-1]==1:
                return -1
            
            visit=set()
            queue=deque()

            queue.append((0,0))
            visit.add((0,0))
            length=1
            while queue:
                for i in range(len(queue)):
                    r,c= queue.popleft()
                    if r==R-1 and c==C-1:
                        return length
                    neighbor=[[1,0],[-1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]
                    for dr,dc in neighbor:
                        new_r,new_c= r+dr,c+dc
                        if new_r<0 or new_c<0 or new_r==R or new_c==C or grid[new_r][new_c]==1 or (new_r,new_c) in visit:
                            continue
                        queue.append((new_r,new_c))
                        visit.add((new_r,new_c))
                length+=1
            return -1
        return(bfs(grid))

        