class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if s[i] != c:
                continue
            i += 1
        
        return i == len(s)