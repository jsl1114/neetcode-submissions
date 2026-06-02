class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        maxSide = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    maxSide = max(maxSide, dp[r+1][c+1])
        
        return maxSide ** 2