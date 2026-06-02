class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
            
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr,nc) not in seen
                        and grid[nr][nc] != -1):
                        grid[nr][nc] = grid[r][c] + 1
                    
                        seen.add((nr,nc))
                        q.append((nr,nc))



