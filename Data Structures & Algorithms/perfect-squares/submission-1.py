class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4
        
        def isSquareNum(num):
            s = int(math.sqrt(num))
            return s ** 2 == num
        
        i = 1
        while i ** 2 <= n:
            if isSquareNum(n - i ** 2):
                return 2
            i += 1
        
        return 3
