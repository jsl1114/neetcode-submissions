class Solution:
    def numSquares(self, n: int) -> int:
        ret = 0
        while n > 0:
            nSqrtFlr = int(n ** 0.5)
            n = n - nSqrtFlr ** 2
            ret += 1
        return ret
