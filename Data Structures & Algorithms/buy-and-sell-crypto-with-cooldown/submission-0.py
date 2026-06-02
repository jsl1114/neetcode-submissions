class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (i,buying): maxProfit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            hold = dfs(i+1,buying)
            if buying:
                buy = -prices[i] + dfs(i+1, not buying)
                dp[(i,buying)] = max(hold,buy)
            else:
                sell = prices[i] + dfs(i+2,not buying)
                dp[(i,buying)] = max(hold,sell)
            return dp[(i,buying)]

        return dfs(0, True)