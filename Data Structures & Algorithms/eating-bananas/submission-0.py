class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = l + (r - l) // 2
            totalHours = sum([p/m if p%m==0 else p//m + 1 for p in piles])

            if totalHours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
            



