class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            nn = self.findNext(n)
            if nn == 1:
                return True
            elif nn in seen:
                return False
            seen.add(n)
            n = nn
            
    
    def findNext(self,n):
        ret = 0
        for c in str(n):
            ret += int(c) 
        return ret