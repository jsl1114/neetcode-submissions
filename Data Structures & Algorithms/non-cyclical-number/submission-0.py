class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            nn = self.findNext(n)
            if nn == 1:
                return True
            if nn in seen:
                return False
            seen.add(nn)
            
    
    def findNext(self,n):
        ret = 0
        for c in str(n):
            ret += int(c) 
        return ret