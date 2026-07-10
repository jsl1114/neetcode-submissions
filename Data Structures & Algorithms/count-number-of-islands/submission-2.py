class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            seen.add((i, j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1" and (ni, nj) not in seen:
                    dfs(ni, nj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    res += 1
                    dfs(i, j)
        
        return res