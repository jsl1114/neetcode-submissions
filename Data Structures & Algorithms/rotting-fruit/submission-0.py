class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = minutes = 0
        rotten = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r,c))

        
        while True:
            cur = []
            for i, j in rotten:
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        fresh -= 1
                        cur.append((ni,nj))
                        grid[ni][nj] = 2
            
            if not cur:
                break
            
            minutes += 1
            rotten = cur
        
        return minutes if fresh == 0 else -1