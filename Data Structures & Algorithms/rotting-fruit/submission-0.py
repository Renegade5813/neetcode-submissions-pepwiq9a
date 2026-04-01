class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1:
                    fresh +=1
                if grid[r][c] ==2:
                    q.append((r,c))
        directions = [[0,1], [1,0], [-1,0], [0, -1]]
        while fresh>0 and q:
            length =len(q)
            for i in range(length):
                r,c = q.popleft()

                for dr,dc in directions:
                    rows,cols = r+dr,c +dc
                    if (rows in range(row) and cols in range((col)) and grid[rows][cols] ==1):
                        grid[rows][cols] =2
                        q.append((rows,cols))
                        fresh -=1
            time+=1
        return time if fresh ==0 else -1