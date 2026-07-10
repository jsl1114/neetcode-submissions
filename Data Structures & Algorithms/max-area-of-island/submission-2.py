class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            seen.add((i, j))
            area = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and grid[ni][nj] == 1:
                    area += dfs(ni, nj)
            return area

        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res