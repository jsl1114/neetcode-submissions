class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] += 1
            dic[t[i]] -= 1
        

        for k in dic:
            if dic[k] != 0:
                return False
        return True
        