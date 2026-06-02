class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        n1, n2 = 1, 1

        i = n - 1

        while i > 0:
            temp = n1 + n2
            n1 = n2
            n2 = temp
            i -= 1

        return n2
