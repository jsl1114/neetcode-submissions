from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and grid[ni][nj] == "1":
                    dfs(ni, nj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ret += 1
                    dfs(i, j)
        
        return ret