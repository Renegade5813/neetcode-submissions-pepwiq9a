class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0

        height = len(grid)
        width = len(grid[0])

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '0':
                    continue
                
                if (i, j) in seen:
                    continue
                
                islands += 1
                stack = [ (i, j) ]

                while stack:
                    r, c = stack.pop()
                    if (r, c) in seen:
                        continue
                    if grid[r][c] == '0':
                        continue

                    seen.add( (r, c) )

                    if r < height - 1:
                        stack.append( (r + 1, c) )
                    if 0 < r:
                        stack.append( (r - 1, c) )
                    if c < width - 1:
                        stack.append( (r, c + 1) )
                    if 0 < c:
                        stack.append( (r, c - 1) )
        return islands