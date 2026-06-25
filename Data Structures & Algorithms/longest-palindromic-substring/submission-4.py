class Solution:
    def longestPalindrome(self, s: str) -> str:
        mid = 0
        half = 0
        for i in range(1,len(s)-1):
                k = 0
                while s[i-k-1] == s[i+k+1]:
                    k += 1
                    if k > half:
                        mid = i
                        half = k
                if s[i] == s[i-1]:
                    if half == 0:
                        half = 0.5
                        mid = i
        
        return s[mid-half: mid+half+1] if half > 0.5 else s[mid] * 2 if half == 0.5 else '' if len(s) == 0 else s[0]